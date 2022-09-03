## Sample tests for demonstration purpose
Writen on python, using Selenium and Robot Framework


### Initialize new venv for project

```python3 -m venv venv```

### Activate venv

```.\venv\Scripts\activate.ps1``` for windows or ```source venv/bin/activate``` for linux

### install required framework

```pip install -r requirements.txt```

### run tests

tests_python.robot - tests with keywords written with python libraries, driver for browser will be downloaded automatically

```robot -d reports tests_robot.robot```

tests_robot.robot - tests with keywords written with robot keywords too. Need to download chromedriver and put into project root

```robot -d reports tests_python.robot```




