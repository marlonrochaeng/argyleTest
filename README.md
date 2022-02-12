# Automation for Argyle

This repository was created to study automation with Python and Selenium

## Requirements

Python 3

Docker

Some updated browser (Chrome, Firefox, etc)

The correspondent driver of your browser (change the driver path in conftest if you need)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage
To run all tests, go to the root folder of the project and execute the command
```bash
pytest --browser chrome
```

To run some specific test, go to the root folder of the project and execute the command
```bash
pytest --browser chrome tests/path_to_test.py
```
To generate the HTML report, go to the root folder of the project and execute the command
```bash
pytest --browser chrome --html=report.html
```

The result will look like:
![alt text](https://github.com/marlonrochaeng/pythonAutomationPratice/blob/master/Report%20Example.png?raw=true)

If you want a Junit XML report, go to the root folder of the project and execute the command
```bash
pytest --browser chrome --junitxml=report.xml
```

If you want to run everything in a docker image, run:
```bash
docker build .
```

Then run:
```bash
docker run {returned_image_hash}
```

### Improvements
 - Use parametrize to improve tests data entry
 - Use docstring to improve documentation 
 - Use allure to serve reports