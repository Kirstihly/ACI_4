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

class Mock(object):
    def __getattribute__(self, name):
        if(name == "Fade"):
            slow_print("Fall returns with leaves fade")
        if(name == "Ray"):
            slow_print("Gradient color from bright ray")
        if(name == "Pathway"):
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


if __name__ == "__main__":
    
    if(random.random()<0.5):
        sys.modules["death"] = Mock()
        sys.modules["death.to"] = Mock()
        sys.modules["death.to.life"] = Mock()
        import life
    else:
        sys.modules["life"] = Mock()
        sys.modules["life.to"] = Mock()
        sys.modules["life.to.death"] = Mock()
        import death
