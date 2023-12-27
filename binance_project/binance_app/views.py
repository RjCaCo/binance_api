from django.http import JsonResponse
from django.shortcuts import render
import requests

valor_abertura: any  = 0
valor_inicial: any  = 0
valor_atualizado: any  = 0

variacao_percentual: any  = None
mensagem: any  = None

solana_inicial: any  = None
solana_atualizado: any  = None

saldo_btc: any  = 1
saldo_dolares: any  = 10000
saldo_total: any  = 0

comprou_btc: bool = False
vendeu_btc: bool = False
valor_operacao_compra: any  = 0

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
    response = resp.json()
    inteiro, decimal = str(response['price']).split('.')
    valor_formatado = f"{inteiro}.{decimal[:2]}"
    valor_inicial = float(valor_formatado)
    return JsonResponse(response)

def atualizado(request):
    global valor_atualizado
    resp = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    response = resp.json()
    inteiro, decimal = str(response['price']).split('.')
    valor_formatado = f"{inteiro}.{decimal[:2]}"
    valor_atualizado = float(valor_formatado)
    return JsonResponse(response)

def solanaInicial(request):
    global solana_inicial
    resp = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT')
    response = resp.json()
    inteiro, decimal = str(response['price']).split('.')
    valor_formatado = f"{inteiro}.{decimal[:2]}"
    solana_inicial = float(valor_formatado)
    return JsonResponse(response)

def solanaAtualizado(request):
    global solana_atualizado
    resp = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT')
    response = resp.json()
    inteiro, decimal = str(response['price']).split('.')
    valor_formatado = f"{inteiro}.{decimal[:2]}"
    solana_atualizado = float(valor_formatado)
    return JsonResponse(response)

def comparar_variacao_BTC(valor_abertura, valor_atualizado):
    global mensagem
    global variacao_percentual
    global valor_operacao_compra
    global saldo_dolares
    global saldo_btc
    global comprou_btc
    global vendeu_btc

    variacao_completa = ((valor_atualizado - valor_abertura) / abs(valor_abertura)) * 100
    variacao_percentual = round(variacao_completa, 2)

    if abs(variacao_percentual) > 1:
        if variacao_percentual > 0:
            # Prova de ir pra argentina / paraguai do Ricardo, se no codigo não funcionar não passa de ano!!!!
            #coloque seu codigo aqui!

            mensagem = f"A variação foi de {variacao_percentual:.2f}% para mais."
        else:
            vendeu_btc = True
            valor_operacao_compra = saldo_dolares * 0.03
            saldo_dolares = saldo_dolares - valor_operacao_compra
            valor_operacao_convertido = valor_operacao_compra / valor_atualizado
            saldo_btc = saldo_btc + valor_operacao_convertido
            mensagem = f"A variação foi de {variacao_percentual:.2f}% para menos."
    else:

        mensagem = "A variação não atingiu -3% nem +3%."
    return variacao_percentual, mensagem

""" def comparar_variacao_SOL(valor_abertura, valor_atualizado):
    global mensagem
    global variacao_percentual

    variacao_completa = ((valor_atualizado - valor_abertura) / abs(valor_abertura)) * 100
    variacao_percentual = round(variacao_completa, 2)

    if abs(variacao_percentual) > 3:
        if variacao_percentual > 0:
            mensagem = f"A variação foi de {variacao_percentual:.2f}% para mais."
        else:
            mensagem = f"A variação foi de {variacao_percentual:.2f}% para menos."
    else:
        mensagem = "A variação não atingiu 3%."
    return variacao_percentual, mensagem """

def index(request):
    saldo_total = saldo_dolares + (saldo_btc * valor_atualizado)
    return render(request, 'binance_app/index.html', {
        'inicial'           : valor_abertura,
        'atualizado'        : valor_atualizado,
        'solana_inicial'    : solana_inicial,
        'solana_atualizado' : solana_atualizado,
        'variacao'          : variacao_percentual,
        'mensagem'          : mensagem,
        'saldo_dolares'     : saldo_dolares,
        'saldo_btc'         : saldo_btc,
        'saldo_total'       : saldo_total,
    })

inicial(None)
abertura(None)
atualizado(None)
solanaInicial(None)
solanaAtualizado(None)
comparar_variacao_BTC(valor_abertura, valor_atualizado)

