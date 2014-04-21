from urllib2 import Request, urlopen
from Crypto.Cipher import DES3
from CoinMktAPI import CoinMktAPI
import base64
import json

URL = "%s/%s/%s" % (CoinMktAPI.URL,"session/signinkey",CoinMktAPI.ApiKey)

print "URL : " + URL
request = Request(URL)

response_body = urlopen(request).read()
print response_body

data = json.loads(response_body)
print("Key          : " +data['Key'])
print("Error Code   : " +str(data['Code']))
print("Error string : " + data['Err'])

encryptedString = base64.b64decode(data['Key'])
print("base64 string : " + encryptedString)
cipher = DES3.new( CoinMktAPI.ApiSecret, DES3.MODE_ECB )
decryptedString = cipher.decrypt(encryptedString)
print "Decrypted string " + decryptedString