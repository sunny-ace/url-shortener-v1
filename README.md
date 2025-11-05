# URL Shortener (FastAPI)

A simple URL shortening application built using **FastAPI**, **Jinja2 templates**, and **Python**.  
The application allows users to input a long URL and receive a shortened version.  
When the shortened URL is visited, it redirects the user back to the original link.

## Features
- Accepts long URLs from the user through a web form.
- Generates a short unique code for each URL.
- Stores URL mappings in memory (dictionary).
- Redirects users to the original URL when the shortened link is visited.
- Basic HTML frontend using Jinja2 templates.

## Tech Stack
- Python 3.13+
- FastAPI
- Jinja2 Templates
- Uvicorn

## Project Structure
app/
┣ main.py
┣ routes/
│ ┗ url_routes.py
┣ templates/
│ ┗ index.html
┗ utils/
┗ shortener.py


## How It Works
1. The user submits a long URL through the form on the home page.
2. A short code is generated using a helper function (`create_short_code()`).
3. The short code and long URL are stored in an in-memory dictionary (`url_db`).
4. The application returns a shortened URL to the user.
5. When the user visits the shortened URL, the application looks up the original URL and redirects.

## Installation and Setup

### Clone the repository
```bash
git clone <your-repo-link>
cd url-shortener


## Create and activate a virtual environment (optional but recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

## Install dependencies
pip install fastapi uvicorn jinja2

## Run the app
uvicorn app.main:app --reload

## Visit in browser
http://127.0.0.1:8000


## API Testing With Swagger UI
FastAPI automatically generates API documentation.
Open:
http://127.0.0.1:8000/docs

Current Limitation

All shortened URLs are stored in memory only.
This means data is lost when the server restarts.

Next Improvements (Future Work)

Add a database (SQLite or PostgreSQL).

Add user accounts and link history.

Track link click analytics.

Add expiration date for shortened links.
End of README.md

