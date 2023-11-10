# Electric Vehicle Charger Project

This project is based on two parts: one for collecting and making sense of data,  
this data is collected on Public EV chargers in Sweden using the Nobil.no API  
the other is for running a simple server with REST API and a Sqlite database.

The server can be seen as a simple skeleton for the backend of an eventual  
implementation of an application where users can find private/public EV chargers  
and rent them. It is mainly set up to allow for CRUD operations on the database.

## File structure
### Data collection
There are two notebooks one for downloading the data using the API key: [here](Sharge_Data_Collection/download_API_data.ipynb)  
the other one for understanding and reorganising this data: [here](Sharge_Data_Collection/reorganise_API_data.ipynb)

Other than that there is one Geojson file used to define the bounding box of sweden.  
There is also one json file with example data from the API call. Lastly there is a  
.csv [file](Sharge_Data_Collection/nobil_data_sweden.csv) containing all the data on Sweden from this API after being reorganised.

### Server
The directory [server](/Sharge_Backend/server) contains the logic of the server.  
[models.py](/Sharge_Backend/server/models.py) defines the schemas for the data to be used and stored.  
[__init__.py](/Sharge_Backend/server/__init__.py) defines the app and the database and their relation.  
[app.py](/Sharge_Backend/server/app.py) imports the app from init and runs it.  
[routes.py](/Sharge_Backend/server/routes.py) defines the API, methods and returns to be made when the API is called.  

The database the server updates is located [here](/Sharge_Backend/instance/db.sqlite3).  
There is also a script [populate_db.py](/Sharge_Backend/populate_db.py) to populate the database with spoofed data.

Lastly there are two http files, that can send requests to the servers. So that it is  
easy to try out the functions of the server and that it returns what it should.  
One for testing the [users](/Sharge_Backend/test_users.http)
and one for testing the [chargers](/Sharge_Backend/test_chargers.http)

## How to run
Clone the project.

```bash
  git clone https://github.com/AdrianHRedhe/EV_Charger_Project.git
```

Go to the project directory

```bash
  cd EV_Charger_Project
```

Install the required dependencies

```bash
  pip install -r requirements.txt
```

### For running data collection
After following the general steps [above](#how-to-run) 

Go to the Data Collection directory

```bash
  cd Sharge_Data_Collection
```

Create a .env file for containing the API key. More info on why [here](#info-on-the-api-used-to-get-the-data)

```bash
  touch .env
```

Add YOUR API key to the .env file with the same variable name.

```bash
  echo "API_KEY = 'YOUR API KEY'" >> .env2
```

i.e. "API_KEY = '34095873498577345987'"

Then you can just run the notebooks as usual.

### For running the server
After following the general steps [above](#how-to-run)

Go to the Server directory

```bash
  cd Sharge_Backend/server
```

Start up the server

```bash
  flask run
```

Once the server is up and running you can make API calls to the server.  
We recommend using the .http files for testing the CRUD operations as well  
as testing data persistance between server runs.

### Info on the API used to get the data
This project uses an API to nobil.no to collect data on electric vehicle chargers  
the API is free to use, you just have to apply [here](https://info.nobil.no/api) to get the key.

We use a .env file to ensure that the API key does not go public. But if you are  
interested in what data is available you can use this client test of the api [here](https://www.nobil.no/api/client/search_apiVer3.php).