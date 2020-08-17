agents = { "Mulder", "Scully", "Doggett", "Reyes" }

# agents.remove("Doggett")
# print(agents)

# agents.remove("Skinner")
# print(agents)

agents.discard("Dogget")
print(agents)

element = agents.discard("Skinner")
print(agents)
print(element)