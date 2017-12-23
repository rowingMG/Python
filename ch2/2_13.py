#Calculating restaurant tab using gift card

#predefine tax
tax_rate = 0.08

#Prompt
print('This program blah blah blah')

#get inputs
gift_cert = float(input('상품권 얼마?: '))

print("Enter ordered items for person1");
appetizer1 = float(input('Appetizer: '))
entree1 = float(input('Entree: '))
drinks1 = float(input('Drinks: '))
dessert1 = float(input('Appetizer: '))

print('')
print("Enter ordered items for person2");
appetizer2 = float(input('Appetizer: '))
entree2 = float(input('Entree: '))
drinks2 = float(input('Drinks: '))
dessert2 = float(input('Appetizer: '))

#Calculate
total_price = appetizer1 + entree1 + drinks1 + dessert1 +\
              appetizer2 + entree2 + drinks2 + dessert2
tax = total_price * tax_rate
tab = total_price + tax - gift_cert

#Print result
print('')
print('Ordered items: $', format(total_price, '.2f'))
print('Restaurant tax: $', format(tax, '.2f'))
print('Tab: $', format(tab, '.2f'))
