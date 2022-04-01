from manim import *

class Surface3DLoop(ThreeDScene):

    video_duration = 30 # Edit this duration
    
    video_rate = 1.05*6 
  
    def func(self, u, v):
        return np.sin(u) * np.cos(v)

    def construct(self):
        axes = ThreeDAxes(x_range=[-3,3], y_range=[-3,3], x_length=6, y_length=6)
        surface = Surface(
            lambda u, v: axes.c2p(u, v, self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=32
        )

        self.set_camera_orientation(theta=45 * DEGREES, phi=60 * DEGREES)
        self.add(axes, surface)
        self.begin_ambient_camera_rotation(rate=self.video_rate/self.video_duration)
        self.wait(self.video_duration)