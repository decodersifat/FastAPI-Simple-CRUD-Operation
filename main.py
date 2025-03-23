from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

# Database connection
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

class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/posts")
def get_posts():
    try:
        cursor.execute(""" SELECT * FROM  public."Posts" """)
        all_posts = cursor.fetchall()
        return {"data": all_posts}
    except Exception as e:
        conn.rollback() 
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.post("/createpost")
def create_post(post:Post):
    cursor.execute("""INSERT INTO public."Posts" (title,content,published) VALUES (%s, %s,%s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


@app.get("/singlepost/{id}")
def get_single_post(id:int):
    cursor.execute("""SELECT * FROM public."Posts" WHERE id = %s""", (str(id)))
    new_post = cursor.fetchone()
    return {"data" : new_post}

@app.delete("/delete/{id}")
def delete_post(id:int):
    cursor.execute("""DELETE FROM public."Posts" WHERE id = %s RETURNING * """, (str(id)))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@app.put("/update/{id}")
def update_post(id:int,post:Post):
    cursor.execute("""UPDATE public."Posts" SET title=%s,content=%s,published=%s WHERE id=%s RETURNING * """, (post.title, post.content,post.published,str(id)))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data":new_post}