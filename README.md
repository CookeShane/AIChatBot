# AIChatBot

AIChatBot is a chatbot that utilizes OpenAI's API to create embeddings of user questions and answers them from a list of predefined questions and answers. If there is no appropriate response, a customised message is returned instead.


## Table of Contents

- Features
- Installation Requirements
- Installation
- Usage
- Editing the FAQs
- Troubleshooting
- Contact Information


## Features

- **OpenAI Integration**: Uses OpenAI's API for generating embeddings of user questions.
- **Vector Similarity Search**: Employs pgvector and Ivfflat Indexing for efficient and accurate matching of user questions to predefined answers.
- **Django Backend**: Manages the application logic, user interactions, and API endpoints.
- **PostgreSQL Database**: Stores the predefined questions, answers, and user interaction data.
- **Dockerized Setup**: Ensures a consistent and reproducible environment for development, testing, and deployment.


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

To modify or add categories, you will need to edit the `AIChatBot/faq_chatbot/management/commands/populate_db.py` file. After making your changes, populate the database by running the following command:
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