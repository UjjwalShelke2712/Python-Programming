# C1-84158-Ujjwal Shelke

fahren_cels = lambda fahrenheit: (fahrenheit - 32) * 5 / 9

fahren_data = list(map(float, input("Enter Fahrenheit temperatures separated by space: ").split()))

cel_data = list(map(fahren_cels, fahren_data))

print("Celsius temperatures:", cel_data)