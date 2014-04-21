from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

URL = "%s/%s/%s/%s" % (CoinMktAPI.URL,"order/cancel", CoinMktAPI.SessionToken, CoinMktAPI.TradeId)
print "URL : " + URL

request = Request(URL,"POST")
response_body = urlopen(request).read()
print response_body