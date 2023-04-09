from pgmpy.readwrite import BIFReader
from pgmpy.inference import VariableElimination

reader = BIFReader("asia.bif")
model = reader.get_model()
variables = model.nodes


def determine_parents(nodes):
    parents = []
    for current_node in nodes:
        parents.extend(model.get_parents(current_node))
        parents.extend(determine_parents(parents))
    return parents


# prompt for variable
while True:
    user_input = input("Which of the following variables should be calculated? \n\n"
                       + "\n".join(variables) + "\n\n").lower()
    if user_input in variables:
        all_parents = list(set(determine_parents([user_input])))
        break
    else:
        print("invalid input, try again!")

# prompt for options
evidence = {}
for node in all_parents:
    cpd = model.get_cpds(node)
    options = cpd.state_names.get(node)
    while True:
        value = input(f"Provide evidence for {node}: " + ", ".join(options) + " or skip with \"skip\"\n").lower()
        if value == "skip":
            break
        if value in options:
            evidence[node] = value
            break
        else:
            print("Invalid option, try again")

print(VariableElimination(model).query([user_input], evidence))
