from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
import openai
import os

app = FastAPI(title="Chatbot App", description="Chatbot con frontend y backend en FastAPI")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    status: str = "success"

def get_chatbot_response(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil y amigable."},
                {"role": "user", "content": message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat", response_class=HTMLResponse)
async def chat_form(request: Request, message: str = Form(...)):
    if not message:
        response = "Por favor, escribe un mensaje."
    else:
        response = get_chatbot_response(message)
    return templates.TemplateResponse("index.html", {"request": request, "user_message": message, "bot_response": response})

@app.post("/api/chat", response_model=ChatResponse)
async def chat_api(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")
    response = get_chatbot_response(request.message)
    return ChatResponse(response=response)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "chatbot"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)