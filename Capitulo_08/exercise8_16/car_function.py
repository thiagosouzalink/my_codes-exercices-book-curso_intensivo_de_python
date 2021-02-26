
def make_car(car_model, car_maker, **car_info):
    car = {}
    car['model'] = car_model
    car['maker'] = car_maker
    for key, value in car_info.items():
        car[key] = value
    return car