def character_frequency(string):
    frequency = {}

    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

characters = "hello"
obj_character = character_frequency(characters)
for char, count in obj_character.items():
    print(f"Char: {char} counts: {count}")