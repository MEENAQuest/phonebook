name_list = []
phone_number_list = []
max_contacts = 3

for i in range(max_contacts):
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    name_list.append(name)
    phone_number_list.append(phone_number)

print("\nName\t\tPhone Number")
for i in range(max_contacts):
    print(f"{name_list[i]}\t\t{phone_number_list[i]}")