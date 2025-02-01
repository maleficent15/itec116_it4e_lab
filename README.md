# itec116_it4e_lab 

This repository contains all lab activities for the ITEC116 course.

## Lab Activities
- **Lab 1**: 

This project is a simple API built using FastAPI that calculates the factorial of a given number
The API exposes a single endpoint, /factorial/{starting_number} which takes an integer as input and returns the factorial of that number

GET /factorial/{starting_number}
Returns the factorial of starting_number

Install dependencies: pip install -r requirements.txt
Run the server: uvicorn lab1:app --reload
Test the API via: http://127.0.0.1:8000/docs

Technologies Used:
FastAPI
Uvicorn
Pydantic
Python-dotenv

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


- **Lab 2**: 

This project is a simple To-DO List API built using FastAPI, allowing users to manage tasks efficiently through Create, Read, Update, Delete operations

Feeatures are:
CRUD Operations : Create, Read, Update and Delete Task
Validation: Ensures valid task IDs and prevents duplicates.
Structured Responses: Returns {"status": "ok"} for success and detailed error messages for failures
API Documentation: Auto-generated Swagger UI for easy testing.
Error handling: Handles invalid inputs like negative IDs and missing task


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


- **Lab 3**: 

This lab extends FastAPI by integrating external APIs to retrieve and format user posts and comments dynamically.

Features:
-Retrieve Posts by User (detailed_pist]{userID} - fetches all post of a specific user along with their comments.
-Get all Posts (/posts/) - Retrieves all post or a specific post by postId.
-Get all comments (/comments/) - fetches all comments or filters them by postId.
-Formatted Comments (/formatted_comment/{postID}) - presents refineed comment details for a specific post.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


- **Lab 4**: 

This lab builds upon lab2 by introducing API versioning, error handling, and API key authentication using environment variables

Features:
---API Versioning:
apiv1 - initial implementation of t5ask management endponts
apiv2 - enhanced version with http exceptions and API key security
---Error Handling (HTTP Exceptions)
404 Not Found - when accessing, deleting or updating a non-existent task
204 No Content - when no tasks are available
201 Created - when a task is successfully added
204 No content - when a task is successfully updated or deleted
200 OK - for other responses
---API Key Authentication:
uses an .env file to stor3e the API key securely
the API key must be included in requeest headers for access.
.gitignore prevents commiting .env to the repository

