# MadLibs
# Concatenate strings using f string method
print("Welcome to the game of MadLibs")
print("You will have to ")

adjective1 = input("Enter Adjective: ")
noun1 = input("Enter Noun: ")
past_verb = input("Enter verb in past tense: ")
adverb = input("Enter adverb: ")
adjective2 = input("Enter Adjective: ")
noun2 = input("Enter Noun: ")
noun3 = input("Enter Noun: ")
adjective3 = input("Enter Adjective: ")
verb = input("Enter verb: ")
adverb2 = input("Enter adverb: ")
past_verb2 = input("Enter verb in past tense: ")
adjective4 = input("Enter Adjective: ")

line1 =f"Today I went to the zoo. I saw a(n) {adjective1} {noun1} \
jumping up and down in its tree. He {past_verb} {adverb} through \
the large tunnel that led to its {adjective2} {noun2} I got some \
peanuts and passed them through the cage to a gigantic gray {noun3}\
towering above my head. Feeding that animal made me hungry. I went to get a {adjective3}\
scoop of ice cream. It filled my stomach. Afterwards I had to {verb} {adverb2}\
to catch our bus. When I got home I {past_verb2} my mom for a {adjective4} day at the zoo"
print(line1)