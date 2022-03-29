from manim import *

class ValueTrackers(Scene):
    def construct(self):

        k = ValueTracker(0)

        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))
       
        self.wait(0.5)
        self.play(FadeIn(num))
       
        self.play(k.animate.set_value(10), run_time=10, rate_func=linear)
        self.wait(1)
        self.clear()