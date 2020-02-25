city_list = {"city": "Москва", "temperature": "20"}

print(city_list["city"])

city_list["temperature"] = 15
print(city_list)

print(city_list.get('country'))
print(city_list.get('country', 'Россия'))

city_list['date'] = '27.05.2019'
print(city_list)

print(len(city_list))