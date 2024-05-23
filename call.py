import requests

# Headers
headers = {
   'Authorization': 'sk-hfp8wuylk9ymt21j97vkqol0x29ljlzfravq39dcbdh43uaiugl7fn6zvqisuy5969'
}

# Data
data = {
  "phone_number": "+255717148269",  # Add the recipient's phone number
  "from": None,
  "task": "You: Mambo Vipi , Naitwa Adam Katani kutoka Agritech ni huduma kwa bwana shamba bot, Nilikuwa nataka kushiriki habari njema nawe kuhusu jinsi ya kurahisisha maisha ya vizazi vijavyo kuhusu Hali ya hewa.\n\n\nYou: Umewahi kusikia kuhusu Kahawa mall? Siyo tu bidhaa kwa ajili ya kunywa pia ina save halli ya hewa kwa kunywa carbon gasses, hadi vifaa vya elektroniki. Na unajua lililo zuri zaidi? Usafirishaji ni bure popote ulipo Tanzania! , Download app ya tunda Shopping sasa inapatikana Playstore na Appstore\n\n\nYou: Hakika kabisa! Tunda Shopping inashirikiana na wauzaji wengi waliothibitishwa ili kuhakikisha unapata bidhaa bora na za bei nafuu. Ukiwa na Tunda Shopping, unapata kila unachohitaji kwa , bila kupoteza muda na gharama za usafiri.\n\nCustomer: Ngoja nikwambie, hii ni habari njema sana! huna haja ya kwenda kuhangaika kununua bidhaa , download app ya tunda shopping ununue sasa !\n\nYou: Karibu sana! Ukiwa na maswali yoyote au unahitaji msaada, usisite kuniuliza.\n\nCustomer: Asante sana! Bila shaka utaingia Tunda Shopping leo leo.\n\nYou: Hakuna shida! Nakuhakikishia utafurahia manunuzi yako.\n\nCustomer: Asante, na wewe pia! Baadaye!\n\nYou: Baadaye!",
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
