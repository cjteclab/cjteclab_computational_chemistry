"""Basic Models in Qunatum Chemistry

This module contains different basic models of quantum mechanics.

Content:
    - Particle in a Box: ParticleBox
"""
from typing import Dict, List, Set
from scipy import constants
from matplotlib import pyplot as plt
import numpy as np

class ParticleBox():
    """Representation of the model 'Particle in a Box'.

    Parameters
    ----------
    mass : float, default=1.0
        Mass [] of the particle.    # unit of the mass
        It is set by default to 1.0, because if user only want to print
        wavefuntions, no mass is needed.
    length_x, length_y, length_z : float, default = 1.0
        Length [] of the box. Up to three-dimensional boxes.

    Methods
    -------
    calc_eigenvalues()

    """
    def __init__(self,
                 mass: float = 1.0,
                 length_x: float = 1.0,
                 length_y: float = 1.0,
                 length_z: float = 1.0):
        self._mass = mass
        self._length_x = length_x
        self._length_y = length_y
        self._length_z = length_z


    def _calc_eigenvalue(self,
                         n_x: int,
                         n_y: int,
                         n_z: int) -> float:
        """Calculate a single eigenvalue of a particle in a box.

        Parameters
        ----------
        n_x, n_y, n_z : int
            Principal quantum numbers up to a three- dimensional box.

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
        >>> new_ParticleBoxB = ParticleBox()
        >>> eigenvalue_b = new_ParticleBoxB.calc_eigenvalue(2, 2, 2)
        >>> print(eigenvalue_b)
        4.116075528067596e-68
        """
        return ((constants.h**2 / (8 * self._mass))
                * ((n_x/self._length_x)**2
                   + (n_y/self._length_y)**2
                   + (n_z/self._length_z)**2))

    def calc_eigenvalues(self,
                           n_x: List = [1, 1],
                           n_y: List = [0, 0],
                           n_z: List = [0, 0]) -> Dict:
        """Calculate n eigenvalues of a particle in a box and returns a Dict.

        Parameters
        ----------
        n_x, n_y, n_z : list of int

            Each spatial principle quantum number consist of [Start, Stop]
            As default values n_x is [1, 1]. The other two spatial principle
            quantum numbers are set to [0,0]. This makes it possible to
            calculate 1D boxes by default.

        Returns
        -------
        dict of {str : float}
            Dictionary items consist of principle quantum number and
            corresponding eigenvalue.

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
        eigenvalues = {}
        # TODO Change code that input single value represent a range. For
        # example range(1) should calculate n for 1. Right now it would
        # calucalte 0, instead user has always to write a list with start and
        # end point. Additionally user have to write a list (1,1), if he only wants
        # to calculate one eigenvalue.
        # Use a genetator.
        for i in range(n_x[0], n_x[1]+1):
            for j in range(n_y[0], n_y[1]+1):
                for k in range(n_z[0], n_z[1]+1):
                    self.eigenvalues[i, j, k] = self.calc_eigenvalue(i, j, k)
        return eigenvalues


    def determine_discrete_eigenvalues(self, eigenvalues: Dict) -> Set:
        """Returns sorted set of discrete eigenvalues.

        Parameters
        ----------
        eigenvalues : dict of {set of int : float}
            Items represent eigenstate with eigenvalues.

        Returns
        -------
        set of floats
            Different discrete eigenvalues.
        """
        return sorted({value for value in eigenvalues.values()})


    def determine_degeneracy(self, eigenvalues: Dict) -> Dict:
        """Determine list of degenerated eigenvalues.

        Parameters
        ----------
        eigenvalues : dict of {set of int : float}
            Items represent eigenstate with eigenvalue.

        Returns
        -------
        list of (float, int, list of tuple of int)
            list consist of: eigenvalue, degree of degeneracy, list of set of
            degenerated eigenstates
        """
        degeneracy = []
        discrete_eigenvalues = self.determine_discrete_eigenvalues(eigenvalues)
        for i in discrete_eigenvalues:
            same_quantum_states = [state for state, value
                                   in self.eigenvalues.items()
                                   if value == i]
            self.degeneracy.append([i,
                                len(same_quantum_states),
                                same_quantum_states])
        return self.degeneracy

    # Draw different plots of a one-dimensional particle in a box
    def _calc_wavefunction(self, n_x: int, n_y: int):
        """Calculate the wavefunction for given principle quantun numbers.

        Attention: Because of spatial limitation only 1D and 2D wavefunctions
        can be calculted.

        Parameters
        ----------
        n_x, n_y : int
            Priniciple quantum numbers for spatial directions x and y.

        Returns
        -------
        float
            z-value of the wavefunction.
        """
        return (np.sqrt(4 / self.length_x * self.length_y)
                * np.sin(n_x * np.pi * x / self.length_x)
                * np.sin(n_y * np.pi * y / self.length_y))

