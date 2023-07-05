from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Define a route and function to handle incoming requests
@app.route('/')
def hello_world():
    return 'David Test123'

# Start the web server
if __name__ == '__main__':
    app.run(host='https://descriptionshortener.azurewebsites.net/', port=8000)