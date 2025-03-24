# Hussein Ghadhban - Portfolio Website

A modern, responsive portfolio website showcasing my work as a Full Stack Developer, built with FastAPI and TailwindCSS. This portfolio highlights my skills, projects, and achievements with a beautiful and interactive design.

## Features

- 🌓 Dark/Light mode support
- 📱 Fully responsive design
- 🎨 Modern UI with smooth animations
- 🚀 Fast performance with FastAPI
- 📝 Dynamic content management through JSON files
- 🔄 Infinite scroll animations for skills
- 📬 Contact form with email integration
- 🌐 Social media integration
- 🎯 SEO optimized

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: 
  - HTML5
  - TailwindCSS
  - JavaScript (Vanilla)
- **Libraries**:
  - AOS (Animate On Scroll)
  - Swiper.js
  - Font Awesome
- **Deployment**: Render

## Project Structure

```
myPortfolio/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   ├── icons/
│   └── data/
│       ├── skills.json
│       ├── achievements.json
│       └── config.json
├── templates/
│   └── index.html
├── main.py
└── README.md
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/hu55ain3laa/myPortfolio.git
cd myPortfolio
```

2. Install dependencies:
```bash
pip install fastapi uvicorn jinja2 python-multipart
```

3. Run the development server:
```bash
uvicorn main:app --reload
```

4. Open your browser and navigate to `http://localhost:8000`

## Customization

### Content Management

All content is managed through JSON files in the `static/data` directory:

- `skills.json`: Define your skills and categories
- `achievements.json`: List your achievements and certifications
- `config.json`: Configure which sections to display

### Styling

- Main styles are in `static/css/style.css`
- TailwindCSS classes are used for utility styling
- Custom animations and transitions are defined in the CSS file

### Images and Icons

- Add your profile image to `static/images/`
- Add skill icons to `static/icons/`
- Supported formats: SVG, PNG, JPG

## Deployment

This portfolio is deployed on Render:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables:
     - `PORT`: 8000

The site is live at: [https://hu55ain3laa.onrender.com](https://hu55ain3laa.onrender.com)

## Contact

- Email: ala.1995@yahoo.com
- GitHub: [hu55ain3laa](https://github.com/hu55ain3laa)
- LinkedIn: [hu55ain3laa](https://linkedin.com/in/hu55ain3laa) 