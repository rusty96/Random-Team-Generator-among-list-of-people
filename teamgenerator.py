#For a even number of people
import random
people = [] #Enter the names of people in the list, suppose 4 people are playing, enter 4 persons name in the list
teamA = [] #let this list be empty creating two teams
teamB = []

for i in range(2):
    one = random.choice(people)
    teamA.append(one)
    people.remove(one)

    two = random.choice(people)
    teamB.append(two)
    people.remove(two)
   
print('Alpha', teamA)
print('Butterfly', teamB)
