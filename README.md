# BAKERY MANAGEMENT SYSTEM

## Introduction
 Welcome to the Sweet Delights Bakery System User's Guide. This document provides an overview of the features and use cases of our Python-based system designed to streamline operations and enhance customer engagement for our local bakery.

This application basically deals with the sales and product management of a bakery based on the Django framework.

![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/login.png)

![alt_text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/homesales.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/homeproduct.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/addsupplier.png)
![alt_text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/addsupplyorder.png)
![alt_text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/confirmorder.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/createorder.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/createproduct.png)
![alt_text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/findcustomer.png)
![alt_text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/homdeliveryorders.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/invoiceview.png)
![ale text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/invoiceprintview.png)
![ale text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/orderdetails.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/vieworders.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/viewsupplyorder.png)
![alt text](https://github.com/dchuai/Bakery-Management-System-Using-Django-dbSQLite3-/blob/main/UIUX/dashboard.png)

---------------------------
# Our Bakery Management System Demonstration Video:
<video src="Sweet%20Delight%20Bakery%20System_demonstration%20video-1.mp4" controls title="System Demonstation Video"></video>

## M08 Final Project Submission 

## Group2: Team Members list: 
1. Karima Kouadri Boudjelthia, 
2. Micheal Mekoya, 
3. Dim Huai

## Group2 Team Members

## Project Manager: Karima Kouadri Boudjelthia
#- Responsible for overall project coordination, goal setting, and ensuring project milestones are achieved.

## Front-End Developer: Micheal Mekoy
#- Designs the user interface and implements front-end features for a seamless customer experience.

## Back-End Developer and Designer: Dim Huai
#- Manages server-side logic, database management, and focuses on creating visual elements.

## Quality Assurance Tester: Karima Kouadri Boudjelthia
#- Ensures the system functions correctly, conducts testing, and identifies and resolves any bugs or issues.

## Documentation Specialist: Dim Huai
#- Keeps project documentation up-to-date, including the proposal, class diagram, and reports.


## PRE-REQUISITES
1. Python 2.7 or Python 3.12.0
2. Django
3. virtual env

## Sweet Delights Bakery System User's Guide: HOW TO USE APPLICATION?

1. Open the link and enter username and password
### Web Login
	Username : aparna.d	Password : welcome@1
### Django Admin
	Username : admin1 password : admin1

2. The navigation bar at the top has all the functionalities required

### Use Cases
### Take New Order
This application allows user to take order of the customer visiting.Follow the following steps to take New Order

1. Enter a 10 digit phone number of the customer to search if the customer with this phone number exists.
2. If customer does not exist, enter customer details:
- First Name	
- Last Name	
- Residential Address
3. Select the product using the drop-down menu, add quantity and click on 'Add' to add the product.
4. To delete the wrong item, just click on 'Delete'.
5. Select if the order is 'Home Delivery' or 'Store Pick-Up'.
6. Enter Home Delivery details:
		- Delivery address
		- Select Delivery Date and Time
		- Additional Delivery instructions('leave at doorstep',etc)
7. Confirm the Order details by adding
		- any extra charges
		- select delivery mode
		- select payment mode
		- Any order instructions like 'Write happy birthday alice' etc
8. Click on Confirm to generate receipt
9. Click on 'Print' to print the receipt
10.Click 'Back' to return to the Home page.

#### CASES OF ERROR :
	If the order is not taken successfully, check if the order is visible in 'View Orders'.
	If not, get back and start from the beginning by searching for customers.
	If yes, delete the order in 'View Order' and take a new order


### View Orders
It views all the orders taken till date and bills of each order.


### View Home Delivery Orders
To view all the orders for home-delivery

### View Sales Report
The dashboard shows number of orders taken TODAY and number of customers added TODAY.
The Pie-Chart gives information about the total units sold of the top 5 most sold Product.
### Add Product
To add an item into the menu, user can add the product into the already existing menu
1. Enter the product name and it's price.
2. Click on add product to add this product in Menu
### Add Supplier
To add details about the new Supplier from whom the user gets ingredients for her shop from.
	1. Enter Supplier's details
		- Company Name
		- Contact Number
		- Office Address
	2. Click on Add Supplier to successfully add  supplier.
### Add Supply Order details
To enter details of the new supply order given to the company. The user can enter the invoice number of the receipt that they got from the supplier after placing order, the total amount that was given to the supplier and the date at which the order is given.The details will be added into pending order by default.

### View Supply Orders
The user can keep track of the orders that they have placed to the suppliers. All the order details added comes in the 'Pending Order' table. To change its status to 'Received', Click on 'Update'. The user will be redirected to a page to add a date of receiving. Submit form to change the status.

*In case of any issue, the user can view the database in 'admin' login in the database.

## Conclusion
#Thank you for using the Sweet Delights Bakery System. We hope this user's guide helps you navigate and utilize the various features of our system effectively.
