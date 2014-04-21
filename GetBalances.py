from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

URL = "%s/%s/%s/%s" % (CoinMktAPI.URL,"account/balances", CoinMktAPI.SessionToken,CoinMktAPI.TradeLevel)
print "URL : " + URL

request = Request(URL)
response_body = urlopen(request).read()
print response_body

