# Blog API

This project implements a Blog API using FastAPI. It provides endpoints for managing blog posts and user authentication.

## Features

- Create, read, update, and delete blog posts.
- Get a list of all blog posts or retrieve a specific post by ID.
- Create and retrieve user information.
- User authentication using JSON Web Tokens (JWT).

## Installation

1. Clone the repository:

   git clone https://github.com/Atul245/Blog-Api.git
   
2. Change to the project directory:

   cd https://github.com/Atul245/Blog-Api.git
   
3. Install the required dependencies using pip:
    
    pip install -r requirements.txt

## Usage
1. Run the FastAPI server:
 
   uvicorn main:app --reload
  
2. Access the API documentation in your browser at http://localhost:8000/docs.
3. Use the available endpoints to interact with the API.

## API Endpoints

### Blogs

  - GET /blogs: Get a list of all blog posts.
  - GET /blogs/{blog_id}: Get a specific blog post by ID.
  - POST /blogs: Create a new blog post.
  - PUT /blogs/{blog_id}: Update an existing blog post.
  - DELETE /blogs/{blog_id}: Delete a blog post.
  
### Users

  - GET /users: Get a list of all users.
  - GET /users/{user_id}: Get user information by ID.
  - POST /users: Create a new user.
  
### Authentication

  - POST /login: User login endpoint. Returns a JWT token upon successful authentication.
