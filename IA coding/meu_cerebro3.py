from google import genai
from google.genai import types

# C maiúsculo aqui!
cliente = genai.Client()

# O nome do parâmetro TEM que ser exatamente "system_instruction"
configuracao = types.GenerateContentConfig(
    system_instruction = ""
)

chat = cliente.chats.create(
    model="gemini-2.5-flash",
    config=configuracao
)

while True: 
    mensagem = input("Digite sua mensagem para a IA: ")
    
    if mensagem.lower() == 'sair':
        print("Até logo, bons estudos!")
        break
        
    resposta = chat.send_message(mensagem)
    print("\n[Professor IA]:", resposta.text)
    print("-" * 50)
