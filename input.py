price = int(input('Cash amount '))
split_by = int(input('Split by '))
tip_amount = float(input('tip '))

total = price + (price * tip_amount)
total_per_person = total / split_by

print(total)
print(total_per_person)