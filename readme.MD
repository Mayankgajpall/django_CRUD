This is a simple project that demonstrate CRUD(Create,Read,Update,Delete) operations using REST API in django.
#### Github actions workflow can also be seen for pushing of docker image to docker hub with each merge.

To run this project:
1) Install dependencies in requirements file.
2) Create and .env file similar to .env_example file.
3) Execute python manage.py runserver command to run the application

Docker commands to run this project:
1) docker build --build-arg SECRET_KEY=<your_secret_key> --build-arg DEBUG=<Debug_flag_True/False> -t <your_tag> .
2) docker run -d -p 8000:8000 <image_name>

Enpoints for the REST API are:
1) /books/ (GET): Provides details of all the books available in the DB
2) /books/ (POST): Insert data in the DB, if the provided json data is valid.
2) /books/<book_id> (GET,PUT,DELETE): Retrieve, update and delete respectively by providing id of the data.

Valid input Json data:

{
    "name": "Mucho Gusto",
    "author": "Hernandez",
    "description": "El muher mucho gusto",
    "language": "Spanish",
    "price": "7$"
}

#### This project is a part of demonstrating implementation of kubernetes. This project will be considered as a microservice and will be deployed using kubernetes.
