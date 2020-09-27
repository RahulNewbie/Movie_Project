Welcome to movie project

Below are the points to install and run the application.
Code is checked with pylint for probable warnings

***Install Dependency***

pip3 install -r requirements.txt

***Run the Application***

Run the application using the following statement

python3 application.py

***Usage***

Open a browser and use the following in the address bar. 

http://localhost:8000/movies/

Here localhost:Port Number/movies/ is the endpoint for user

***Using curl***

Use the following curl command to get the movie data

curl -H "Content-Type: application/json" -X GET http://localhost:8000/movies/

