from manim import *


class Introduction(Scene):
    def construct(self):
        name = Tex("Bank")
        box = SurroundingRectangle(name, buff=0.5)
        self.play(Write(name))
        self.play(Create(box))
        self.wait(2.0)