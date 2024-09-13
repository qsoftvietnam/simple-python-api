from flask import Flask, jsonify, abort, Response

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)


@app.route("/healthz", methods=["GET"])
def healthz():
    """
    Check the health status of the application.
    
    Returns:
        str: A string indicating the health status of the application.
    """Retrieve the list of days.
    
    Returns:
        flask.Response: A JSON response containing the list of days.
    """
    """Retrieve a specific day from the days list based on the given day_id.
    
    Args:
        day_id (int): The unique identifier of the day to retrieve.
    
    Returns:
        flask.Response: A JSON response containing the day information if found, or a 404 error if not found.
    """
    """
    return "Healthy"


@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)

"""Creates a new day entry.

Returns:
    tuple: A tuple containing a JSON response with a success status and HTTP status code 201 (Created).
"""

@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})


@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    app.run(debug=True)
