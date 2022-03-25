import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 72.5
HEIGHT_CM = 167.64
AGE = 25
exercise_text = input("what exercise did you do?")
bearer_headers = {
    "Authorization": "Bearer iamfiercewithpeoplewhostealsecretstuff"
}
headers = {
    "x-app-id": "0b5bec1d",
    "x-app-key": "9bdce78a7f8ac5d425f5a56a903a3742"
}
SHEET_ENDPOINT = "https://api.sheety.co/00205ec55b1d487b42f799a269495567/copyOfMyWorkouts/workouts"

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
result = response.json()
print(result)
for exercise in result['exercises']:
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    sheet_parameters = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_parameters, headers=bearer_headers)
    print(sheet_response.text)
