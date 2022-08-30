statement1 = "Pakistan is a developing country"
print(statement1.upper())
print(statement1.lower())
print(statement1.find('y'))
# case sensitive (-1)
print(statement1.find('Y'))
print(statement1.find('i'))
print(statement1.find('p'))
print(statement1.find('P'))
print(statement1.find('K'))
# only starting index will display
print(statement1.find(' is '))
print(statement1.find(' Is '))
print(statement1.replace('a', 'A'))

# boolean displays
# also case_sensitive
print('a' in statement1)
print("A" in statement1)
