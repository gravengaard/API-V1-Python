from urllib2 import Request, urlopen
from Crypto.Cipher import DES3
from CoinMktAPI import CoinMktAPI
import base64
import json

URL = "%s/%s/%s" % (CoinMktAPI.URL,"session/signinkey",CoinMktAPI.ApiKey)

request = Request(URL)

response_body = urlopen(request).read()
data = json.loads(response_body)
encryptedString = base64.b64decode(data['Key'])
cipher = DES3.new( CoinMktAPI.ApiSecret, DES3.MODE_ECB )
decryptedString = cipher.decrypt(encryptedString)
