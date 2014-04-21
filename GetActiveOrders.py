from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

# URL = coin.CoinMktAPI.BaseURL + "orders/" + coin.CoinMktAPI.SessionToken + "/" + coin.CoinMktAPI.SamplePair + "/" + coin.CoinMktAPI.SampleTradeStatusOpen + "/" + coin.CoinMktAPI.SampleTradeLevel;
URL = "%s/%s/%s/%s/%s/%s" % (CoinMktAPI.URL,"orders", CoinMktAPI.SessionToken,CoinMktAPI.Pair,CoinMktAPI.StatusOpenOrder, CoinMktAPI.TradeLevel)
print "URL : " + URL

request = Request(URL)
response_body = urlopen(request).read()
print response_body

