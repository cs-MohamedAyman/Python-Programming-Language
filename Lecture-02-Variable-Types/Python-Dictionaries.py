#Python Dictionaries

x = {'python':'easy', 'c++':'medium', 'java':'hard'}
print(x)
print(len(x))
print(x['python'])
x['c#'] = 'medium'
x['c++'] = 0
print(x)
print(len(x))
print(x['c#'])
print(x['c++'])

x = {'London': 6, 'Paris': 8, 'Barcelone': 11}
print(x)
x['Paris'] = {'Zurich': 2, 'Roma': 5}
x['Barcelone'] = 'windy'
print(x)
print(x['Paris']['Zurich'])
print(x['Barcelone'][:3])
