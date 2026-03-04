# URL Shortener

A full-stack URL shortening service built with FastAPI and PostgreSQL.

## Live Demo
[https://urlshortener-production-1801.up.railway.app](https://urlshortener-production-1801.up.railway.app)

## Features
- Shorten any URL instantly
- Track click counts for each link
- Dashboard with top links and click analytics
- Bar chart visualization of link performance
- Duplicate URL prevention
- Input validation

## Tech Stack
- **Backend:** FastAPI, Python
- **Database:** PostgreSQL, SQLAlchemy ORM
- **Frontend:** HTML, Tailwind CSS, Chart.js
- **Deployment:** Railway

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/shorten` | Create a short URL |
| GET | `/{short_code}` | Redirect to original URL |
| GET | `/stats/{short_code}` | Get URL statistics |
| GET | `/links` | Get all links sorted by clicks |

## Run Locally
```bash
git clone https://github.com/TasnimZarin/URL_Shortener.git
cd URL_Shortener
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables
```
DATABASE_URL=postgresql://username@localhost/url_shortener
```