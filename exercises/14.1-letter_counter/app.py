par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
lower_string = par.lower()
without_spaces = lower_string.replace(' ','')
print(without_spaces)

for let in without_spaces:
    if let not in counts:
        counts[let] = 1
    else:
        counts[let] += 1

print(counts)
