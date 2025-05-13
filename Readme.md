# Remind-me-later

**Remind-me-later** is a simple web service that allows users to schedule reminders by specifying a message, date, time,
and delivery method (SMS or Email). The frontend UI is handled by a JS app; this project implements the backend API
using Django and Django REST Framework.

---

## Features

- Create reminders with:
    - Message text
    - Date & time
    - Delivery method: `sms` or `email`
- Extensible for future delivery methods
- OpenAPI 3.0-compliant API with:
    - Swagger UI
    - ReDoc
- Uses Django ORM and DRF for fast development and maintainability

---

## Tech Stack

- Python 3.8+
- Django 3.2+ / 4.x
- Django REST Framework
- drf-spectacular (OpenAPI documentation)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/remind-me-later.git
cd remind-me-later
````

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

# Curl For Testing

curl --location 'localhost:8000/api/reminders/' \
--header 'Content-Type: application/json' \
--data '{
"message": "Attend the meeting",
"remind_at": "2025-05-12T17:30:00Z",
"remind_via": "email"
}
'

## API Documentation
Swagger UI: http://localhost:8000/api/docs/swagger/

ReDoc UI: http://localhost:8000/api/docs/redoc/