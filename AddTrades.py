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

for x in range(0, 20):
    order.FromCoinSymbol = CoinMktAPI.Currency
    order.ToCoinSymbol = "USD"
    order.TradePrice = round(random.uniform(1,3),3)
    order.Units = round(random.uniform(1,2),2)
    order.TradeSide = int(random.uniform(0,1))
    order.TradeLevel = 0
    order.TradeTypeCode  = 1
    order.SessionToken = CoinMktAPI.SessionToken
    orders.list.append(order)

orderstr = json.dumps(orders.list, default=encodeOrder)
length = len(orderstr)
myheaders = {'Content-Type': 'application/json','Content-Length': length}

try:     
    request = urllib2.Request(url=URL,data=orderstr,headers=myheaders)
    request.get_method = lambda: 'POST'
    response_body = urllib2.urlopen(request).read()
    data = json.loads(response_body)
    if data is not None: 
        print("Error Code   : " +str(data['Code']))
        print("Error string : " +data['Err'])
    else:    
        print("Error - trades not created ")

except: # catch *all* exceptions
    error = trace_except(sys.exc_info())    
    print("Error while creating trades : '%s' " % error)

finally:
    print("Completed add trade request ")
