from flask import Flask, jsonify, request

# Initialise the app
app = Flask(__name__)


# Define what the app does
@app.get("/greet")
def index():
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    if not fname and not lname:
        # If both first name and last name are missing, return an error
        return jsonify({"status": "error"})
    elif fname and not lname:
        # If first name is present but last name is missing
        response = {"data": f"Hello, {fname} !"}
    elif not fname and lname:
        # If first name is missing but last name is present
        response = {"data": f"Hello, Mr. {lname} !"}
    else:
        # if none of the above is true, then both names must be present
        response = {"data": f"Is your name {fname} {lname} ?"}

    return jsonify(response)
