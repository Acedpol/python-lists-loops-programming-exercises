names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
names[1] = "Steven"
names[-1] = "Pepe"
names[0] = names[2] + names[4]

for i in range(0,len(names)):
    print(names[len(names)-(i+1)])