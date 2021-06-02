# A basic madlib program
# Takes input form user and then creates a madlib and prints it to the screen.

ing_verb = input("A verb ending in 'ing': ")
body_part_1 = input("A part of the body: ")
body_part_2 = input("A part of the body: ")
body_part_3 = input("A part of the body: ")
plural_noun_1 = input("A plural noun: ")
plural_noun_2 = input("A plural noun: ")
plural_noun_3 = input("A plural noun: ")
plural_noun_4 = input("A plural noun: ")
verb_1 = input("A verb: ")
noun_1 = input("A noun")
noun_2 = input("A noun")
noun_3 = input("A noun")
place_1 = input("A place")
adverb_1 = input("An adverb")


title = "\n\nHave you always wondered what it\'s like to be a dog?\n\n"

madlib1 = f"7:00 a.m.: I wake up and my tummy is jumping. I bug my human by {ing_verb} her {body_part_1} until I get some {plural_noun_1}.\n"
madlib2 = f"7:30 a.m.: Potty time! My human takes me outside to {verb_1} on a/an {noun_1}.\n"
madlib3 = f"8:00 a.m.: My human leaves to go to (the) {place_1}. I am sad and pout {adverb_1}\n"
madlib4 = f"9:00 a.m.: Naptime. I cuddle on my favorite {noun_2} and dream about chasing {plural_noun_2}.\n"
madlib5 = f"6:00 p.m.: MY HUMAN IS HOME! FINALLY! I wag my {body_part_2} back and forth, and give my human kisses on the {body_part_3}.\n"
madlib6 = f"6:30 p.m.: My human takes me for a walk, and I sniff lots of {plural_noun_3}.\n"
madlib7 = f"7:00 p.m.: Dinnertime! Eating {plural_noun_4} is my favorite!\n"
madlib8 = f"9:00 p.m.: I snuggle up next to my human and fall asleep, happy as a/an {noun_3}."

print(title)
print(madlib1+madlib2+madlib3+madlib4+madlib5+madlib6+madlib7+madlib8)
