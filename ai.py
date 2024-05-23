import google.generativeai as genai

genai.configure(api_key="AIzaSyA5AXNj0uqvAaLApLiYkNCicLFzoReB8w4")

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest"
)

msg = "parts"

messages = model.start_chat(history=[
    {"role" : "user", msg : [""]},
    {"role": "model" , msg :[""] }
])

while True:

    user_input = input("Adam: ")
    user_rens = messages.send_message(user_input)
    print("Agri tech: " , messages.last.text)
    
