#
#Processamento de dados provenientes do JSON
#
import urllib.request
import json

def pJSON():
  endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
  wURL = urllib.request.urlopen(endereco)
  if (wURL.getcode() == 200):
    pagedata = wURL.read()
    obJSON = json.loads(pagedata)

    total = obJSON["metadata"]["count"]
    print("O total de dados processados é: " + str(total))

    for local in obJSON["features"]:
      print(local["properties"]["place"])

pJSON()

