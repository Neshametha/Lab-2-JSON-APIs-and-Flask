import json
import main_functions
import requests

url = "http://api.open-notify.org/astros.json"

# astronauts_in_space = requests.get(url).json()

astronauts_filename = "astronauts.json"

# astronauts_dict = main_functions.save_to_file(astronauts_in_space,astronauts_filename)

astronauts_dict = main_functions.read_from_file(astronauts_filename)
print (type(astronauts_dict))

print (astronauts_dict.keys())
print (len(astronauts_dict))

print (type(astronauts_dict["message"]))
print (type(astronauts_dict["people"]))
print (type(astronauts_dict["number"]))

for i in astronauts_dict["people"]:
    print (i["name"])
