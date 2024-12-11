sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below
new_list = []
for i in range(len(sample_list)):
    new_list.append(sample_list[-(i+1)])
print(new_list)