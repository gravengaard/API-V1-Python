from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

#var URL = coin.CoinMktAPI.BaseURL + "session/end" + "/" + coin.CoinMktAPI.SessionToken;
URL = "%s/%s/%s" % (CoinMktAPI.URL, "session/end", CoinMktAPI.SessionToken)

print "URL : " + URL
request = Request(URL)

response_body = urlopen(request).read()
print response_body

