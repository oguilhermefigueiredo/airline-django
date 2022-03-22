## How to use

1. git clone https://github.com/oguilhermefigueiredo/airline-django && cd airline-django
1. docker build -t airline-django .
1. docker run -dp 8000:8000 --rm airline-django

## Accessing the routes

### Flights

http://localhost:8000/flights

![flights](https://user-images.githubusercontent.com/97318219/159582175-c4d1ecde-774e-4003-a7bb-29247144296f.png)

![passengers](https://user-images.githubusercontent.com/97318219/159582791-488ca9a6-22fe-492f-af8b-981a670aa1fd.png)

### Users

http://localhost:8000/users

![login](https://user-images.githubusercontent.com/97318219/159582384-f1bac281-9f76-4d7b-9e76-7bd0f6a6f46e.png)

![upage](https://user-images.githubusercontent.com/97318219/159582963-2107de10-44da-4a00-ad47-ae4a5fd7de3e.png)

![out](https://user-images.githubusercontent.com/97318219/159582972-b7efdb80-3245-4d41-93e2-71bf81c32ba1.png)

### Admin Page

http://localhost:8000/admin

![admin-page](https://user-images.githubusercontent.com/97318219/159582412-df1afb7a-2076-44fd-93b5-760a68e48fb5.png)

You can manage flights, users and airports using the admin page. The login
access is just *admin* followed by the password being *admin", too.

### Sessions and authentication

![cookies](https://user-images.githubusercontent.com/97318219/159583147-4ee11852-bbfe-4e06-ab6e-0ced7bbb6fc6.png)

If you try to access the same application in another browser, another session 
will be started, using tokens to maintain the site/forms reliable.

Users can create their accounts and login successfully, through the login page,
although they're not able to do it without having an account created using the 
admin page.
