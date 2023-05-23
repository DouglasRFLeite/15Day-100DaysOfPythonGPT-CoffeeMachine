# 15Day-100DaysOfPythonGPT-CoffeeMachine

Day 15 of the [100 Days of Code with Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) from Udemy.

## What is 100DaysOfPythonGPT?

100 Days of Python is a Python Bootcamp from Udemy that provides 100 days of Python pratical content with lessons and projects. The GPT part is something I'm adding to the course and infers that I shall use ChatGPT's engine and/or API in some way on each and every one of those 100 projects. Furthermore, I shall also practice using PyTest to test these projects and applications at least in some level.

## CoffeeMachine

Coffee Machine is the fifteenth project of the fifteenth Day of the bootcamp. Its purpise is to be one more project to enhance skills and, in the courses sequence, it's supposed to be the first project on an actual Python development enviroment. I have done that with VSCode ever since I began.

The project consists of a coffee machine that holds resources, money and a menu, the user may ask for the coffees and pay with coins, recieving change when needed.

It did not seem feasible to use ChatGPT's API in this project but it is pretty well tested, with a test file for every functionality.

## Project Structure

 - [src/](src/) - There is only the file `coffee_machine.py` with the functions, and the file `manu.py` with the necessary data of each coffee.
 - [test/](test/) - There is a test for each important functionality of the coffee machine: `test_report.py`, `test_resources.py`, `test_payment.py` and `test_make_coffee.py`.
