people = [
 'Marek',
 'Monke',
 'Bednar'
]
length_of_list = len(people)

print(length_of_list)


def print_all_el(list):
    for x in list:
        print(x, "Print all el func")

print_all_el(people)