# FastAPI CRUD API Documentation

This documentation provides an overview of the FastAPI CRUD API, which uses SQLAlchemy for database interaction with PostgreSQL.

## Project Structure

```
FastAPI-Simple-CRUD-Operation/
│── main.py         # Main FastAPI application
│── database.py     # Database configuration and session management
│── models.py       # SQLAlchemy models

```

## Installation

1. Clone the repository:
   ```bash
   git clone -b FastAPI-CRUD-Operation---SQLAlchemy https://github.com/decodersifat/FastAPI-Simple-CRUD-Operation.git
   ```

## Database Configuration

The database is configured in `database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse

password = urllib.parse.quote("yourpass")
SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:{password}@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### Dependency Injection for Database Session

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Models

The `models.py` file defines the `Post` model:

```python
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean , TIMESTAMP

class Post(Base):
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
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

