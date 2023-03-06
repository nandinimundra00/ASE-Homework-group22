import csv
import re
import json
# with open('../data/repgrid1.csv', 'r') as file:
#     csvread = csv.reader(file)
    
#     for row in csvread:
#         row = row.replace('{',)
#         print(row)
    

def file_to_json(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()

    contents = re.sub(r'(\w+)\s*=', r'"\1":', contents)
    contents = re.sub(r'{', '{', contents)
    contents = re.sub(r'}', '}', contents)
    contents = re.sub(r"'", '"', contents)
    json_data =  json.dumps(contents)
    print(json_data)
    print(type(json_data))
    
    print(json.loads(json_data))


file_to_json('../data/repgrid1.csv')
