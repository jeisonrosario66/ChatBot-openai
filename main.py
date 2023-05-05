#import   
import openai
from env import ORG, APIKEY

openai.organization = ORG
openai.api_key = APIKEY
#openai.Model.list()

conversation = ""
print("\t\texit() para salir")

def botChat():
    while True:
        question = input("Humano: ")
        if question == "exit()":
            break
        else:
            conversation += "\nHumano: " + question + "\nAi:"
            response = openai.Completion.create(
                engine="davinci",
                prompt=conversation,
                temperature=0.9,
                max_tokens=250,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["\n", " Humano:", " AI:"]
            )
            anwer=response.choices[0].text.strip()
            conversation += anwer 
            print("AI: " + anwer + "\n")

botChat()
































    
    
    
    
""" 
#import   
import openai

openai.api_key = "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"

conversation = ""

i=1
while (i != 0):
    question = input("Humano: ")
    conversation += "\nHumano: " + question + "\nAi:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Humano:", " AI:"]
    )
    anwer=response.choices[0].text.strip()
    conversation += anwer 
    print("AI: " + anwer + "\n")
"""    
