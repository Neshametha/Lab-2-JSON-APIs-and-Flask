import json

def save_to_file(data,file_name):
    with open(file_name,"w") as write_file:
        json.dump(data, write_file,indent=2)
        print ("The file {0} was successfully created".format(file_name))

def read_from_file(file_name):
    with open(file_name, 'r') as read_file:
        data=json.load(read_file)
        print("The file {0} was successfully read".format(read_file))
    return data
