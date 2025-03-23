# Hussein Ghadhban - Portfolio Website

A modern, responsive portfolio website showcasing my work as a Full Stack Developer, built with FastAPI and TailwindCSS.

## Features

- 🎨 Modern and responsive design with smooth animations
- 🌓 Dark/Light mode support
- 📱 Mobile-first approach
- ⚡ Fast and optimized performance
- 🔒 Secure contact form
- 🎯 SEO optimized
- 📊 Dynamic content management through JSON files
- 🎨 Beautiful UI with TailwindCSS
- 🚀 FastAPI backend for optimal performance

## Tech Stack

- **Backend**: FastAPI (Python 3.12+)
- **Frontend**: 
  - TailwindCSS for styling
  - Jinja2 Templates
  - Font Awesome icons
  - AOS (Animate On Scroll)
  - Swiper.js for carousels
- **Deployment**: Docker & Docker Compose

## Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/hu55ain3laa/myPortfolio.git
cd myPortfolio
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
uvicorn main:app --reload
```

5. Open your browser and navigate to `http://localhost:8000`

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t portfolio .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 portfolio
```

## Production Deployment

### Option 1: Using Docker (Recommended)

1. Build and push the Docker image to a container registry:
```bash
docker build -t hu55ain3laa/portfolio:latest .
docker push hu55ain3laa/portfolio:latest
```

2. Deploy using Docker Compose:
```bash
docker-compose up -d
```

### Option 2: Direct Server Deployment

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export PORT=8000
```

3. Run with a production server (e.g., Gunicorn):
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

4. Set up a reverse proxy (e.g., Nginx) in front of the application.

## Configuration

The website content can be easily customized through JSON files in the `static/data` directory:

- `config.json`: General website configuration
- `skills.json`: Skills and technologies
- `achievements.json`: Achievements and certifications

### Example Configuration

```json
{
  "name": "Hussein Ghadhban",
  "role": "Full Stack Developer",
  "about": "Your about text here",
  "contact": {
    "email": "your.email@example.com",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername"
  }
}
```

## Project Structure

```
myPortfolio/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── data/
│       ├── config.json
│       ├── skills.json
│       └── achievements.json
├── templates/
│   └── index.html
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Hussein Ghadhban - [ala.1995@yahoo.com](mailto:ala.1995@yahoo.com)

- GitHub: [hu55ain3laa](https://github.com/hu55ain3laa)
- LinkedIn: [hu55ain3laa](https://linkedin.com/in/hu55ain3laa)

Project Link: [https://github.com/hu55ain3laa/myPortfolio](https://github.com/hu55ain3laa/myPortfolio) 