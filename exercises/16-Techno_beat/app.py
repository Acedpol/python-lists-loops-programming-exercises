def lyrics_generator(data):
    lyrics = ""
    combo = 0 # three 1s in a row
    
    for let in data:
        if let == 0:
            lyrics += "Boom "
            combo = 0
        elif let == 1:
            lyrics += "Drop the bass "
            combo += 1

            # adicionalmente si hay tres seguidos
            if combo == 3:
                lyrics += "!!!Break the bass!!! "
                combo = 0

    return lyrics

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
