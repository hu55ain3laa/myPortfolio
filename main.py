from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from pathlib import Path
import json
import os
import re
from typing import Dict, Any

# Try to import production settings
try:
    from prod_settings import USE_HTTPS, DOMAIN, FORCE_HTTPS_RESOURCES
    is_production = True
except ImportError:
    # Default to development settings
    USE_HTTPS = False
    DOMAIN = "localhost:8000"
    FORCE_HTTPS_RESOURCES = False
    is_production = os.environ.get("ENVIRONMENT") == "production"

# Custom middleware to redirect HTTP to HTTPS
class HTTPSRedirectMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Check if the request came from HTTP
        if request.headers.get("x-forwarded-proto") == "http":
            # Get the full URL and redirect to HTTPS
            url = request.url
            https_url = str(url).replace("http://", "https://")
            return RedirectResponse(https_url)
        return await call_next(request)

# Custom middleware to modify response headers for HTTPS content
class HTTPSHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Content-Security-Policy"] = "upgrade-insecure-requests"
        return response

app = FastAPI(
    title="Hussein Ghadhban Portfolio Website",
    description="Personal portfolio website built with FastAPI",
    version="1.0.0"
)

# Add HTTPS redirect middleware
app.add_middleware(HTTPSRedirectMiddleware)
# Add headers middleware
app.add_middleware(HTTPSHeadersMiddleware)

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

# Configure templates with custom settings
templates = Jinja2Templates(directory="templates")

# Add custom functions to templates
def secure_url_for(name: str, **path_params):
    """Generate URLs that are always HTTPS in production"""
    url = app.url_path_for(name, **path_params)
    if is_production or FORCE_HTTPS_RESOURCES:
        return f"https://{DOMAIN}{url}"
    return url

# Add the function to Jinja templates
templates.env.globals["secure_url_for"] = secure_url_for

# Create a custom middleware for request base URL
class URLBaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Force HTTPS for production
        if is_production or request.headers.get("x-forwarded-proto") == "https":
            request.state.url_scheme = "https"
        else:
            request.state.url_scheme = request.url.scheme
        
        response = await call_next(request)
        return response

app.add_middleware(URLBaseMiddleware)

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

# Process skills data to fix icon paths
def process_skills_data(skills_data: Dict[str, Any]) -> Dict[str, Any]:
    for category in skills_data.values():
        if "skills" in category:
            for skill in category["skills"]:
                if "icon" in skill and isinstance(skill["icon"], str):
                    # Check if the icon path starts with 'static/'
                    if skill["icon"].startswith("static/"):
                        icon_path = skill["icon"].replace("static/", "")
                        if is_production or FORCE_HTTPS_RESOURCES:
                            skill["icon"] = f"https://{DOMAIN}/static/{icon_path}"
                        else:
                            skill["icon"] = f"/static/{icon_path}"
    return skills_data

skills_data = process_skills_data(load_json_file('static/data/skills.json'))
achievements_data = load_json_file('static/data/achievements.json')
config = load_json_file('static/data/config.json')

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        # Set base URL scheme to HTTPS in production
        request.state.url_scheme = "https" if is_production else request.url.scheme
        
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "url_scheme": "https" if is_production else request.url.scheme,
                "is_production": is_production,
                "domain": DOMAIN,
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