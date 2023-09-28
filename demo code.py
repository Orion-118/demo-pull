import random as rand

#random function does not take any parameter
random_num = rand.random()

#but if you want to then use randint
random_range = rand.randint(1,10)

#now lets do some calculations using this random number
passowrd = str(random_range) + " hello i am random"

print(random_num, random_range)
