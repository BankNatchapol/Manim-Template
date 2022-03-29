from manim import *

HOME = ".\images"

class Images(Scene):
    def construct(self):
        self.camera.background_color = BLUE
        icon = SVGMobject(f"{HOME}\\cat.svg").shift(LEFT * 2)
        im = ImageMobject(f"{HOME}\\dog.png").shift(RIGHT * 2)
        icon.height = 3
        icon.width = 3
        im.height = 5
        im.width = 5
        self.play(DrawBorderThenFill(icon), FadeIn(im))
        self.wait(3.0) 
        self.clear()       