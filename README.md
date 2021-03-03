# Company Manager

Program to manage your company orders. 

## Table of contents
* [About](#About)
* [Technologies](#technologies)
* [Other files](#other-files)
* [Project status](#project-status)

## About

Part of github portfolio to show current skills as Process Improvement Specialist.

Project uses sqlite DataBase, which scheme is published on
[dbdesigner.net](https://dbdesigner.page.link/KBXNfS5kDVTwjB6R6).


## Technologies

Project is fully build with python and its open source libraries:
* sqlalchemy - to manage DataBase
* PySide2 with Qt Designer - to build GUI
* pandas - to deal with .csv files

### PySide2 namespace
Objects names refer to their text and type of widget, by use of below shortcuts:
<br />IW - Input Widget
<br />DW - Display Widget
<br />CT - Container
<br />B - Buttons


## Other files
1. Countries_table.csv - Configuration file with ISO 3166 country codes. Used to populate DB for the first time with countries names and codes
2. my_db.db - Database created with ORM sqlalchemy. Populated with Countries_table.csv on initial.

## Project status
Project under development.