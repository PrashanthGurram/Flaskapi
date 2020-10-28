# Import nessecary parts from flask and faker to generate random    # name and email.
from flask import Flask, request, jsonify
from faker import Faker
from flask_cors import CORS
# To create and initialize a faker generator.
fake = Faker()

# Create the app object that will route our calls.
app = Flask(__name__)
CORS(app)
# Add a single endpoint that we can use as an API to accept GET and # POST requests.
@app.route("/", methods=["POST", "GET"])
def index():
    # fake to create random name and email
    # name = fake.name()
    # email = fake.email()
    response = [
{
"Country": "United Kingdom",
"Price": 1200,
"Product": "Latitude"
},
{
"Product": "Precision ",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "Australia"
},
{
"Product": "Precision ",
"Price": 3600,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Optiplex",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "Israel"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "France"
},
{
"Product": "Precision ",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "Netherlands"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Optiplex",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "United States"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "Ireland"
},
{
"Product": "Precision ",
"Price": 1200,
"Country": "Canada"
},
{
"Product": "Latitude",
"Price": 1200,
"Country": "India"
},
{
"Product": "Precision ",
"Price": 3600,
"Country": "United Kingdom"
}
]
    # return name and email as a JSON httpresponse using jsonify
    return jsonify(response)
# When run from command line, start the server.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
