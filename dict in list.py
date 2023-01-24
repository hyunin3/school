infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
#print(infos[0]['age']+infos[1]['age'])
result = 0
for dic in infos:
    result = result + dic['age']
print(result)
