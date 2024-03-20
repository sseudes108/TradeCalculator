import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

random_string = generate_random_string(27)
print("String aleatória:", random_string)