import random

LENGTH = int(input("Enter the length of password: "))  # minimum length is 5

UPPER_CHAR_REQUIRED = True if input(
    "Require upper characters? (-y) ").lower() == 'y' else False
LOWER_CHAR_REQUIRED = True if input(
    "Require lower characters? (-y) ").lower() == 'y' else False
NUMERIC_CHAR_REQUIRED = True if input(
    "Require numeric characters? (-y) ").lower() == 'y' else False
SPECIAL_CHAR_REQUIRED = True if input(
    "Require special characters? (-y) ").lower() == 'y' else False

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
UPPER_CHARACTERS = [chr(i) for i in range(65, 91)]
LOWER_CHARACTERS = [chr(i) for i in range(97, 123)]
NUMERIC_CHARACTERS = [str(i) for i in range(0, 10)]

password = ''
must_have = 0
char_pool = []
if UPPER_CHAR_REQUIRED:
    char_pool.append(UPPER_CHARACTERS)
    must_have += 1
if LOWER_CHAR_REQUIRED:
    char_pool.append(LOWER_CHARACTERS)
    must_have += 1
if SPECIAL_CHAR_REQUIRED:
    char_pool.append(SPECIAL_CHARACTERS)
    must_have += 1
if NUMERIC_CHAR_REQUIRED:
    char_pool.append(NUMERIC_CHARACTERS)
    must_have += 1

for i in range(must_have):
    password += random.choice(char_pool[i])
for _ in range(LENGTH):
    password += random.choice(char_pool[random.randint(0, must_have-1)])

print(password)
