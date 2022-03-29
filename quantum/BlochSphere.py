from manim import *
import numpy as np

def get_spherical_coordinates(statevector):
    # Convert to polar form:
    r0 = np.abs(statevector[0])
    phi0 = np.angle(statevector[0])

    r1 = np.abs(statevector[1])
    phi1 = np.angle(statevector[1])

    # Calculate the coordinates:
    r = np.sqrt(r0 ** 2 + r1 ** 2)
    theta = 2 * np.arccos(r0 / r)
    phi = phi1 - phi0
    x	=	r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    return [x, y, z]

#Manim Example | How to Show Sphere in Manim 
class BlochSphere(ThreeDScene):
    CONFIG = {
          "x_axis_label": "$x$",
          "y_axis_label": "$y$",
          "z_axis_label": "$z$",
          "basis_i_color": GREEN,
          "basis_j_color": RED,
          "basis_k_color": GOLD
    }
    
    def construct(self):
        H_AXIS: np.ndarray = np.array((np.sin(np.pi/4), 0, np.cos(np.pi/4)))

        ### calculate state
        start_state = np.array([1, 0])
        gate = (1/np.sqrt(2))*np.array([[1, 1],
                                        [1, -1]])
        target_state = start_state@gate
        gate = np.array([[np.exp(-complex(0,1)*np.pi/4), 0],
                        [0, np.exp(complex(0,1)*np.pi/4)]])
        target_state = target_state@gate
        
        

        ###


        scale_value = 3.0
        axes = ThreeDAxes(x_range=np.array([-4, 4, 1]),y_range=np.array([-4, 4, 1]),
                          z_range=np.array([-4, 6, 1]), depth=3,
                          axis_config={
                              "stroke_width":1,
                              "include_ticks":False,
                          })
        axes.add(axes.get_axis_labels())
        labelz = axes.get_z_axis_label(Tex("$z$"))
        self.set_camera_orientation(theta=45*DEGREES, phi=60*DEGREES, gamma=0*DEGREES)

        sphere = Sphere(radius=1.0, resolution=(25,25), color=BLUE).set_opacity(0.2).scale(scale_value)
        v1 = Vector(np.array([0, 0, scale_value]), color=RED)
        v2 = np.array(get_spherical_coordinates(target_state))*scale_value
        target_vector = Vector(v2, color=RED)
        self.add(axes, labelz, sphere, v1)
        self.wait()
        #self.play(Transform(v1, target_vector), run_time=3)
        self.play(v1.animate.rotate_about_origin(180*DEGREES, H_AXIS), run_time=3)
        self.wait()
        self.clear()