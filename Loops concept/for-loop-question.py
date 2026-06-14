# Program: The current population of a town is 10,000. The population of the town is increasing at the rate of 10% per year. Write a program to find
#          the population at the end of each of the last 10 years.

curr_pop=10000
for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop= curr_pop /1.1

   