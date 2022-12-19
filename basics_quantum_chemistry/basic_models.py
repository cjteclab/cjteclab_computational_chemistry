"""Basic Models in Qunatum Chemistry

This module contains different basic models of quantum mechanics and quantum
chemistry. 

Content:
    - Particle in a Box: ParticleBox
"""
from typing import Dict, List
from scipy import constants
from matplotlib import pyplot as plt

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
        n_x, n_y, n_z : int
            Principal quantum numbers up to a 3 dimensional box.

        Returns
        -------
        float
            Return the eigenvalue with particular principle quantum number.

        Examples
        --------
        >>> from typing import Dict, List
        >>> from scipy import constants

        First Example
        >>> new_ParticleBoxA = ParticleBox()
        >>> eigenvalue_a = new_ParticleBoxA.calc_eigenvalue(1, 1, 1)
        >>> print(eigenvalue_a)
        1.6464302112270383e-67


        Second Example
        >>> new_ParticleBoxB = ParticleBox(1, 2, 2, 2)
        >>> eigenvalue_b = new_ParticleBoxB.calc_eigenvalue(1, 1, 1)
        >>> print(eigenvalue_b)
        4.116075528067596e-68
        """
        return ((constants.h**2 / (8 * self.mass))
                * ((n_x/self.length_x)**2
                   + (n_y/self.length_y)**2
                   + (n_z/self.length_z)**2))

    def calc_n_eigenvalues(self,
                           n_x: List = [1, 1],
                           n_y: List = [0, 0],
                           n_z: List = [0, 0]) -> Dict:
        """Calculate n eigenvalues of a particle in a box and returns a Dict.

        Parameters
        ----------
        n_x, n_y, n_z : list of int
            Each spatial principle quantum number consist of [Start, Stop]
            As default values n_x is [1, 1]. The other two spatial principle
            quantum numbers are set to [0,0]. This gives the opportunity to
            calculate 1D boxes by default.

        Returns
        -------
        dict of {str : float}
            Return principle quantum numbers and the corresponding eigenvalue.

        Examples
        --------
        >>> from typing import Dict, List
        >>> from scipy import constants

        First Example
        >>> new_ParticleBoxA = ParticleBox()
        >>> eigenvalues_a = new_ParicleBoxA.calc_n_eigenvalues()
        >>> print(eigenvalues_a)
        {(1, 0, 0): 5.488100704090127e-68}

        Second Example
        >>> new_ParticleBoxB = ParticleBox(1, 2, 2, 2)
        >>> eigenvalues_b = new_ParticleBoxB.calc_n_eigenvalues([1 , 3])
        >>> print(eigenvalues_b)
        {(1, 0, 0): 1.3720251760225318e-68, (2, 0, 0): 5.488100704090127e-68,
         (3, 0, 0): 1.2348226584202787e-67}
        """
        self.eigenvalues = {}
        # TODO Change code that input single value represent a range. For
        # example range(1) should calculate n for 1. Right now it would
        # calucalte 0, instead user has always to write a list with start and
        # end point.
        for i in range(n_x[0], n_x[1]+1):
            for j in range(n_y[0], n_y[1]+1):
                for k in range(n_z[0], n_z[1]+1):
                    self.eigenvalues[i, j, k] = self.calc_eigenvalue(i, j, k)
        return self.eigenvalues

    def print_eigenvalues(self):
        """Print the eigenvalues of the particle in a box."""
        

if __name__ == '__main__':
