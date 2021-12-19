import requests
import json
from types import SimpleNamespace
import re

url="https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=1e93f3210bac57570f842906f08558ca0fbf1606&formato=json"
data = requests.get(url)

x = json.loads(data.text, object_hook=lambda d:SimpleNamespace(**d))

    # x  = namespace(UFs=[namespace(Valor='30.855,66', Fecha='2021-12-07')])
    # x.UFs  = [namespace(Valor='30.855,66', Fecha='2021-12-07')]
valorUF = x.UFs[0].Valor
valorUF = re.sub('[\.]','',valorUF)
valorUF = valorUF[:5]
valorUF = int(valorUF)

