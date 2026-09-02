inputs = ["Name - ", "Animal - ", "Object - ", "Verb - ", "Food - "]
outputs = []

for i in range(len(inputs)):
    outputs.append(input(inputs[i]))

print()

print("One day, {} was walking down the street when they saw a {} sitting on top of a {}.".format(outputs[0], outputs[1], outputs[2]))
print("\"WHAT are you doing?\" {} shouted.".format(outputs[0]))
print("The animal suddenly {} toward them and dropped a giant plate of {} right at their feet.".format(outputs[3], outputs[4]))
print("Without thinking, {} picked it up and took a bite.".format(outputs[0]))
print("That’s when the {} whispered, \"You have made a terrible mistake.\"".format(outputs[1]))
print("{} froze.".format(outputs[0]))
print("Then the {} pulled out a tiny briefcase and said, \"We need to talk.\"".format(outputs[1]))
print("And that is how [A name] accidentally became the most wanted {} smuggler in the entire city.".format(outputs[0], outputs[4]))