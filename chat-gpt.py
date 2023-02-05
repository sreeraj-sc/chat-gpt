import openai
from gtts import gTTS
import os

# Apply for an API key from OpenAI and put it in this line:
openai.api_key = "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"

def communicate_with_chatbot(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response["choices"][0]["text"].strip()
    return message

while True:
    input_text = input("Me : ")
    output_text = communicate_with_chatbot(input_text)
    print("chat-gpt : " + output_text)
    tts = gTTS(text=output_text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3 > /dev/null 2>&1")
