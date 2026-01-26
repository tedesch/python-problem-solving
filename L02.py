# #problem 1
# string = "Polytechnic"

# print("%s...%s" % (string[0:3], string[len(string) - 3 : len(string)]))

# #problem 2
# price = float(input("Enter the price of the item: "))

# dollars = int(price)
# cents = int((price - dollars) * 100 + 0.5)

# # print(dollars,"dollars", cents, "cents")
# print(f"{dollars} dollars and {cents} cents")

# #problem 3
# names = ['Fritz']
# names.insert(0, 'Ann')
# names.insert(1, 'Melina')
# names.pop(2)
# names.append('Jorge')
# print(sorted(names))

#problem 4
contacts = {'Jenny': 8675309, 'James': 5551212}
print(*contacts)
print("Jenny's number is", contacts['Jenny'])
brian = contacts.get('James')

print('Brian has new number', brian)