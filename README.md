Django REST API Project
This project implements a Django REST API for storing paragraphs of text and searching for specific words within them. Users can register, log in, and store paragraphs along with word-to-paragraph mappings in a PostgreSQL database.

Features
User registration and authentication
Storing paragraphs of text
Searching for words within paragraphs
Tech Stack
Django
Django Rest Framework
PostgreSQL
Docker
docker-compose
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <project_directory>
Install Docker and docker-compose:

Docker Installation
docker-compose Installation
Build and start Docker containers:

css
Copy code
docker-compose up --build
Access the Django application at http://localhost:8000.

API Endpoints
User Registration:

POST /api/register/: Register a new user.
Paragraph Creation:

POST /api/paragraphs/: Create a new paragraph (authentication required).
Paragraph Search:

GET /api/paragraphs/search/?word=<word>: Search for paragraphs containing a specific word (authentication required).
Authentication
JWT authentication is used for all API endpoints.
Obtain a JWT token by sending a POST request to /api/token/.
Include the token in the Authorization header for subsequent requests.
Directory Structure
graphql
Copy code
myproject/
│
├── myapp/             # Django app
│   ├── migrations/    # Database migrations
│   ├── models.py      # Define models including Custom User Model
│   ├── serializers.py # Serializers for API endpoints
│   ├── views.py       # Define API views
│   └── ...
│
├── myproject/          # Django project settings
│   ├── settings.py     # Project settings including PostgreSQL configuration
│   ├── urls.py         # URL routing
│   └── ...
│
├── db/                 # PostgreSQL database files (volume for Docker)
│
├── Dockerfile          # Dockerfile for Django application
├── docker-compose.yml  # Docker Compose configuration
└── README.md           # Usage instructions


