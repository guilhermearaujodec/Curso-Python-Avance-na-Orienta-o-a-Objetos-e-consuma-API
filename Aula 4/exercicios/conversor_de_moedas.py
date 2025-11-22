import requests

url = "https://economia.awesomeapi.com.br/last/BRL-USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    cotacao = float(data['BRLUSD']['bid'])
    mensagem = f"U$ 1 real corresponde a $ {cotacao:.2f}"
    print(mensagem)
else:
    print(f"A requisição falhou com o código de status {response.status_code}") 
    