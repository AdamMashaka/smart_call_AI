import requests

# Headers
headers = {
   'Authorization': 'Secret_Key'
}

# Data
data = {
  "phone_number": "+255767939809", 
  "from": None,
  "task": "Karibu Zeno Limited , Bonyeza moja kwa huduma ya tunda Shopping , mbili kuhusu ZenoHub, na tatu kuongea Sales Manager. ",
  "model": "enhanced",
  "language": "eng",
  "voice": "ravi",
  "voice_settings": {},
  "local_dialing": False,
  "max_duration": 12,
  "answered_by_enabled": False,
  "wait_for_greeting": False,
  "record": False,
  "amd": False,
  "interruption_threshold": 100,
  "temperature": None,
  "transfer_list": {
    "1": "+255744963858",
    "2": "+255744963858",
    "3": "+255744963858"
  },
  "metadata": {},
  "pronunciation_guide": [],
  "start_time": None,
  "request_data": {},
  "tools": [],
  "webhook": None
}

# API request 
response = requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)

# Check the response
if response.status_code == 200:
    print("Call successfully initiated.")
else:
    print("Error:", response.status_code, response.text)
