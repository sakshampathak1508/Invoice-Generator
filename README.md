# Invoice-Generator
Task:

Develop an application that generates invoices in fairly simple format. Format
for reference can be found at the end of this task. You can make a model for
items and other details as per your convenience. The application must facilitate
the following API(s):
1. GET: get the list of available items with details such as (name, price,
description).
2. POST: to send the list of items to buy with corresponding quantities.
3. PUT: to update the list of items in the purchase list.
4. GET: get the invoice for the purchase in pdf format as per the above
format but with all the necessary details filled dynamically.
Configure and deploy the application mentioned in first point to any open and
free hosting service like Heroku/PythonAnywhere. Add the link to the project.


The admin panel of this app can be accessed by:

https://invoice-disecto.herokuapp.com/admin/
username: 123456
password: 123456

1. TO GET THE LIST OF ALL AVAILABLE ITEMS
		 		 
		Api Path :- https://invoice-disecto.herokuapp.com/all-items/
		its a simple get request so you get all the available items

2. TO POST THE ITEM LIST OF SEVERAL ITEMS FOR A PARTICUALR ORDER
		
			
		Api Path :- https://invoice-disecto.herokuapp.com/item-list/
		This post request takes two things as a request data one of which is the list of items id and their quantities
		and the order name.
		
		eg: in json
			{
				"item_list": [{"item": 1,"quantity": 2},{"item": 2,"quantity": 4}],
				"name": "arun"
			}
			
3. TO UPDATE THE ITEM LIST IN AN ORDER BEFORE PLACING IT A SIMPLE PUT REQUEST

		Api Path :- https://invoice-disecto.herokuapp.com/item-list/
		This put request simply edits the list items accordingly
		
		eg: in json it takes lid as required field
			{
				"lid": 1,
				"quantity": 5
			}
			
4. GET INVOICE PDF
		
		Api path:- https://invoice-disecto.herokuapp.com/invoice-pdf/?oid=2
		
		it takes a parameter at the end as an order id as oid to generate an invoice of that particular order
		
