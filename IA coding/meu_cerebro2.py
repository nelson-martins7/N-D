from google import genai

cliente = genai.Client()

# 1. Criamos o chat ANTES do loop e definimos o modelo aqui
chat = cliente.chats.create(model="gemini-2.5-flash") # Cria um chat usando o modelo Gemini-2.5-flash

while True: 
    # 2. Pegamos a mensagem do usuário
    mensagem = input("Digite sua mensagem para a IA: ")
    
    # Se o usuário digitar 'sair', o programa fecha
    if mensagem.lower() == 'sair':
        print("Até logo!")
        break
        
    # 3. Enviamos a mensagem ATRAVÉS do chat (que mantém a memória)
    resposta = chat.send_message(mensagem) # Envia a mensagem para o modelo e recebe a resposta
    
    # 4. Mostramos a resposta
    print(resposta.text) # Imprime a resposta
    print("-" * 30) # Uma linha para separar as conversas