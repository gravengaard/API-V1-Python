from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

# "https://stagepubapi.coinmkt.com/v1/account/addresses/" + coin.CoinMktAPI.SessionToken;
URL = "%s/%s/%s" % (CoinMktAPI.URL,"account/addresses", CoinMktAPI.SessionToken)
print "URL : " + URL

request = Request(URL)
response_body = urlopen(request).read()
print response_body

