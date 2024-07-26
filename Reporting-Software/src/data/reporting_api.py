# Import libraries and functions

from flask import Flask, request
from reporting_app import main

# Initialize the Flask application

app = Flask(__name__)

# Define the route to create the report and upload it to Azure Blob Storage

@app.route('/report', methods=['GET'])
def get_report():
    try:  
        main()
        return {"message": "Report created and uploaded to Azure Blob Storage"}
    except:
        return {"error": "no data"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)