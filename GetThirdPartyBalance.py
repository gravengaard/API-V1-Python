from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

sampleThirdPartyAccountID =  "5045fb47-d909-4da6-98bb-64b1f457ceb3"

URL = "%s/%s/%s/%s/%s" % (CoinMktAPI.URL,"thirdparty/balances", CoinMktAPI.SessionToken,  "1", sampleThirdPartyAccountID)
print "URL : " + URL

request = Request(URL)
response_body = urlopen(request).read()
print response_body

