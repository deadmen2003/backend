from fastapi import APIRouter, HTTPException
from app.controllers.post_controller import *
from models.post_model import post

router = APIRouter()

nuevo_post = postController()


@router.post("/create_post")
async def create_post(post: post):
    rpta = nuevo_post.create_post(post)
    return rpta

@router.get("/get_post/{post_id}",response_model=post)
async def get_post(post_id: int):
    rpta = nuevo_post.get_post(post_id)
    return rpta

@router.get("/get_posts/")
async def get_posts():
    rpta = nuevo_post.get_posts()
    return rpta

@router.put("/put_post/{id}")
async def put_post(id:int, post: post):
    rpta = nuevo_post.put_post(id, post)
    return rpta

@router.delete("/delete_post/{id}")
async def delete_post(id: int):
    rpta = nuevo_post.delete_post(id)
    return rpta
