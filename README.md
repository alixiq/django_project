# Django Project: API CRDU
### This is a DailyTask project built with Django and Django REST framework, HTTP requests enter the system through Apache or Nginx servers. These requests are then handled by a WSGI server like Gunicorn, which manages asynchronous request handling. After passing through the WSGI server, requests are intercepted by Django's middleware, performing various tasks like authentication or modifying requests. The URL dispatcher then directs requests to specific views, where database queries are made to generate the appropriate response. Finally, the response travels back through the middleware, WSGI server, and server software, reaching the client. This entire process ensures efficient request handling and response generation in the DailyTask application.
### Python version = 3.9.0
### Upgrading pip:
#### python -m pip install --upgrade pip
### Installing requirements.txt file
#### pip install -r requirements.txt