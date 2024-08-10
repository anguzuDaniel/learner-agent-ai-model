import pymysql
import json

# Database configuration (Moodle)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'moodle'
}

def fetch_courses():
    # Establish connection to Moodle database
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Fetch course data from Moodle database
    query = "SELECT id, fullname AS name FROM mdl_course LIMIT 5"
    cursor.execute(query)
    courses = cursor.fetchall()

    connection.close()
    return courses

def recommend(user_input):
    # Load intents and responses from the JSON file
    with open('data.json', 'r') as file:
        intents = json.load(file)['intents']

    # Fetch courses from Moodle
    courses = fetch_courses()
    responses = {}

    # Iterate through intents to find matching patterns
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                for response in intent['responses']:
                    if response['type'] == 'course':
                        # Find the course by its ID from Moodle data
                        course = next((c for c in courses if c['id'] == response['id']), None)
                        if course:
                            responses[response['name']] = course['name']
                    else:
                        responses[response['name']] = response['name']
                
    return responses
