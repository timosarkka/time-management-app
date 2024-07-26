# Time Management and Reporting System

## Overview
This repository contains two main applications:
* Time Management App: Used by consultants to log their working hours.
* Reporting Software App: Generates reports of logged hours and stores them in Azure Blob Storage.

Note! You'll need an access to a PostgreSQL server and database in order to input data.

## Time Management App

###  Installation
Clone the repository:


```
git clone https://github.com/timosarkka/time-management-app.git
cd time-management-app
```

Install the required dependencies:

```
pip install -r requirements.txt
```

### Configuration

Note! You'll need an access to a PostgreSQL server and database in order to input data

Configure the database connection settings e.g. using a 'database.ini'-file or similar and add following parameters:
```
    'host': 'your_db_host',
    'database': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'port': 'your_db_port'
```

### Database Operations

The Time Management App performs the following operations:

* Fetch all working hours
* Fetch working hours by ID
* Create a new working hour entry
* Update an existing working hour entry
* Delete a working hour entry

### API Endpoints

The following endpoints are provided by the Flask API:

* GET /: Check if the API is running.
* GET /workinghours: Retrieve all working hours.
* GET /workinghours/<int:id>: Retrieve working hours by ID.
* POST /workinghours: Create a new working hour entry.
* PUT /workinghours/<int:id>: Update an existing working hour entry.
* DELETE /workinghours/<int:id>: Delete a working hour entry.

### Usage

You can use the time management e.g. with Postman or use curl:

Some example use cases:

Fetch all working hours
```
curl -X GET http://localhost:5000/workinghours
```

Fetch working hours by ID
```
curl -X GET http://localhost:5000/workinghours/1
```

Create a new working hour entry
```
curl -X POST http://localhost:5000/workinghours -H "Content-Type: application/json" -d '{
    "customerID": 1,
    "employeeID": 1,
    "startTime": "2024-05-05T08:00:00",
    "endTime": "2024-05-05T17:00:00",
    "lunchBreak": true
}'
```

Update an existing working hour entry
```
curl -X PUT http://localhost:5000/workinghours/1 -H "Content-Type: application/json" -d '{
    "customerID": 1,
    "employeeID": 1,
    "startTime": "2024-05-05T09:00:00",
    "endTime": "2024-05-05T18:00:00",
    "lunchBreak": false
}'
```

Delete a working hour entry
```
curl -X DELETE http://localhost:5000/workinghours/1
```

## Reporting Software App

### Installation

If you've already cloned the repo like instructed above, you just need to install the required dependencies:
```
pip install -r requirements.txt
```

### Configuration

Configure the database connection settings in config.py as described in the Time Management App section.

Set up Azure Blob Storage connection by configuring the environment variable azure_storage_pass with your Azure Storage connection string.

###  Report Generation

The Reporting Software App generates reports for the specified date and uploads them to Azure Blob Storage. It performs the following operations:

* Calculate working hours by consultant and customer
* Calculate average working hours by consultant
* Calculate cumulative working hours by customer

### API Endpoint
The following endpoint is provided by the Flask API:

GET /report: Generate a report and upload it to Azure Blob Storage.

### Example usage

Just run the app and it will generate and upload the report based on the data found from the server's database.
