"""Basic Models in Qunatum Chemistry

This module contains different basic models of quantum mechanics and quantum
chemistry. 

Content:
    - Particle in a Box: ParticleBox
"""
from typing import Dict, List
from scipy import constants


class ParticleBox():
    def __init__(self,
                 mass: float = 1.0,
                 length_x: float = 1.0,
                 length_y: float = 1.0,
                 length_z: float = 1.0):
        self.mass = mass
        self.length_x = length_x
        self.length_y = length_y
        self.length_z = length_z


    def calc_eigenvalue(self,
                        n_x: int,
                        n_y: int,
                        n_z: int) -> float:
        """Calculate a single eigenvalue of a particle in a box.

        Parameters
        ----------
        n_x : int
            The length in 
        return ((constans.h**2 / (8 * self.mass))
                * ((n_x/self.length_x)**2
                   + (n_y/self.length_y)**2
                   + (n_z/self.length_z)**2))

    def calc_n_eigenvalues(self,
                           n_x: List = [1, 1],
                           n_y: List = [0, 0],
                           n_z: List = [0, 0]) -> Dict:
        self.eigenvalues = {}
        for i in range(n_x[0], n_x[1]+1):
            for j in range(n_y[0], n_y[1]+1):
                for k in range(n_z[0], n_z[1]+1):
                    self.eigenvalues[i, j, k] = self.calc_eigenvalue(i, j, k)
        return self.eigenvalues

if __name__ == '__main__':
