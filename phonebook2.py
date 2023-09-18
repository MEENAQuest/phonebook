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

searched_name = input("\nEnter name for search: ")
print("Your Search Result is: ")

if searched_name in name_list:
    name_index = name_list.index(searched_name)
    phone_number = phone_number_list[name_index]
    print(f"Name: {searched_name} \t Phone Number: {phone_number}")
else:
    print("This name is not in your Phonebook")    