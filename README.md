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

### First launch

On the first launch of the program, user will be asked to setup company account.
![add_customer](/readme_screen_shoots/add_supplier.png)

When company account is created, user will be welcomed with welcome window for each run of program.
![welcome_window](/readme_screen_shoots/welcome_window.png)


### Main window

Main window contains buttons which open appropriate modules of program.

![main_window](/readme_screen_shoots/main_window.png)


#### Add and Edit Customer

Those modules allows to add customers to company database and edit them. 
![add_customer](/readme_screen_shoots/edit_customer.png)

#### My Products

Module used to manage information about products that company has in sell. 
![my_products](/readme_screen_shoots/my_products.png)

#### Price-lists

Module used to create and manage Price-lists for each customer separately. 
![price_lists](/readme_screen_shoots/price_list.png)

#### Add and Edit new Order

Module used to create orders and to edit them for each customer separately. 
![add_n_edit_order](/readme_screen_shoots/add_n_edit_order.png)

### Show order and order details

Module used to browse orders and edit details.

![show_order](/readme_screen_shoots/show_orders.png)
![show_order_details](/readme_screen_shoots/show_order_details.png)


## Technologies

Project is fully build with python (ver 3.8) and its open source libraries:

- **sqlalchemy==1.3.23** - to manage DataBase
- **PySide2==5.15.1** - to build GUI
- **pandas==1.1.2** - to deal with .csv files
- **xlwings==0.23.0** - create xlsx files and save them as pdf from it

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