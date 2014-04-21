from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

sampleCount = "?Count=10";

URL = "%s/%s/%s/%s/%s%s" % (CoinMktAPI.URL,"book", CoinMktAPI.ApiKey, CoinMktAPI.Pair, CoinMktAPI.TradeLevel, sampleCount)
print "URL : " + URL

request = Request(URL)
response_body = urlopen(request).read()
print response_body