from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json
import os
from typing import Dict, Any

app = FastAPI(
    title="Hussein Ghadhban Portfolio Website",
    description="Personal portfolio website built with FastAPI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://localhost:3000",
        "https://hu55ain3laa.github.io",
        "https://hu55ain3laa.com",
        "https://www.hu55ain3laa.com",
        "https://*.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def load_json_file(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON")
        return {}

skills_data = load_json_file('static/data/skills.json')
achievements_data = load_json_file('static/data/achievements.json')
config = load_json_file('static/data/config.json')

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "title": "Hussein Ghadhban - Portfolio",
                "name": "Hussein Ghadhban",
                "role": "Full Stack Developer",
                "about": "I am a passionate Full Stack Developer with expertise in building scalable web applications and machine learning solutions. With a strong foundation in both frontend and backend technologies, I create efficient and user-friendly applications that solve real-world problems.",
                "skills": skills_data,
                "achievements": achievements_data.get("achievements", []),
                "certifications": achievements_data.get("certifications", []),
                "config": config,
                "projects": [
                    {
                        "title": "AI Image Recognition System",
                        "description": "A deep learning-based system that can identify and classify objects in images with high accuracy.",
                        "technologies": ["Python", "TensorFlow", "FastAPI", "React"],
                        "github_url": "https://github.com/hu55ain3laa/ai-image-recognition",
                        "live_url": "https://ai-image-recognition.demo"
                    },
                    {
                        "title": "E-commerce Platform",
                        "description": "A full-stack e-commerce platform with real-time inventory management and payment processing.",
                        "technologies": ["Python", "Django", "React", "PostgreSQL"],
                        "github_url": "https://github.com/hu55ain3laa/ecommerce-platform",
                        "live_url": "https://ecommerce.demo"
                    },
                    {
                        "title": "Data Analytics Dashboard",
                        "description": "An interactive dashboard for visualizing and analyzing complex datasets.",
                        "technologies": ["Python", "FastAPI", "React", "D3.js"],
                        "github_url": "https://github.com/hu55ain3laa/data-dashboard",
                        "live_url": "https://dashboard.demo"
                    }
                ],
                "contact": {
                    "email": "ala.1995@yahoo.com",
                    "github": "https://github.com/hu55ain3laa",
                    "linkedin": "https://linkedin.com/in/hu55ain3laa"
                },
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=False
    ) 