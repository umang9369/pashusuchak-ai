#  PashuSuchak AI

An AI-powered cattle breed detection and livestock assistance platform designed to help farmers identify cattle breeds from images and receive breed-specific insights, health recommendations, feeding guidance, and farmer-friendly information.

## Overview

PashuSuchak AI combines Computer Vision and Large Language Models (LLMs) to provide an intelligent livestock analysis system.

The application accepts an image uploaded by the user, detects the cattle breed using a computer vision model, and then uses an LLM to generate detailed breed information, health guidance, feeding recommendations, and farmer-oriented explanations.

This project was built with a FastAPI backend and AI-powered inference pipeline using Groq and Qwen3.6-27B.

---

## Problem Statement

Many farmers and livestock owners may not have easy access to breed experts or veterinary guidance. Identifying cattle breeds and understanding breed-specific characteristics can be difficult, especially for new farmers.

PashuSuchak AI aims to bridge this gap by providing:

* Automated cattle breed identification
* Breed-specific information
* Feeding recommendations
* Health guidance
* Easy-to-understand farmer assistance

---

## Features

### Computer Vision Based Breed Detection

* Upload cattle images
* Breed identification using Roboflow-hosted detection/classification models
* Confidence score generation

### AI-Powered Livestock Assistant

Using Groq API and Qwen3.6-27B:

* Breed description generation
* Physical characteristics explanation
* Feeding recommendations
* Health-related guidance
* Breed-specific information
* Farmer-friendly responses

### FastAPI Backend

* RESTful API architecture
* Image upload handling
* AI inference pipeline
* JSON-based responses
* Easy frontend integration

### Frontend Integration

Frontend communicates with the FastAPI backend through REST APIs.

Frontend stack:

* HTML
* CSS
* JavaScript

---

# System Architecture

```text
                +------------------+
                |     Frontend     |
                | HTML/CSS/JS UI   |
                +--------+---------+
                         |
                         |
                         v
                +------------------+
                |     FastAPI      |
                | Backend Service  |
                +--------+---------+
                         |
          +--------------+--------------+
          |                             |
          v                             v

 +------------------+      +-----------------------+
 | Roboflow Model   |      | Groq API             |
 | Breed Detection  |----->| Qwen3.6-27B LLM      |
 +------------------+      +-----------------------+
                                      |
                                      v
                        +---------------------------+
                        | Breed Insights            |
                        | Feeding Recommendations   |
                        | Health Guidance           |
                        | Farmer Assistance         |
                        +---------------------------+
```

---

# Tech Stack

## Backend

* FastAPI
* Python
* Uvicorn

## AI & Machine Learning

* Groq API
* Qwen3.6-27B
* Roboflow

## Frontend

* HTML
* CSS
* JavaScript

## API Communication

* REST APIs
* JSON

---

# AI Workflow

### Step 1: Image Upload

User uploads a cattle image through the frontend.

### Step 2: Breed Detection

The image is sent to the Roboflow model for cattle breed detection.

Example output:

```json
{
  "breed": "Gir Cow",
  "confidence": 0.92
}
```

### Step 3: LLM Processing

The detected breed information is sent to Qwen3.6-27B through Groq.

Example prompt:

```text
Detected Breed: Gir Cow

Provide:
- Breed description
- Physical characteristics
- Feeding recommendations
- Health considerations
- Suitable climate
```

### Step 4: Response Generation

The LLM generates farmer-friendly information.

### Step 5: Final Output

The frontend receives:

```json
{
  "breed": "Gir Cow",
  "confidence": 0.92,
  "description": "...",
  "feeding_guidance": "...",
  "health_recommendations": "...",
  "farmer_advisory": "..."
}
```

---

# API Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Analyze Cattle Image

```http
POST /analyze
```

Request:

```multipart/form-data
image=<uploaded_file>
```

Response:

```json
{
  "breed": "Gir Cow",
  "confidence": 0.92,
  "description": "...",
  "feeding_guidance": "...",
  "health_recommendations": "...",
  "farmer_advisory": "..."
}
```

---

# Project Structure

```text
PashuSuchak-AI
│
├── backend/
│   ├── app/
│   ├── routes/
│   ├── services/
│   ├── ai/
│   ├── models/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/umang9369/pashusuchak-ai.git

cd pashusuchak-ai
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

ROBOFLOW_API_KEY=your_roboflow_api_key
```

## Run Backend

```bash
uvicorn main:app --reload
```

---

# Current Status

Project is currently under active development.

Implemented:

* Backend architecture
* AI workflow design
* API integration planning
* Image processing pipeline

Pending / In Progress:

* Roboflow model integration stabilization
* API deployment
* Production testing
* Model accuracy improvements

---

# Known Limitations

* Roboflow API integration is currently under development.
* Production deployment has not yet been completed.
* Performance depends on external API availability.
* AI-generated recommendations should not replace professional veterinary consultation.

---

# Future Improvements

* Multi-language farmer support
* Disease detection
* Vaccination reminders
* Livestock management dashboard
* Mobile application
* Offline inference support
* Voice-based farmer assistant
* Analytics dashboard

---

# My Contribution

This project highlights my work in Backend Development and AI Integration.

Responsibilities:

* Designed backend architecture using FastAPI.
* Developed API workflow for image analysis.
* Integrated Groq API and Qwen3.6-27B for AI-generated responses.
* Designed LLM prompt flow for breed insights and farmer assistance.
* Built image processing and response generation pipeline.
* Worked on system integration between computer vision and LLM components.

Frontend development and Roboflow model training/integration were handled separately, while my primary focus was Backend Engineering and AI functionality.

---

#

Backend Developer | AI Enthusiast

Focused on Backend Engineering, AI Systems, FastAPI, LLM Applications, RAG Systems, and Agentic AI.
