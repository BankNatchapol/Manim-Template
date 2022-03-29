from manim import *
from Introduction import * 
from Images import * 

class MultipleScenes(Scene):
    def construct(self):
        Introduction.construct(self)
        Images.construct(self)
        self.clear()