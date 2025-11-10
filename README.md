# Chatbot con FastAPI y OpenAI

## Características

- 🔹 Backend en FastAPI 
- 🔹 Integración con OpenAI: Respuestas inteligentes con GPT-3.5-turbo.  
- 🔹 Frontend HTML/CSS/JS

---

## Requisitos previos

-  **Python 3.7+** → [Descargar](https://www.python.org/downloads/)  
- 🔑 **Cuenta de OpenAI** → [Regístrese aquí](https://platform.openai.com/)  
-  **Git** → [Instalar Git](https://git-scm.com/downloads) (Debe colocar su API Key dentro del código como señalé)
- 📁 Archivos estáticos: Se pueden reemplazar si desea (Los que se encuentran en la carpeta static)
  

---

## 🚀 Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Ale4400/Python-AI-chatbot.git
cd Python-AI-chatbot

Página Principal: Cargue el frontend.
Enviar Mensajes:
Usa el input de texto y presiona "Enviar" o Enter.
El bot responde en tiempo real usando OpenAI.
API: Envía POST a /api/chat con JSON {"message": "Hola"} para respuestas programáticas.
Salud: Visite /health para verificar el estado del servicio.
