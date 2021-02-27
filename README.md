# A REST API of products with Flask
### This api has been developed with the aim of showing how Flask works and how a simple api works. This api consists of managing products, you can create, read, update and delete a product, that's right, a CRUD!
### The database engine used for this project is SQLite
### It is not necessary to create the database as the API automatically creates the database when it is first started. The database is created in the same directory as the project, it is empty since it is created from 0. It is necessary to add products to be able to work with them, let's see how it is done :
### **Requierements**
* `pip install pipenv`
* [Python](https://www.python.org/)
* [SQLite](https://www.sqlite.org/index.html)
### **Setting up the environment**
#### This project uses `pipenv`, which allows you to automatically create and manage a virtual environment for different projects, as well as add / remove packages from your Pipfile as you install / uninstall packages.
1. To make the requests it is necessary to use an API client such as Insomnia, here is the link to download it: [Insomnia](https://insomnia.rest/)
2. To run the virtual environment of the project, go to your directory and run this command in a terminal: `pipenv shell`
3. Now you need to install some packages to be able to work with the api without problems, to do this, execute this command in the terminal: `pipenv install -r requirements.txt`. If you want to see the packages you just installed, visit the `Pipfile` file
4. We are almost there! Just start the server and the magic begins! To start the server, go to the project directory, open the terminal and run this command: `python app.py`
5. To verify that the server is working without any problem, access from your browser or from the API client to this address: `http://127.0.0.1:5000/`
### **Make requests**
#### **Add product `http://127.0.0.1:5000/products` with POST method**
```
{
    "name": "example",
    "description": "example",
    "price": 100,
    "quantity": 100
}
```
#### **Get all products `http://127.0.0.1:5000/products` with GET method**
```
[
  {
    "description": "Sturdy pencils",
    "id": 1,
    "name": "Pen",
    "price": 1.5,
    "quantity": 252
  },
  {
    "description": "Gaming keyboards",
    "id": 2,
    "name": "Keyboard",
    "price": 70,
    "quantity": 500
  }
]
```
#### **Get product by its ID `http://127.0.0.1:5000/products/id` with GET method**
```
{
    "description": "Sturdy pencils",
    "id": 1,
    "name": "Pen",
    "price": 1.5,
    "quantity": 252
  }
```
#### **Update product `http://127.0.0.1:5000/products/id` with PUT method**
```
{
    "name": "Pen",
    "description": "Sturdy pencils",
    "price": 1.5,
    "quantity": 350
  }
```
#### **Delete product `http://127.0.0.1:5000/products/id` with DELETE method**

```
{
    "message": "product deleted"
}
```

