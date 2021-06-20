import urllib.request

url = "http://www.weather.com"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = str(urllib.request.urlopen(req).read())
templine = '<span data-testid="TemperatureValue" class="_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--tempValue--3KcTQ">'
stringstart = html.find(templine)
stringend = stringstart + len(templine)
print("Temperature is", html[stringend:stringend+2]+"°C")
