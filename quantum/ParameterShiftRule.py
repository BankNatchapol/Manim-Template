from manim import *
import pennylane as qml
from pennylane import numpy as np

x = np.linspace(-np.pi, np.pi, 100)

dev = qml.device("default.qubit", wires=1)
@qml.qnode(dev)
def function(var):
  qml.RX(var, wires=0)
  return qml.expval(qml.PauliZ(0))

def slope_point(ax, point, length):
    slope = (function(point+np.pi/2)-function(point-np.pi/2))/np.pi
    slope_ps = slope*np.pi/2
    a = ax.c2p(point+length, slope_ps*(length)+function(point))
    b = ax.c2p(point-length, slope_ps*(-length)+function(point))
    return [a, b]

class ParameterShiftRule(Scene):
    def construct(self):

        k = ValueTracker(-1.2)

        ax = (
            Axes(x_range=[-4,4,1], y_range=[-1.5,2,0.5], x_length=10, y_length=6)
            .to_edge(DOWN)
            .add_coordinates()
        ).set_color(WHITE)

        func = ax.plot(function, x_range=[-np.pi, np.pi], color=BLUE)

        
        pt = always_redraw(
            lambda: Dot().move_to(
                ax.c2p(k.get_value(), func.underlying_function(k.get_value()))
            )
        )
        
        slope = always_redraw(  
            lambda: DashedLine(slope_point(ax, k.get_value(), 1)[0], slope_point(ax, k.get_value(), 1)[1])
        )
        psp = always_redraw(
            lambda: Dot().move_to(
                ax.c2p(k.get_value()+np.pi/2, func.underlying_function(k.get_value()+np.pi/2))
            )
        )
        psn = always_redraw(
            lambda: Dot().move_to(
                ax.c2p(k.get_value()-np.pi/2, func.underlying_function(k.get_value()-np.pi/2))
            )
        )

        
        line = always_redraw(
            lambda: Line(start=psp.get_center(), end=psn.get_center())
        )
        

        self.add(ax, func, pt, psp, psn, line, slope)
        self.wait()
        self.play(k.animate.set_value(1.2), run_time=5, rate_func=linear)
        self.wait()
        self.clear()