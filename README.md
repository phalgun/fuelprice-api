fuelprice-api
=============

An API for the latest fuel prices in India for all the major towns and cities. 
It is a Flask based lean app. 

To run it on your own server, you will need [Python][] with the [Flask][] microframework and [lxml][]. 
Use can use either `easy_install` or `pip` to install the libraries. 

Start the server with : 

    $ python runserver.py

[Python]: http://python.org/
[Flask]: http://flask.pocoo.org/
[lxml]: http://lxml.de/

REST webservice calls
---------------------

- /fuelprice/v1.0/diesel - returns a JSON with diesel prices of all the major towns & cities in India. 
- /fuelprice/v1.0/diesel/cityname - returns a JSON with the diesel price in cityname. 
- /fuelprice/v1.0/petrol/ - returns a JSON with petrol prices of all the major towns & cities in India. 
- /fuelprice/v1.0/petrol/cityname - returns a JSON with the petrol price in cityname. 
- /fuelprice/v1.0/city - returns a JSON with a list of all the supported cities & towns. 

Do holler if you need help in understanding the code or using it. 

--
I <3 scraping. 
