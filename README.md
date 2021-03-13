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

To build GUI Qt Designer was used as part of PySide2 library. 


## OverView

###First launch

On the first launch of the program, user would be ask to setup company account.
![add_customer](/readme_screen_shoots/add_customer.png)

After which welcome window will appear, which will appear within each launch of the program after company account is created.
![welcome_window](/readme_screen_shoots/welcome_window.png)


###Main window

Main window contains buttons which open appropriate modules of program.

![main_window](/readme_screen_shoots/main_window.png)


####Add Customer and Edit Customer

Those modules allows to add customers to company database and edit them. 
If user won't provide all necessary data, appropriate widgets would have red border to inform that there is missing required data.
![add_customer](/readme_screen_shoots/add_customer.png)

####My Products

Module used to manage information about products that company has in sell. 
![my_products](/readme_screen_shoots/my_products.png)

####Price-lists

Modules used to create and manage Price-lists for each customer separately. 
![price_lists](/readme_screen_shoots/price_list.png)


## Technologies

Project is fully build with python (ver 3.8) and its open source libraries:

- **sqlalchemy==1.3.23** - to manage DataBase
- **PySide2==5.15.1** - to build GUI
- **pandas==1.1.2** - to deal with .csv files

### PySide2 namespace
Objects names refer to their text and type of widget, by use of below shortcuts:
<br />IW - Input Widget
<br />IV - Item View
<br />DW - Display Widget
<br />CT - Container
<br />B - Buttons


## Other files
1. Countries_table.csv - Configuration file with ISO 3166 country codes. Used to populate DB for the first time with countries names and codes
2. my_db.db - Database created with ORM sqlalchemy. Populated with Countries_table.csv on initial.

## Project status
Project under development.