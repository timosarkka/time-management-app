# Time Management and Reporting System

## Overview

This repository contains two main applications:
* Time Management App: A very simple app used by consultants to log their working hours.
* Reporting Software App: Generates a text-based report of logged hours and stores them in Azure Blob Storage.

Note! You'll need access to a PostgreSQL server and database in order to test the apps and input data.

### Basic architecture

![image](https://github.com/user-attachments/assets/52780dc1-53a3-4004-b5f9-05ef9e0e8f73)

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

Note! You'll need an access to a PostgreSQL server and database in order to input data.

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

You can use the time management app together with an API platform, e.g. Postman. Run the above API calls to fetch, create, update or delete hour entries.

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
