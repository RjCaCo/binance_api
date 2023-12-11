
from django.http import JsonResponse
from django.shortcuts import render
import requests

def obter_dados_da_api(request):
    api_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(api_url)
    data_response = response.json()
    return JsonResponse(data_response)

def index(request):
    return render(request, 'binance_app/index.html')

