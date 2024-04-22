str = input("Enter the string : ")

alpha_list=[]
digit_list=[]
special_list=[]

for c in str:
    if (c.isalpha()):
        alpha_list.append(c)
    elif (c.isdigit()):
        digit_list.append(c)
    else:
        special_list.append(c)


if (len(alpha_list)==4 and len(digit_list) == 4 and len(special_list)==1 and len(str) == 9):
    print("Valid String")
else:
    print("Not Valid String")



