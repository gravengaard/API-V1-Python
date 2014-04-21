from urllib2 import Request, urlopen
from Crypto.Cipher import DES3
from CoinMktAPI import CoinMktAPI
import base64
import json
import hashlib


baseURLSigninKey = CoinMktAPI.URL + "/session/signinkey" ;
baseURLSessionToken = CoinMktAPI.URL + "/session/new" ;
  
sampleApiKey = '7B4B9E13366C41799A3B8C85DA9852DF';
sampleApiSecret = "907213ED44E54596B96192A7"
sampleTradeLevel = '0';
sampleSecondaryKey = "158be92709e545ba9a89d128f950e577";

URLSignin = "%s/%s" % (baseURLSigninKey, sampleApiKey)
print "URL-Signin : " + URLSignin

request = Request(URLSignin)
response_body = urlopen(request).read()
print response_body

data = json.loads(response_body)
print("***********************************************************")
print("Key          : " +data['Key'])
print("-----------------------------------------------------------")
print("Error Code   : " +str(data['Code']))
print("-----------------------------------------------------------")
print("Error string : " + data['Err'])
print("Key   : " +str(data['Key']))
encryptedString = base64.b64decode(data['Key'])
print("-----------------------------------------------------------")
print("Base64 string : " + encryptedString)
cipher = DES3.new( sampleApiSecret, DES3.MODE_ECB )
decryptedString = cipher.decrypt(encryptedString)
print("-----------------------------------------------------------")
print "Decrypted string " + decryptedString
print("-----------------------------------------------------------")

hashvalue = hashlib.sha512("%s%s%s" % (decryptedString,sampleSecondaryKey, hashlib.sha512("333333")))
hex_dig = hashvalue.hexdigest()

print(base64.b64encode(hex_dig))
print("***********************************************************")

# [GET] v1/session/new/{apiKey}/{tradeLevel}?hashedSignInKey={hashedSignInKey}
URLSession = "%s/%s/%s" % (baseURLSessionToken,sampleApiKey, sampleTradeLevel )
URLSession += "?hashedSignInKey=" + base64.b64encode(hex_dig) 
print("-----------------------------------------------------------")
print("URL-Session : " + URLSession)
print("***********************************************************")

request = Request(URLSession)
response_body = urlopen(request).read()
print response_body
