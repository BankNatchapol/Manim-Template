from manim import *

class Getters(Scene):
    def construct(self):

        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        arrow = always_redraw(
                lambda: Line(start=rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip()
        )

        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait(1.0)
        self.play(rect.animate.to_edge(UR))
        self.wait(1.0)
        self.clear()