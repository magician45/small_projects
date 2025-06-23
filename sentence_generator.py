import random

names = ["Peter", "Michell", "Jane", "Steve"]
cities = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "a cake", "an apple", "a laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]


def random_word(words):
    return random.choice(words)


print("Hello, let's try this:")
while True:
    random_name = random_word(names)
    random_city = random_word(cities)
    random_verb = random_word(verbs)
    random_noun = random_word(nouns)
    random_adverb = random_word(adverbs)
    random_detail = random_word(details)
    print(f'{random_name} form {random_city} {random_adverb} {random_verb} {random_noun}')
    input("Click [Enter] to generate a new one")


