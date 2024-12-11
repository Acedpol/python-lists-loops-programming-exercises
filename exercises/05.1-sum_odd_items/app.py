my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
is_odd = lambda n: n % 2 != 0
sum_odds = 0
for e in my_list:
    if (is_odd(e)):
        sum_odds += e

print(sum_odds)