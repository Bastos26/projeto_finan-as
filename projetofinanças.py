import requests
import os

pais = input("Digite um país (em inglês, ex: brazil, argentina): ").strip().lower()
token = os.environ.get('token')
if not token:
    raise ValueError("⚠️ Token não encontrado. Verifique a variável de ambiente 'token'.")

url = f"https://brapi.dev/api/v2/prime-rate?country={pais}&token={token}"
resposta = requests.get(url)
if resposta.status_code == 200:
    data = resposta.json()
    taxas = data.get("prime-rate", [])  # nota: chave é 'prime-rate', com hífen
    if taxas:
        print(f"\n📈 Taxas de juros para {pais.capitalize()}:\n")
        for item in taxas:
            print(f"• Data: {item['date']} → Taxa: {item['value']}%")
    else:
        print("🔍 Nenhum dado disponível para esse país.")
else:
    print(f"❌ Erro ao buscar dados: {resposta.status_code} - {resposta.text}")


