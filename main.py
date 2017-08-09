import json
import types

class Result:
    def __init__(self, key, name, role):
        self.key = key
        self.name = name
        self.role = role


f_roles = open('roles.txt').read()
f_champs = open('champs.txt').read()
f_result = open('result.txt', 'w+')

roles =  json.loads(f_roles)
champs = list(json.loads(f_champs)['data'].values())
results = []

for champ in champs:
    key = champ['key']
    name = champ['name']
    role = roles[champ['name']]
    result = Result(key,name,role).__dict__
    results.append(result)

f_result.write(json.dumps(results))

# for role in roles:
#     print(champ.name == role for champ in champs)