def build_profile(first, last, **user_info):  # **user_info is a dictionary
    """Build a dict with all information received"""
    profile = dict()
    profile['first_name'] = first
    profile['last'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


user_profile1 = build_profile('alfonso', 'areiza', age=31, city='Belo Horizonte')
print(user_profile1)

# user_profile2 = build_profile('alfonso', 'areiza', age=31, city='Belo Horizonte', 'Barranquilla')
# user_profile2 can not be created because 'Barranquilla' must be before the keyword arguments

# data = {"age":31, "city": 'Belo Horizonte'}
# user_profile3 = build_profile('alfonso', 'areiza', data)
# user_profile3 can not be created because data must be set in call-in function


def make_car(fabricante, modelo, **kwargs):
    car = {}
    car['maker'] = fabricante
    car['model'] = modelo
    for k, v in kwargs.items():
        car[k] = v
    return car


data = {'color': 'blue', 'tow_package': True}
car = make_car('subaru', 'outback', **data)
print(car)
