# AIChatBot

AIChatBot is a Python & Django based chatbot that utilises OpenAI's API to create embeddings of user questions and answers them from a list of predefined questions and answers. If there is no appropriate response, a customised message is returned instead. The chatbot is (almost) contained inside a single Django app, and therefore can easily be integrated into any other Django project.


## Table of Contents

- Features
- Installation Requirements
- Installation
- Usage
- Editing the FAQs
- Troubleshooting
- Contact Information


## Features

- **Django Application**: This project is Django based, which manages the application logic, user interactions, and API endpoints. Please note, `DEBUG = TRUE` has been left for simplicity.
- **Chatbot Containment**: The chatbot is contained in a single Django app, allowing for easy integration with other Django projects.
- **OpenAI Integration**: Uses OpenAI's API for generating embeddings of user questions.
- **PostgreSQL Database**: Stores the predefined questions, answers, and user interaction data. The database is run through a Docker container. The image used is the `ankane/pgvector` image.
- **Vector Similarity Search**: Employs pgvector and Ivfflat Indexing for efficient and accurate matching of user questions to predefined answers.
- **Dockerized Setup**: Ensures a consistent and reproducible environment for development, testing, and deployment. A Dockerfile is provided to create an image of the Django application, while a docker-compose.yml file is provided for the configuration of the multi-container complete application.
- **Maintainability**: This project was designed for ease of maintenance and to be easily extenisble. For example, what to add a different API for get embeddings, simply add a new class with the Python code to `faq_chatbot/nlp.py`. Have new questions and answers, add them to the `FAQs` folder.


## Installation Requirements

- Docker and Docker Compose
- Git


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CookeShane/AIChatBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AIChatBot
    ```
3. Create `.env` file with environment variables (same directory level as the docker-compose.yml):
    ```plaintext
    POSTGRES_NAME=<database name>
    POSTGRES_USER=<user name>
    POSTGRES_PASSWORD=<user password>
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432

    OPENAI_API_KEY=<insert your openai-api-key here>
    ```
4. Build and start the Docker container:
    ```bash
    docker compose build
    docker compose up
    ```


## Usage

Once the Docker container has completed the startup, follow the next steps (The container can take a while to build and start).
1. Go to the browser and enter the following url:
    ```plaintext
    http://127.0.0.1:8000/
    ```
2. Interact with the chatbot through the provided interface.


## Editing the FAQs

The FAQs are sourced from the FunderPro.com website and stored in the `AIChatBot/FAQs` directory. They are categorized into three subcategories: 'General Queries', 'The Challenge', and 'The Funded Account'. Each question is stored in a separate file with the following format:

- **File Name**: `<the question>.txt`
- **File Content**:
  - **First Line**: `<the question>`
  - **Subsequent Lines**: `<the answer>`

To modify or add categories, you will need to edit the `AIChatBot/faq_chatbot/management/commands/populate_db.py` file. After making your changes, populate the database by running the command below. Please note, this command clears the database entirely and then repopulates it when its run. It is included in the `Dockerfile` and `docker-compose.yml` by default but can be taken out for quicker container start times.
```bash
python manage.py populate_db
```

## Troubleshooting

### Common Issues

- **Docker Not Starting**: Ensure Docker is running and you have the necessary permissions.
- **.env File Encoding**: Make sure the encoding of the `.env` is UTF-8.
- **Environment Variables**: Double-check your `.env` file for any typos or missing values.
- **Port Conflicts**: Make sure the ports used by Docker are not occupied by other services.



## Contact Information:

For any questions or suggestions, please contact me through my details below:
- Email: shanephcooke@gmail.com
- LinkedIn: https://www.linkedin.com/in/cooke-shane/