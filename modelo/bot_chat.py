import openai
from env import ORG, APIKEY

class BotChat():
    def __init__(self, userName):
        openai.organization = ORG
        openai.api_key = APIKEY
        self.userName = userName
        self.nameAI = "AI"
        self.respuestaTxt = ""
    
    def pregunta(self, pregunta):
        conversacion = ""
        question = f"{self.userName}: {pregunta}"
        conversacion += f"\n{self.userName}: " + question + f"\n{self.nameAI}:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=conversacion,
            temperature=0.9,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", f" {self.userName}:", f" {self.nameAI}:"]
        )
        anwer=response.choices[0].text.strip()
        conversacion += anwer 
        self.respuestaTxt = "AI: " + anwer + "\n"