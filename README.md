# Company Manager

Program to manage your company orders. 

## About

Part of github portfolio to show current skills as Process Improvement Specialist.

Project uses sqlite DataBase, which scheme is published on
[dbdesigner.net](https://dbdesigner.page.link/KBXNfS5kDVTwjB6R6).


## Technology

Project is fully build with python and its open source libraries.
To manage DataBase module sqlalchemy has been used.
To build GUI PySide2 has been used, with Qt Designer to project it.

### PySide2 namespace
Objects names refer to their text and type of widget, by use of below shortcuts:
<br />IW - Input Widget
<br />DW - Display Widget
<br />CT - Container
<br />B - Buttons


## Other files
1. Countries_table.csv - Configuration file with ISO 3166 country codes. Used to populate DB for the first time with countries names and codes
2. my_db.db - Database created with ORM sqlalchemy. Populated with Countries_table.csv on initial.

