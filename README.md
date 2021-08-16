# Flask template for Craft Exercise

# Overview

## Local Development Instructions
* Clone this repository and navigate to the project.
* Set up Virtual Environment   
* Install dependencies from requirements.txt file
    ```pip install -r requirements.txt```   
* Run ```python app.py``` to spin up application.
* Run ```pytest tests/test.py ``` to run tests.
* The template repo has 2 endpoints and a 404 handler.
  -  192.168.0.118:5000/healthcheck
    ``` json
    {
      "status": "healthy"
    }
    ```
  -  192.168.0.118:5000/details
    ``` json
    {
      "api_version": "0.1",
      "app": "Craft Exercise",
      "env": "dev"
    }
    ```
  -  192.168.0.118:5000/xyz
    ``` json
    {
      "api_version": "0.1",
      "app": "Craft Exercise",
      "msg": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }
    ```
  
  
###Docker Instructions

* ```docker image build -t <image-name> .```
* ```docker run -p 5000:5000 -d <image-name>```