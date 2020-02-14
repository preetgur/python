# import time


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# import pygame
# print("Version of pygame :",pygame.ver)


# play_music = input("Do you want to play sidhu music ? yes/no :")

# if play_music == "yes":
#     pygame.mixer.init()

#         # file = ['sidhu.mp3','sidhu.mp3']
#     pygame.init()
#         # pygame.mixer.music.load(file[0])
#     pygame.mixer.music.load('sidhu.mp3')
#     pygame.mixer.music.play()
#     pygame.event.wait()

# else:
#     print("Ok as your wish :")


from pygame import mixer
from datetime import datetime
from time import time

# def music_loop(file):
def music_loop(file,stopper):

    print("User enter this keyword :",stopper)
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper :
            mixer.music.stop()
            break
        else:
            print("Wrong Keyword")

def log_now(msg):
    with open("health_pygame.txt",'a') as f :
        f.write(f"{msg} {datetime.now()} \n")

if __name__ == "__main__":
    # music_loop("sidhu.mp3") 

    int_water = time()       # initialize the time
    int_eyes = time() 
    int_excercise = time() 

    # set the number of seconds after which the music is played
    water_seconds = 30*60 
    eye_seconds =  45*60
    excercise_seconds = 55*60 

    while True:
        if time() - int_water > water_seconds:
            print("please drink the water , and enter the drink keyword to stop :")
            music_loop('sidhu.mp3',"drink")
            int_water = time()
            log_now("Drink water at :")

        if time() - int_eyes > eye_seconds:
            print("please relax the eyes , and enter the eye keyword to stop :")
            music_loop('sidhu.mp3','eye')
            int_eyes = time()
            log_now("Eyes excersice at :")


        if time() - int_excercise > excercise_seconds:
            print("please do the physical activity , and enter the excercise keyword to stop :")
            music_loop('sidhu.mp3',"excercise")
            int_excercise = time()
            log_now("body excercise at :")            