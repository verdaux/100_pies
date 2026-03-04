import random
import my_module

random_int = random.randint(1,10)
print(random_int)

print(my_module.fav)

random_floater = random.random() * 10
print(random_floater)

random_rando_float = random.uniform(1,10)
print(random_rando_float)

heads_or_tails = random.randint(1,2)
if heads_or_tails == 1:
    print("Heads")
elif heads_or_tails==2:
    print("Tails")

print(my_module.states)
print(my_module.states[1])

my_module.states[2] = "YO"
print(my_module.states)

my_module.states.extend(["YI","PO"])
my_module.states.append("II")
print(my_module.states)

print(my_module.dirty_dozen)