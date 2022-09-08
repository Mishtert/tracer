import json


# reading the nct_ta dictionary 
with open('asset/data/nct_ta_dict.json') as f:
    data = f.read()
nct_ta_dict = json.loads(data) #load dict
# print(len(nct_ta_dict))

# reading the mesh_to_ta_dict dictionary 
with open('asset/data/mesh_to_ta_dict.json') as f:
    data = f.read()
mesh_to_ta_dict = json.loads(data) #load dict
# print(len(mesh_to_ta_dict))
with open('asset/data/replacement_dict.json') as f:
    data = f.read()
repl_dict = json.loads(data) #load dict
# print(len(mesh_to_ta_dict))

with open('asset/data/entry_terms_dict.json') as f:
    data = f.read()
entry_dict = json.loads(data) #load dict
# print(len(mesh_to_ta_dict))

with open('asset/data/final_check_dict.json') as f:
    data = f.read()
final_check = json.loads(data) #load dict
# print(len(mesh_to_ta_dict))

with open('asset/data/gb_us_dict.json') as f:
    data = f.read()
gb_2_us_dict = json.loads(data) #load dict
# print(len(mesh_to_ta_dict))