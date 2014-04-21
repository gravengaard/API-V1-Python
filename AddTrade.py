from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI
import json
from string import join

sampleTradeType = "0"
sampleTradeSide = "0"
sampleAmount = "1.008"
samplePrice = "3.88"

URL = "%s/%s/%s/%s/%s/%s/%s/%s/%s" % (CoinMktAPI.URL,"order/new", CoinMktAPI.SessionToken, CoinMktAPI.Pair , sampleTradeType, sampleTradeSide,samplePrice, sampleAmount, CoinMktAPI.TradeLevel)
print "URL : " + URL

try: 
    request = Request(URL,"POST")
    response_body = urlopen(request).read()
    print "Response body " + response_body

    data = json.loads(response_body)
    if data is not None: 
        print("Error Code   : " +str(data['Code']))
        print("Error string : " + data['Err'])
        print("Trade Id     : " +data['TradeId'])
        raise Exception, "[" +str(data['Code']) + "] : " +  "Error string : " + data['Err']
    else:    
        print("Error - trade was not created for values in URL: " +URL)

except Exception, e :
    print "Error while creating trade. Details are " + e.message 
finally:   
    print("Completed addtrade task " )