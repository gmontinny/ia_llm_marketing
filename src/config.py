import os
from dotenv import load_dotenv

load_dotenv()

# Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Geral
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

PROVIDERS = ["Groq (Llama)", "OpenAI (ChatGPT)"]
PLATFORMS = ["Instagram", "Facebook", "LinkedIn", "Blog", "E-mail"]
TONES = ["Normal", "Informativo", "Inspirador", "Urgente", "Informal"]
LENGTHS = ["Curto", "Médio", "Longo", "1 parágrafo", "1 página"]
AUDIENCES = ["Geral", "Jovens adultos", "Famílias", "Idosos", "Adolescentes"]
