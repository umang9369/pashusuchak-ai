# PashuSuchak AI - Livestock Breed Identification System

A web application for identifying livestock breeds using AI image recognition technology. The application uses OpenAI for generating breed descriptions and Roboflow for image analysis and breed prediction.

## Project Structure

```
pashusuchak-ai/
├── frontend/             # Frontend web application
│   ├── index.html        # Main HTML file
│   ├── app.js            # Frontend JavaScript
│   └── styles.css        # CSS styles
├── backend/              # Backend API server
│   ├── app.py            # Flask application
│   ├── model.py          # AI model for breed identification
│   └── requirements.txt  # Python dependencies
├── components/           # Reusable UI components
├── lib/                  # Shared libraries
├── public/               # Static assets
├── scripts/              # Utility scripts
└── styles/               # Global styles
```

## Features

- Upload images of livestock animals
- AI-powered breed identification
- Detailed breed information display
- Responsive web interface

## Getting Started

### Frontend Setup

1. Open the `frontend` directory
2. Open `index.html` in a web browser

### Backend Setup

1. Navigate to the `backend` directory
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```
   python app.py
   ```

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **AI Models**: OpenAI API (for breed descriptions), Roboflow API (for image analysis)
- **Text-based Sprites**: Custom MCP (Monospace Character Painting) implementation

## Deployment

This application can be deployed in two ways:

1. **Local Deployment**: Follow the setup instructions above
2. **GitHub Pages**: The frontend is hosted on GitHub Pages, while the backend needs to be deployed separately on a service like Heroku, Render, or similar platforms

## API Keys

To use the application with real predictions, you'll need to add your own API keys:

1. OpenAI API key for breed descriptions
2. Roboflow API key for image analysis

Add these keys to the `model.py` file in the backend directory.
- **AI Model**: Placeholder (to be implemented with actual ML model)

## Future Enhancements

- Implement actual machine learning model for breed identification
- Add user authentication
- Create database for storing analysis history
- Expand breed database with more information