import urllib
from CoinMktAPI import CoinMktAPI
import json
import random
import urllib2
import sys
import traceback

sampleTradeType = "0"
sampleTradeSide = "1"
sampleAmount = "1.01"
samplePrice = "18.88"

URL = "%s/%s/%s" % (CoinMktAPI.URL,"order/new/many", CoinMktAPI.SessionToken)
print "URL : " + URL

def trace_except(sysexecinfo, smessage = ''):
   """ Trace exceptions """
   exc_type, exc_value, exc_traceback = sysexecinfo
   i, j = (traceback.extract_tb(exc_traceback, 1))[0][0:2]
   k = (traceback.format_exception_only(exc_type, exc_value))[0]
   return k
def encodeOrder(obj):
    if isinstance(obj, Order):
        return obj.__dict__
    return obj
class Order:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
class Orders(object):
    def __init__(self):
        self.list = []   

order = Order()
orders = Orders()

# looks like this ...
# [
#    {"FromCoinSymbol":"LTC","ToCoinSymbol":"USD","TradeType":1,"TradeSide":1,"TradePrice":8.88,"Units":0.01,"TradeLevel":0,"SessionToken":"EzAerFa1CtEQJa6tov9t9Hta-vyNFYzaKQ6hxRV9pw9Hj1_P7VVU3aA7WWHz8k3b-PU_XRHsPBQzZ0Nin_KVJyzuhWI0Oa7tjnxjeTUEwEA%3D","ApiKey":"","IP":"49.128.60.181"},
#    {"FromCoinSymbol":"BTC","ToCoinSymbol":"USD","TradeType":1,"TradeSide":1,"TradePrice":8.88,"Units":0.01,"TradeLevel":0,"SessionToken":"EzAerFa1CtEQJa6tov9t9Hta-vyNFYzaKQ6hxRV9pw9Hj1_P7VVU3aA7WWHz8k3b-PU_XRHsPBQzZ0Nin_KVJyzuhWI0Oa7tjnxjeTUEwEA%3D","ApiKey":"","IP":"49.128.60.181"},
#    {"FromCoinSymbol":"FTC","ToCoinSymbol":"USD","TradeType":1,"TradeSide":1,"TradePrice":8.88,"Units":0.01,"TradeLevel":0,"SessionToken":"EzAerFa1CtEQJa6tov9t9Hta-vyNFYzaKQ6hxRV9pw9Hj1_P7VVU3aA7WWHz8k3b-PU_XRHsPBQzZ0Nin_KVJyzuhWI0Oa7tjnxjeTUEwEA%3D","ApiKey":"","IP":"49.128.60.181"},
#    {"FromCoinSymbol":"FTC","ToCoinSymbol":"BTC","TradeType":1,"TradeSide":1,"TradePrice":8.88,"Units":0.01,"TradeLevel":0,"SessionToken":"EzAerFa1CtEQJa6tov9t9Hta-vyNFYzaKQ6hxRV9pw9Hj1_P7VVU3aA7WWHz8k3b-PU_XRHsPBQzZ0Nin_KVJyzuhWI0Oa7tjnxjeTUEwEA%3D","ApiKey":"","IP":"49.128.60.181"},
#    {"FromCoinSymbol":"PPC","ToCoinSymbol":"USD","TradeType":1,"TradeSide":1,"TradePrice":8.88,"Units":0.01,"TradeLevel":0,"SessionToken":"EzAerFa1CtEQJa6tov9t9Hta-vyNFYzaKQ6hxRV9pw9Hj1_P7VVU3aA7WWHz8k3b-PU_XRHsPBQzZ0Nin_KVJyzuhWI0Oa7tjnxjeTUEwEA%3D","ApiKey":"","IP":"49.128.60.181"}
# ]

for x in range(0, 200):
    order.AppId = "5511fa73-9f09-4dc0-a8a7-8e5a75160fc0"
    #order.ApiKey = CoinMktAPI.ApiKey
    order.IP = "49.128.60.181"
    order.FromCoinSymbol = CoinMktAPI.Currency
    order.ToCoinSymbol = "USD"
    order.TradePrice = round(random.uniform(1,3),3)
    order.Units = round(random.uniform(1,2),2)
    order.TradeSide = int(random.uniform(0,1))
    order.TradeLevel = 0
    order.TradeTypeCode  = 1
    order.SessionToken = CoinMktAPI.SessionToken
    orders.list.append(order)

#print "orders:"
#for o in orders.list:
#    print o.to_JSON()

orderstr = json.dumps(orders.list, default=encodeOrder)
length = len(orderstr)

#print "Orders : " + orderstr

myheaders = {'Content-Type': 'application/json','Content-Length': length}
#print "Headers : " + str(myheaders) 

#response = requests.post(URL,data=orderstr, headers=myheaders)
#print response.status_code
#print response.text
#print response.url


try:     
    request = urllib2.Request(url=URL,data=orderstr,headers=myheaders)
    request.get_method = lambda: 'POST'
    print "d2 " + request.get_data()
    
    response_body = urllib2.urlopen(request).read()

    print "Response " + response_body

    data = json.loads(response_body)
    if data is not None: 
        print("Error Code   : " +str(data['Code']))
        print("Error string : " +data['Err'])
    else:    
        print("Error - trade was not created ")

except: # catch *all* exceptions
    error = trace_except(sys.exc_info())    
    print("Error while creating trades : '%s' " % error)

finally:
    print("Completed add trade request ")