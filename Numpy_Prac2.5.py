# C1-84158_Ujjwal Shelke

cheking_num = lambda num : num > 18

num_data = input("Enter the number data = ").split()
num_data = list(map(float, num_data))

check_num = list(map(cheking_num,num_data))

print(f"remainder is = {check_num}")