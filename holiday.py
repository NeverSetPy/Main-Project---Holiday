# Key value pairs to access city and hotel cost. 
# Function for menu which displays flight options for user. Accesses Dictionary to eliminate hard coding of cities.
# Outer while loop to embed loops within body of code for exception handling.
# Functions for each cost calculation (hotel, plane, car) with f strings to display information to user.
# Final total holiday cost function at end after all questions are asked and all data is gathered.

while True:    

    cities = {'london': 140,
                'amsterdam': 285,
                'st.petersburg': 370,
                'milan': 155,
                'helsinki': 140,
                'johannesburg': 230,
                'jaipur': 360,
                'tokyo': 300,
                'istanbul': 210
                }
    
    city_keys = list(cities.keys())

    def menu():
        print()
        print(city_keys[0])
        print(city_keys[1])
        print(city_keys[2])
        print(city_keys[3])
        print(city_keys[4])
        print(city_keys[5])
        print(city_keys[6])
        print(city_keys[7])
        print(city_keys[8],'\n')
            
        
    def hotel_cost(num_nights, cost = 245):
        total_hotel = num_nights * cost
        print(f'Hotel cost is £{total_hotel}.\n')
        return total_hotel

    def plane_cost(city_flight):
        total_plane = cities[city_flight]
        print(f'Flight cost is £{total_plane}.\n')
        return total_plane
        
    def car_rental(rental_days, car_cost = 72):
        total_car = rental_days * car_cost
        print(f'Car rental cost is £{total_car}.\n')
        return total_car

            
    menu()

    while True:
        try:
            city_flight = plane_cost(input('What city do you want to fly to?\n> '))
            break
        except KeyError:
            print('You misspelled a city.')
            continue
                
    while True:
        try:
            num_nights = hotel_cost(int(input('How many nights are you staying at the hotel?\n> ')))
            break
        except ValueError:
            print('Please enter a number.')

    while True:
        try:
            rental_days = car_rental(int(input('How many days do you need the car for?\n> ')))
            break
        except ValueError:
            print('Please enter a number.')

    def holiday_cost(flight = city_flight, hotel = num_nights, car = rental_days):
        total = flight + hotel + car
        return total     

    print(f'The total cost of your holiday, including your flight, hotel and car rental will be:\n£{holiday_cost()}')
    break
