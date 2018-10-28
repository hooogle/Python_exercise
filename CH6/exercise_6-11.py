cities = {
    'Beijing':{
        'country': 'China',
        'population': '100 million',
        'fact': 'The captial of China.'
        },
    'NewYoke':{
        'country': 'USA',
        'population': '50 million',
        'fact': 'a big city in America.'
        },
    'Tokyo':{
        'country': 'Japan',
        'population': '80 million',
        'fact': 'the captial of Japan',
        }
    }
for city_name, city_info in cities.items():
    print('city name: ' + city_name)
    print(city_info['country'] + '\n' + city_info['population'] + '\n' + city_info['fact'])