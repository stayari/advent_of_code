input_data = open("input6.txt", "r").read().split()
dict_tree = dict()

for i, orbit in enumerate(input_data):

    orbit = orbit.split(")")

    dict_tree[orbit[0]] = orbit[1]

print(dict_tree)