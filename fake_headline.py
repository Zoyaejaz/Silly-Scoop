import random

subjects = [
    "Shahrukh Khan",
    "Virat Kholi",
    "Nirmala Sitaraman",
    "A Mumbai cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi",
    "Bhopal"
]

actions=[
    "launches",
    "cancels plan",
    "dances with",
    "eats",
    "plays",
    "declares war on"
    "orders",
    "celebrates"
]

places_or_things =[
    "at Red fort",
    "in Mumbai Local Train",
    "a plate of Samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing =random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {places_or_thing} "
    print("\n" + headline)

    use_input = input("\nDo you want another headline? (yes/no)").strip()
    if user_input == "no":
        break

print("\n Thanks for using the Fake news Headline ggenerator. Have a fun day")
