# C1-84158-Ujjwal Shelke

conversion_to_dollar = lambda rupees : rupees / 85

rupees_data = input("Enter the rupees data = ").split()
rupees_data = list(map(float, rupees_data))

dollar_conversion = list(map(conversion_to_dollar, rupees_data))

print(f"ruppes converted to dollar = {dollar_conversion}")