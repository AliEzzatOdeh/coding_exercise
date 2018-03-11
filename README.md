My example requires Python3.6, I assumed tha the customer will search for a hotel offer, by the city, start date and end date.
The application handles the count for the days of stay, the application should display a list of offers with links to Expedia 
website to book the hotel, I have choosen to show for each offer an image along with the name, the price per night, 
total price, hotel star rating and a booking link.

In order to run the example follow instructions below, I advice using virtualenv for running the example:
  1)In case you selected to use virtualenv, create a virtual directory with the name you want.
  2)Clone my github repository inside the required directory.
  3)Run the command "pip install -r requirments.txt" to install the libraries required for the app.
  4)Run the unit test(s) with the command "python manage.py test" and make sure test passes.
  5)Run the server with the command "python manage.py runserver" and start testing ^_^.
  
ISSUES:
I used date inputs for ease of use for user, but not all browsers support it e.g. "Firefox", so user should handle inserting 
the valid format in case he/she unsupported browser, it should work fine in Chrome.

LIVE EXAMPLE:
This is my first time using Heroku, I found it interesting, here is a live example of the application: 
https://ali-ezzat-coding-example.herokuapp.com/

Travis-ci:
Also it is my first time using , my application builds successfully using it, here is a link: 
https://travis-ci.org/AliEzzatOdeh/coding_exercise
