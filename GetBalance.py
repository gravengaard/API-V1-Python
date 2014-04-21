from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

#var URL = coin.CoinMktAPI.BaseURL + "account/balance" + "/" + coin.CoinMktAPI.SessionToken + "/" + coin.CoinMktAPI.SampleCurrency + "/" + coin.CoinMktAPI.SampleTradeLevel;
URL = "%s/%s/%s/%s/%s" % (CoinMktAPI.URL,"account/balance", CoinMktAPI.SessionToken, CoinMktAPI.Currency, CoinMktAPI.TradeLevel)
print "URL : " + URL

request = Request(URL)
response_body = urlopen(request).read()
print response_body

