# About the project
This mini-project outlines the possibilities offered by Flask in terms of quick deployment of a streamlined API.

## Built with
- Python
- Flask

# Getting started

## Prerequisites
- Python 3.6+
- pip
- Flask
- requests
- pyyaml
- flask_http_auth
- translate

## Installation

1. To launch the Flask development server and launch the API locally, start by cloning the repo:

    `git clone git@github.com:piotr-de/ruf_api.git`


2. Install all the libraries and dependencies from the requirements.txt file located in your local repo:

    ```
    cd ruf_api
    pip install -r requirements.txt
    ```


3. Set the RUF_API_TOKEN environment variable of your choice - anyone wishing to make calls to the API will need to provide it as a bearer token:

    - Windows:
        `set RUF_API_TOKEN=<your_chosen_token>`
    - Linux:
        `$ RUF_API_TOKEN=<your_chosen_token>`
    - WSL2 with Ubuntu:
        `export RUF_API_TOKEN=<your_chosen_token>`


4. The API is ready to launch as a local development server:

    `python app.py`

The API should now be running locally on `http://localhost:8080/`

# Usage

In order to access the full functionality of the API, you will require an API client e.g., [Postman](https://www.postman.com), which you can download for free. This will enable you to supply the valid authorization bearer token. Without one, you can still view the OpenAPI schema - simply type `http://localhost:8080/` into your browser address bar.

## Endpoints

    - `/`
        Displays the OpenAPI schema

    - `/status`
        Displays a JSON object containing the fact load status as well as the number of facts (unique and overall) already loaded

    - `/facts`
        Displays a JSON array of all the fact ids already loaded

    - `/facts/<fact_id>`
        Displays a JSON object representing a specific fact: its content, source etc.
        You can pass an additonal parameter `lang` as a query string, containing a ISO 639-1 language code e.g., `?lang=de`, which will return the fact translated into your language of choice.

