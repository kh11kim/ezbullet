import numpy as np
from ezpose import SE3, SO3
import ezbullet as eb 

def setup_function():
    global world
    world = eb.World(gui=False)

def test_load_world():
    pass