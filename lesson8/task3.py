#we need an algorithm to shuffle elements randomly
from random import shuffle

#get list of numbers 1-40 and shuffle them
numbers = list(range(1, 41))
shuffle(numbers)

#get first seven and store them in a new list. sort the new list
lotteryNums = numbers[:7]
lotteryNums.sort()

#print the elements and separate them with colon and space: ', '
print(*lotteryNums, sep=', ')

