def describe_city(city, country = 'China'):
    return "\"" + city + ',' + country + "\""
print(describe_city('Beijing'))
print(describe_city('Shanghai'))
print(describe_city('Tokyo','Japan'))