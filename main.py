from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
# import psycopg2
# from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind = engine)


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/posts")
def get_posts(db:Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return {"data":post}



@app.post("/createpost")
def create_post(post:Post , db:Session = Depends(get_db)):
    
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}




@app.get("/singlepost/{id}")
def get_single_post(id:int , db:Session = Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.id == id).first()
    return {"data": post}
    



@app.delete("/delete/{id}")
def delete_post(id:int, db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).delete(synchronize_session=False)
    db.commit()
    return {"data": post}


@app.put("/update/{id}")
def update_post(id:int,post:Post,  db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    posts = post_query.first()
    
    return {"data":posts}




