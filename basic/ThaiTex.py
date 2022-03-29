from manim import *


class ThaiTex(Scene):
    def construct(self):
        name = Text("สวัสดีครับ")
        box = SurroundingRectangle(name, buff=0.5)
        self.play(Write(name))
        self.play(Create(box))
        self.wait(2.0)
        self.clear()