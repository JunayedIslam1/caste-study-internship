import json
file = open("pos_0.png.json", "r")
data = file.read()
finalData = json.loads(data)

print(finalData)
