import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]
        
bars = 1;
print(bars);
people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Next person"]

for x in bars, people:
    if x is 'ACME':
        print(x)
    elif x is 'The Wren':
        print(x)
    else:
        print("Nothing happened")


random_bar = random.choice(bars)
random_person = random.choice(people)
random_person2 = random.choice(people)
print(
    f"How about you go to {random_bar} with {random_person} {random_person2}")
