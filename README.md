# Celery Task Queue with Flower

A modern Flask + Celery distributed task queue with Flower monitoring dashboard.

## Tech Stack

- **Flask 3.0** - Web framework
- **Celery 5.3** - Distributed task queue
- **Flower 2.0** - Real-time Celery monitoring
- **Redis** - Message broker & result backend

## Local Development

### Prerequisites

- Python 3.10+
- Redis server running locally

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables (optional)
export CELERY_BROKER_URL=redis://localhost:6379/0
export CELERY_RESULT_BACKEND=redis://localhost:6379/0
export FLASK_SECRET_KEY=your-secret-key
```

### Running

Start each service in a separate terminal:

```bash
# Terminal 1: Start Redis (if not running as a service)
redis-server

# Terminal 2: Start Celery worker
celery -A tasks worker --loglevel=info

# Terminal 3: Start Flower monitoring
celery -A tasks flower --port=5555

# Terminal 4: Start Flask app
flask run
```

Then visit:
- **Web App**: http://localhost:5000
- **Flower Dashboard**: http://localhost:5555

## Deployment

Follow the guide at https://render.com/docs/deploy-celery for production deployment on Render.

## Features

- Asynchronous task execution
- Real-time task monitoring via Flower
- Task result tracking with Redis backend
- Modern, responsive UI
