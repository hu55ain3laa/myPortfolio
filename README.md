# Personal Portfolio Website

A modern, responsive portfolio website built with FastAPI and TailwindCSS.

## Features

- 🎨 Modern and responsive design
- 🌓 Dark/Light mode support
- 📱 Mobile-friendly layout
- ⚡ Fast and optimized performance
- 🔒 Secure contact form
- 🎯 SEO optimized

## Tech Stack

- FastAPI
- TailwindCSS
- Jinja2 Templates
- Python 3.12+

## Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
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
docker build -t your-registry/portfolio:latest .
docker push your-registry/portfolio:latest
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

The website can be configured through the following JSON files in the `static/data` directory:

- `config.json`: General website configuration
- `skills.json`: Skills and technologies
- `achievements.json`: Achievements and certifications

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/portfolio](https://github.com/yourusername/portfolio) 