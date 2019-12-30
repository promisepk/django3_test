import requests
import json

url = 'http://localhost:8000/o/token/'
s = requests.Session()
var = {'grant_type':'authorization_code',
       'code':'ekB1mrbW1mh7Iud9INSjPc6alndY5z',
       'redirect_uri':'http://www.baidu.com',
       'client_id':'dqHNwrUWLaAew0hTFDpKh0XMPIrOWUZJdgQdbyNM',
       'client_secret':'YZ1RxoBOMS00OUzvbUy87WOJdah9ZiO5CGErL8uwsSB5hHbVhjXpyn0t8gFsFTSN0EOJ4WijtCcFsydDNUjgA5D51LE3MeHQbXaw8FSZj7h2PHhXppnnL9gHnfVQEq34',
            }
r = s.post(url=url,data=var)

print(r.text)