# Possible Solutions:
## 1)

string = input()
length = len(string)
first_character = string[0]
last_character = string[length-1]
print("First character: " + first_character)
print("Last character: " + last_character)


## 2)

given_string = input()
number_of_characters = int(input())
result = given_string[:number_of_characters]
print(result)


## 3)

given_string = input()
skip_character_index = int(input())
first_part = given_string[:skip_character_index]
last_part = given_string[skip_character_index+1:]
print(first_part+last_part)
