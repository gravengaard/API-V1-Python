from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

URL = "%s/%s/%s/%s" % (CoinMktAPI.URL,"order/status", CoinMktAPI.SessionToken, CoinMktAPI.TradeId)
print "URL : " + URL

request = Request(URL,"GET")
response_body = urlopen(request).read()
print response_body