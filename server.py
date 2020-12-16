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
"Legend": "Latitude",
"Data": 1200,
"Label": "United Kingdom",
"Title":"Sales Numbers for Dell Products"    
},
{
"Legend": "Precision ",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "Australia",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Precision ",
"Data": 3600,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Optiplex",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "Israel",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "France",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Precision ",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "Netherlands",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Optiplex",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "United States",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "Ireland",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Precision ",
"Data": 1200,
"Label": "Canada",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Latitude",
"Data": 1200,
"Label": "India",
"Title":"Sales Numbers for Dell Products" 
},
{
"Legend": "Precision ",
"Data": 3600,
"Label": "United Kingdom",
"Title":"Sales Numbers for Dell Products" 
}
]
    # return name and email as a JSON httpresponse using jsonify
    return jsonify(response)
# When run from command line, start the server.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
