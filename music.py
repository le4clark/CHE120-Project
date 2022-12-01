import random, pygame, sys

class music:
    def __init__(self):


        randInt = random.randrange(0,101)
        #2% chance to play magnolia eclair ~MA
        if randInt <= 2:
            """
            This is Magnolia Eclair from Guilty Gear Xrd. I thought adding an actual good song
            (compared to Geese theme) and only playing very rarely would be funny
            ~MA
            """
            song = pygame.mixer.music.load("magnolia_eclair.mp3")
            #sets the volume ~MA
            pygame.mixer.music.set_volume(0.30)
        else:
            """
            Geese theme is an arangment of Guile's Theme from Street Fighter 2 where I 
            randomly pitched everything and changed most of the instruments to recorders
            ~MA
            """
            song = pygame.mixer.music.load("geeslstheme.wav")
            #sets the volume ~MA
            pygame.mixer.music.set_volume(0.50)
        
        
        #plays the song ~MA
        pygame.mixer.music.play(5)
        
        
