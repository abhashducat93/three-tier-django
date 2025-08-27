FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Production command with Gunicorn
CMD ["sh", "-c", "sleep 5 && python manage.py migrate && gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 3 --pythonpath /app"]
