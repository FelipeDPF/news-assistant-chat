# ===================================================================
# main.py — News Assistant Backend (FastAPI)
# Version: 0.1.0-beta
# 
# This is the backend server for the News Assistant App.
# It uses FastAPI to provide a web interface that serves:
#  - the frontend (index.html rendered via Jinja2)
#  - a POST endpoint that receives a search query and fetches news
#    from NewsAPI.org based on that query
#
# The frontend interacts with this backend to retrieve and display
# news articles in a conversational chat format.
#
# API keys are securely loaded from a .env file using python-dotenv.
# ===================================================================
__version__ = "0.1.0-beta"
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")  # Protect your API key from being exposed in code

# Create the FastAPI application instance
app = FastAPI()

# Enable CORS so the frontend (index.html with JS) can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Consider restricting in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up Jinja2 template engine to render HTML
templates = Jinja2Templates(directory="templates")

# Route to serve the frontend chat interface
@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to handle news search requests from frontend
@app.post("/news")
async def get_news(request: Request):
    try:
        body = await request.json()
        query = body.get("query")

        # Build NewsAPI URL based on whether the user entered a search query
        url = (
            f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey={API_KEY}"
            if query
            else f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        )

        # Send GET request to NewsAPI
        r = requests.get(url)
        data = r.json()

        # Extract articles or default to empty list
        articles = data.get("articles", [])

        # Return results as JSON
        return JSONResponse(content={"articles": articles})

    except Exception as e:
         # Return a generic error response if something goes wrong
        return JSONResponse(content={"error": str(e)}, status_code=500)