from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI

sampleThirdPartyAccountID = "99890348590345"

URL = "%s/%s/%s/%s" % (CoinMktAPI.URL,"thirdparty/movecoinkey", CoinMktAPI.SessionToken, sampleThirdPartyAccountID)

print "URL : " + URL
request = Request(URL)

response_body = urlopen(request).read()
print response_body