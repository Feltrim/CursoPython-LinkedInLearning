#
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request
import json


def manipula_json():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    web_url = urllib.request.urlopen(endereco)
    if web_url.getcode() == 200:
        dados = web_url.read()
        o_json = json.loads(dados)

        contagem = o_json["metadata"]["count"]
        print(f"Contagem {str(contagem)}")

        for local in o_json["features"]:
            print(local["properties"]["place"])


manipula_json()
