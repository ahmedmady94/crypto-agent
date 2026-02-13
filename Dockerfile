# 1. Use a small, official Python image
FROM python:3.11-slim

# 2. Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory inside the container
WORKDIR /app

# 4. Install system dependencies (optional but safe)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy dependency list first (better caching)
COPY requirements.txt .

# 6. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy the application code
COPY app ./app

# 8. Expose FastAPI port
EXPOSE 8000

# 9. Run FastAPI via uvicorn
# for local run (static port) : CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]