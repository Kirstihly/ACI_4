import sys
import importlib
from time import sleep
import random


def slow_print(str):
    words = str.split()
    for word in words:
        for letter in word:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.05)
        sys.stdout.write(" ")
        sys.stdout.flush()
    print("")



slow_print("Hello! I am an intelligent mac poet!")
slow_print("I will randomly pick a season and compose a poem.")
slow_print(".....")
slow_print("....")
slow_print("...")
season = random.choice(["spring", "summer", "fall", "winter"])
slow_print("This is {} season.".format(season))
if (season == "spring"):
    slow_print("Well, I will have the probability of 20% to hate it...")
    life_prob = 0.8
elif (season == "summer"):
    slow_print("Well, I will have the probability of 40% to hate it...")
    life_prob = 0.6
elif (season == "fall"):
    slow_print("Well, I will have the probability of 50% to hate it...")
    life_prob = 0.5
elif (season == "winter"):
    slow_print("Well, I will have the probability of 90% to hate it...")
    life_prob = 0.1
else:
    slow_print("Although I am intelligent, I do not know that season. ")
    exit;
slow_print(".....")
slow_print("....")
slow_print("...")


class Mock(object):
    season = season

    def __getattribute__(self, name):
        if(name == "Fade"):
            if (season == "spring"):
                slow_print("Spring returns with snow thaw")
            elif (season == "summer"):
                slow_print("Heat wave returns with floret")
            elif (season == "fall"):
                slow_print("Fall returns with leaves fade")
            elif (season == "winter"):
                slow_print("Winter returns with snow flurry")
        if(name == "Ray"):
            slow_print("Gradient color from bright ray")
        if(name == "Pathway"):
            if (season == "summer"):
                slow_print("Steam the pathway")
            else:
                slow_print("Piercing winds penetrate pathway")
        if(name == "Fill"):
            slow_print("I enjoy the brief fill")
        if(name == "Place"):
            slow_print("I let go the common place")
        if(name == "View"):
            slow_print("Get strayed in the sunrise view")
        if(name == "Wind"):
            slow_print("Blows the wind")
        if(name == "Tree"):
            slow_print("Rustles the tree")
        if(name == "Squirrel"):
            slow_print("Sprints the squirrel")
        if(name == "Life"):
            slow_print("Lives the life")
        if(name == "Death"):
            slow_print("Comes the death")
        return Mock()

Fall, Gradient, I, Get, Blows, Rustles, Sprints, Lives, Comes, Piercing = [Mock()]*10

if(random.random()<life_prob):
    sys.modules["death"] = Mock()
    sys.modules["death.to"] = Mock()
    sys.modules["death.to.life"] = Mock()
    import life
else:
    sys.modules["life"] = Mock()
    sys.modules["life.to"] = Mock()
    sys.modules["life.to.death"] = Mock()
    import death
