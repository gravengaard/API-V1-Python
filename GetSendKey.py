from urllib2 import Request, urlopen
from CoinMktAPI import CoinMktAPI
from Crypto.Cipher import DES3
import base64
import json

URL = "%s/%s/%s" % (CoinMktAPI.URL, "wallet/sendcoinkey/new" , CoinMktAPI.SessionToken)
print "URL : " + URL
request = Request(URL,"POST")
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