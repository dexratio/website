from django.shortcuts import render

def home(request):
    import requests
    import json


    # grab crypto price data https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,BSV,ETH,XRP,BCH,XMR,ZEC,TORN,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)


    # grab crypto news data
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    #https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter a crypto symbol into the form above..."
        return render(request, 'prices.html', {'notfound': notfound})
