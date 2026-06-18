from google import genai

cliente = genai.client() # Cria um cliente para a API

while True:

    resposta = cliente.models.generate_content(
        model = "gemini-2.5-flash",
        content = input("Digite o que você quer que eu faça: ",)
    ) # Envia a solicitação para o modelo Gemini-2.5-flash
    print(resposta.text) # Imprime a resposta