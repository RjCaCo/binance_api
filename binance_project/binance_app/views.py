from django.http import JsonResponse
from django.shortcuts import render
import requests

valor_abertura = None
valor_atualizado = None
variacao_percentual = None
mensagem = None

def abertura(request):
    global valor_abertura
    params = {
        'limit'     : 1,
        'interval'  : '1d',
        'symbol'    : 'BTCUSDT'
    }
    base_url = 'https://api.binance.com/api/v3/klines'
    response = requests.get(base_url, params=params)
    response_abertura = response.json()
    valor_abertura = float(response_abertura[0][1])

def inicial(request):
    global valor_inicial
    resp = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    valor_inicial = resp.json()
    return JsonResponse(valor_inicial)

def atualizado(request):
    global valor_atualizado
    resp = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    response = resp.json()
    inteiro, decimal = str(response['price']).split('.')
    valor_formatado = f"{inteiro}.{decimal[:2]}"
    valor_atualizado = float(valor_formatado)
    return JsonResponse(response)

def comparar_variacao(valor_abertura, valor_atualizado):
    global mensagem
    global variacao_percentual

    # Calcular o percentual de variação
    variacao_completa = ((valor_atualizado - valor_abertura) / abs(valor_abertura)) * 100
    variacao_percentual = round(variacao_completa, 2)

    # Verificar se a variação é maior que 3%
    if abs(variacao_percentual) > 3:
        if variacao_percentual > 0:
            mensagem = f"A variação foi de {variacao_percentual:.2f}% para mais."
        else:
            mensagem = f"A variação foi de {variacao_percentual:.2f}% para menos."
    else:
        mensagem = "A variação não atingiu 3%."
    return variacao_percentual, mensagem

def index(request):
    return render(request, 'binance_app/index.html', {
        'inicial'   : valor_abertura,
        'atualizado': valor_atualizado,
        'variacao'  : variacao_percentual,
        'mensagem'  : mensagem
    })

inicial(None)
abertura(None)
atualizado(None)
comparar_variacao(valor_abertura, valor_atualizado)

