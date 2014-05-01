from urllib2 import Request, urlopen
from Crypto.Cipher import DES3
from CoinMktAPI import CoinMktAPI
import base64
import json
import hashlib


baseURLSigninKey = CoinMktAPI.URL + "/session/signinkey" ;
baseURLSessionToken = CoinMktAPI.URL + "/session/new" ;
  
sampleApiKey = '8B4B9E13366C41799A3B8C85DA9852DF';
sampleApiSecret = "807213ED44E54596B96192A7"
sampleTradeLevel = '0';
sampleSecondaryKey = "858be92709e545ba9a89d128f950e577";
sampleApiPIN = "88888";

URLSignin = "%s/%s" % (baseURLSigninKey, sampleApiKey)

request = Request(URLSignin)
response_body = urlopen(request).read()

data = json.loads(response_body)
encryptedString = base64.b64decode(data['Key'])
cipher = DES3.new( sampleApiSecret, DES3.MODE_ECB )
decryptedString = cipher.decrypt(encryptedString)

# this line cannot work because hashlib.sha512(sampleAPIPIN) returns an object not a string
hashvalue = hashlib.sha512("%s%s%s" % (decryptedString,sampleSecondaryKey, hashlib.sha512(sampleApiPIN)))
hex_dig = hashvalue.hexdigest()

URLSession = "%s/%s/%s" % (baseURLSessionToken,sampleApiKey, sampleTradeLevel )
URLSession += "?hashedSignInKey=" + base64.b64encode(hex_dig) 
request = Request(URLSession)
response_body = urlopen(request).read()
print response_body
