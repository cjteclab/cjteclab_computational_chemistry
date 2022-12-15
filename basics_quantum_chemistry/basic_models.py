"""Basic Models in Qunatum Chemistry

This module contains different basic models of quantum mechanics and quantum
chemistry. 

Content:
    - Particle in a Box: ParticleBox
"""

def convert_unit(target_unit: str, number: float, unit: str) -> float:
    pass

class ParticleBox():
    """Represent a particle in a box.

    Parameters
    ----------
    lenght_x, length_y, length_z : float
        Length of the box in different spatial directions. Can be represent a
        one-dimensional box up to a three-dimensional box.
    mass : float, default=0.0
        Mass of the particle. Is needed to calculate the eigenvalues.
    """
    def __init__(self,
                 length_x: float,
                 length_y: float = 0.0,
                 length_z: float = 0.0,
                 mass: float = 0.0):
        self.length_x = length_x
        self.length_y = length_y
        self.length_z = length_z
        self.mass = mass

    def calc_n_eigenvalues(self,
                           n_x: int = 1,
                           n_y: int = 0,
                           n_z: int = 0) -> float:
        # return DictComprehension
        pass

# Instead of a ParticleBox class I can also use a Box class and a Particle
# class.

class Box():
    def __init__(self,
                 length_x: float,
                 length_y: float = 0.0,
                 length_z: float = 0.0,
                 mass: float = 0.0):
        self.length_x = length_x
        self.length_y = length_y
        self.length_z = length_z

class Particle():
    def __init__(self,
                 mass: float):
        self.mass = mass

class ParticleBox():
    def __init__(self,
                 particle: obj,
                 box: obj)
    self.particle = particle
    self.box = box

    def calc_n_eigenvalues(self,
                           n_x: List = [1, 1, 1],
                           n_y: List = [0, 0, 0],
                           n_z: List = [0, 0, 0]) -> float:
        self.eigenvalues = {}
        for i in range(n_x[0], n_x[1], n_x[2]):
            for j in range(n_y[0], n_y[1], n_y[2]):
                for k in range(n_z[0], n_z[1], n_z[2]):
                    self.eigenvalues[i, j, k] = calc_eigenvalue(i, j, k)


    def calc_eigenvalue(self,
                        n_x: int,
                        n_y: int,
                        n_z: int) -> float:
        return ((constans.h**2 / (8 * mass))
                * ((n_x/self.length_x)**2
                   + (n_y/self.length_y)**2
                   + (n_z/self.length_z)**2))
