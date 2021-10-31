import random

descriptor = "Salted"
noun = "NPC"
new_name = descriptor + noun
# print(new_name)

descriptor_pool = ["Tactical", "Sweet", "Leet", "Salty", "Fire", "Toxic", "Icy", "Based", "Nuclear", "Zombie", "Zooming", "Darth", "Sneaky", "Happy"]

noun_pool = ["Bread", "Pepe", "Donut", "Kirby", "Mew", "Boba", "Matcha", "Vader", "Cat", "Patriot", "Lychee", "Durian", "Rebel", "NPC", "Squid"]

# access array values
# print(descriptor_pool[0]) # Tactical
# print(descriptor_pool[3]) # Salty

# new_name = descriptor_pool[8] + noun_pool[3] # Toxic Kirby
# print(new_name)

# how to get length of an array/list ?
descriptor_length = len(descriptor_pool)
# print(descriptor_length)
# print(descriptor_pool[descriptor_length - 1]) # Icy

# how to get a random number between a specified range ?
# random.randrange(0, 101, 2)    # Even integer from 0 to 100 inclusive
# print(random.randrange(0,descriptor_length,1))

random_desc = random.randrange(0,descriptor_length,1)
random_noun = random.randrange(0,len(noun_pool),1) # inline function call versus setting to a variable then using variable in function
print(descriptor_pool[random_desc] + noun_pool[random_noun])