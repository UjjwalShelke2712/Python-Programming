# C1-84158-Ujjwal Shelke

conversion_to_miles = lambda km : km * 0.621371

distance_data = input("Enter Distance in kilometer = ").split()
distance_data = list(map(float,distance_data))

distance_miles = list(map(conversion_to_miles, distance_data))

print(f"Distance in miles = {distance_miles}")