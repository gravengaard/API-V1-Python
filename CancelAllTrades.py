from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

sampleTradeIds = "88d207ff-c208-4c10-a72e-7a9a8443c89c,ADAKSMDLKASD,8d21e6a4-06c7-472f-8c62-e0fa0f431a1a"

URL = "%s/%s/%s/%s" % (CoinMktAPI.URL,"order/cancel/all", CoinMktAPI.SessionToken,CoinMktAPI.TradeLevel)
print "URL : " + URL

request = Request(URL,"POST")
response_body = urlopen(request).read()
print response_body



#var URL = coin.CoinMktAPI.BaseURL + "order/cancel" + "/" + coin.CoinMktAPI.SessionToken + "/" + sampleTradeId;

