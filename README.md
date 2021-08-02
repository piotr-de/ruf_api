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