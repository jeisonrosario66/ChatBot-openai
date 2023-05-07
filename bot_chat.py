""" 
Bloque: Modelo
"""
import openai
from env import ORG, APIKEY # modulo con las credenciales para acceder a la api

class BotChat():
    """Crea la conexcion con la api de openai
    """
    def __init__(self, userName):
        """Constructor del objeto

        Args:
            userName (srt): nombre para el usuario a usar
        """
        openai.organization = ORG
        openai.api_key = APIKEY
        self.userName = userName
        self.nameAI = "AI"
        self.respuestaTxt = ""
    
    def consulta(self, pregunta):
        """metodo de consulta al bot

        Args:
            pregunta (srt): Mensaje a enviar al bot
        """
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