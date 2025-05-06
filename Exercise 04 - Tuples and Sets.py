my_colours = {"red", "green", "fuchsia"}

used_colours = ["red", "orange", "purple"]

for colour in used_colours:
    my_colours.add(colour)

print("my_colours:", my_colours)

interesting_colours = {"fuchsia", "turqoise"}

print("Common colours:", my_colours & interesting_colours)

print("Is 'brown' in my_colours?", "brown" in my_colours)

frozen_colours = frozenset(my_colours)
print("frozen_colours:", frozen_colours)

frozen_colours.add("brown") # This line will raise an Attribute Error