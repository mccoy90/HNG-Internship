from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    local_timezone = pytz.timezone('Europe/Berlin')  # Replace with your desired time zone
    current_day = datetime.datetime.now(local_timezone).strftime('%A')

    # Get current UTC time
    current_utc_time = datetime.datetime.now(pytz.utc).strftime('%H:%M:%S')

    # GitHub URLs
    github_file_url = "https://github.com/mccoy90/HNG-Internship/blob/main/slack_info.py"
    github_repo = "https://github.com/mccoy90/HNG-Internship"

    # Prepare the response JSON
    response = {
        "current_day": current_day,
        "current_utc_time": current_utc_time,
        "github_file_url": github_file_url,
        "github_repo": github_repo,
        "slack_name": slack_name,
        "status_code": 200,
        "track": track
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)