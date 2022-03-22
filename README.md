## How to use

1. git clone https://github.com/oguilhermefigueiredo/airline-django && cd airline-django
1. docker build -t airline-django .
1. docker run -dp 8000:8000 --rm airline-django

### Accessing the routes

http://localhost:8000/flights
http://localhost:8000/users
http://localhost:8000/admin

You can manage flights, users and airports using the admin page. The login
access is just *admin* followed by the password being *admin", too.

If you try to access the same application in another browser, another session 
will be started, using tokens to maintain the site/forms reliable.

Users can create their accounts and login successfully, through the login page,
although they're not able to do it without having an account created using the 
admin page.
