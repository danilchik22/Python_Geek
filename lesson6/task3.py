import sys
import itertools

dict_people = {}
with open("People.txt", "r", encoding="utf-8") as file_people:
    with open("Hobby.txt", "r", encoding="utf-8") as file_hobby:
        people = file_people.readlines()
        hobbies = file_hobby.readlines()
        hobbies = [line.rstrip() for line in hobbies]
        if len(people) > len(hobbies):
            dict_people = {person.rstrip(): hobby for person, hobby in itertools.zip_longest(people, hobbies)}
        elif len(people) == len(hobbies):
            dict_people[line_people.rstrip()] = line_hobby.rstrip()
        else:
            sys.exit([1])
print(dict_people)
