# Learning selenium with Python

## Install the important libraries
- Selenium
- Pytest
- Allure Pytest
- Pytest HTML
- xdist - Run parallel execution
- logging
- openpyxl - read CSV or EXCEL
- Behave
- Faker lib - Fake data generation


``pip install selenium pytest pytest-html allure-pytest``

## How to push to git
1. git add .
2. git commit -m "Message"
3. git push
4. git pull (if you add something on gitlab)

## Install parallel execution
``pip install pytest-xdist``
``pytest -n auto code/.py -s -v``
