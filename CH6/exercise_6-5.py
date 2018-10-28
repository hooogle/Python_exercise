rivers = {
    'nile': 'Egypt',
    'chang jiang': 'China',
    'Mississipi': 'USA',
    }
for river, country in rivers.items():
    print("The " + river + ' runs trhough ' + country + '.')
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)