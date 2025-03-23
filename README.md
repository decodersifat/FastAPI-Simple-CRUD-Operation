# FastAPI CRUD API Documentation

This documentation provides an overview of the FastAPI CRUD API, with different database integrations.

## Available Branches

1. **FastAPI CRUD with SQLAlchemy** ([View Branch](https://github.com/decodersifat/FastAPI-Simple-CRUD-Operation/tree/FastAPI-CRUD-Operation---SQLAlchemy))
2. **FastAPI CRUD with psycopg2** ([View Branch](https://github.com/decodersifat/FastAPI-Simple-CRUD-Operation/tree/FastAPI-CRUD-Operation---psycopg2))

## Project Structure

```
FastAPI-Simple-CRUD-Operation/
│── main.py         # Main FastAPI application

```

## Installation

1. Clone the repository:
   ```bash
   git clone -b FastAPI-CRUD-Operation---psycopg2 https://github.com/decodersifat/FastAPI-Simple-CRUD-Operation.git
   ```

## Database Connection (psycopg2)

The database connection is handled in `main.py`:

```python
import psycopg2
from psycopg2.extras import RealDictCursor
import time

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='yourpass',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print("Database connection failed")
        print("Error:", error)
        time.sleep(2)
```

## API Endpoints

### Get All Posts

```http
GET /posts
```

#### Response:

```json
{
  "data": [
    {"id": 1, "title": "First Post", "content": "Hello FastAPI!", "published": true}
  ]
}
```

### Create a New Post

```http
POST /createpost
```

#### Request Body:

```json
{
  "title": "New Post",
  "content": "This is a new post.",
  "published": true
}
```

#### Response:

```json
{
  "data": {
    "id": 2,
    "title": "New Post",
    "content": "This is a new post.",
    "published": true
  }
}
```

### Get a Single Post by ID

```http
GET /singlepost/{id}
```

#### Response:

```json
{
  "data": {
    "id": 1,
    "title": "First Post",
    "content": "Hello FastAPI!",
    "published": true
  }
}
```

### Delete a Post by ID

```http
DELETE /delete/{id}
```

#### Response:

```json
{
  "data": 1
}
```

### Update a Post by ID

```http
PUT /update/{id}
```

#### Request Body:

```json
{
  "title": "Updated Post",
  "content": "Updated content.",
  "published": false
}
```

#### Response:

```json
{
  "data": {
    "id": 1,
    "title": "Updated Post",
    "content": "Updated content.",
    "published": false
  }
}
```

## Running the API

Run the FastAPI server using:

```bash
fastapi dev main.py
```

The API will be available at:

```
http://127.0.0.1:8000
```

## Testing

You can test the API using:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

## License

This project is open-source and available under the [MIT License](LICENSE).

