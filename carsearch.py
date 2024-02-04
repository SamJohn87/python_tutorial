mileage_used_mustang = 53291

car_ad = f'Used Mustang for sale with {mileage_used_mustang} mileage'

search_ad = 'Mustang' in car_ad
mileage_check = mileage_used_mustang < 100000

if search_ad and mileage_check:
    print('Mustang is in the ad and mileage is below 100,000 miles')
