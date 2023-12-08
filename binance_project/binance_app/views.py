from django.shortcuts import render
import requests

def index(request):
    # Lógica para acessar a API da Binance e obter os dados do BTC
    # Substitua a URL abaixo pela URL correta da API da Binance
    api_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(api_url)
    btc_data = response.json()

    # Adicione lógica para obter dados de preços históricos, se necessário

    return render(request, 'binance_app/index.html', {'btc_data': btc_data})
