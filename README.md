# FastAPI MongoDB Forms API

This project is a FastAPI application that allows users to submit form data, which is then stored in a MongoDB Atlas database. The API supports full CRUD operations (Create, Read, Update, Delete) and is designed to be deployed on Render with automatic deployments from GitHub.

## Features

- FastAPI for creating the API endpoints.
- MongoDB Atlas for storing form data.
- Motor for asynchronous MongoDB operations.
- Pydantic for data validation.
- Environment variable management for sensitive data.

## Project Structure

- typeform-backend/
- │
- ├── app/
- │ ├── init.py
- │ ├── main.py
- │ ├── models.py
- │ ├── database.py
- │ └── routes/
- │ └── form.py
- ├── .env
- ├── .gitignore
- ├── requirements.txt
- └── README.md


## Prerequisites

- Python 3.7+
- MongoDB Atlas account

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/typeform-backend.git
   cd typeform-backend

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate` 

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt

4. **Set up environment variables:**

   - Create a .env file in the root directory of your project and add your MongoDB connection string:
  
     ```sh
     MONGO_DETAILS=mongodb+srv://<username>:<password>@<cluster-address>/typeform?retryWrites=true&w=majority
   - **Note**: Replace `<username>`, `<password>`, and `<cluster-address>` with your actual MongoDB Atlas credentials.

5. **Run the application:**

      ```sh
      uvicorn app.main:app --reload

## Usage

You can use Postman or any other API client to interact with the API. Below are the endpoints available:

### Create a Form (POST `/api/form`)

- **URL**: `http://localhost:8000/api/form`
- **Method**: POST
- **Headers**: `Content-Type: application/json`
- **Body**: (JSON)

  ```json
  {
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com",
      "country": "USA",
      "phone_number": "+1234567890",
      "languages": ["Python", "JavaScript"],
      "experience_level": "Intermediate",
      "compensation": "$50,000 - $80,000",
      "certifying_statement": "I accept",
      "linkedin_url": "https://www.linkedin.com/in/johndoe"
  }


### Retrieve All Forms (GET `/api/forms`)
- **URL**: `http://localhost:8000/api/forms`
- **Method**: GET

### Retrieve a Single Form (GET `/api/form/{id}`)
- **URL**: `http://localhost:8000/api/form/{id}`
- **Method**: GET

### Update a Form (PUT `/api/form/{id}`)
- **URL**: `http://localhost:8000/api/form/{id}`
- **Method**: PUT
- **Headers**: `Content-Type: application/json`
- **Body**: (JSON)
  ```json
  {
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane.doe@example.com",
      "country": "Canada",
      "phone_number": "+9876543210",
      "languages": ["Rust", "C++"],
      "experience_level": "Advanced",
      "compensation": "$80,000 - $120,000",
      "certifying_statement": "I accept",
      "linkedin_url": "https://www.linkedin.com/in/janedoe"
  }

### Delete a Form (DELETE `/api/form/{id}`)

- **URL**: `http://localhost:8000/api/form/{id}`
- **Method**: DELETE

### Troubleshooting

- Ensure your MongoDB connection string is correct.
- Verify that your MongoDB Atlas cluster is accessible and IP whitelisted.
- Check the logs for any deployment issues.


### Live Demo Can be Accessed Through

```sh
https://typeform-backend.onrender.com
