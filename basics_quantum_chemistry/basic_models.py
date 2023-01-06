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
        >>> eigenvalue_a = new_ParticleBoxA._calc_eigenvalue(1, 1, 1)
        >>> print(eigenvalue_a)
        1.6464302112270383e-67

        Second Example
        >>> new_ParticleBoxB = ParticleBox(1, 2, 2, 2)
        >>> eigenvalue_b = new_ParticleBoxB._calc_eigenvalue(1, 1, 1)
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
        >>> eigenvalues_a = new_ParicleBoxA.calc_eigenvalues()
        >>> print(eigenvalues_a)
        {(1, 0, 0): 5.488100704090127e-68}

        Second Example
        >>> new_ParticleBoxB = ParticleBox(1, 2, 2, 2)
        >>> eigenvalues_b = new_ParticleBoxB.calc_eigenvalues([1 , 3])
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
                    eigenvalues[i, j, k] = self._calc_eigenvalue(i, j, k)
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
                                   in eigenvalues.items()
                                   if value == i]
            degeneracy.append([i,
                                len(same_quantum_states),
                                same_quantum_states])
        return degeneracy

    # Draw different plots of a one-dimensional particle in a box

    def plot_eigenvalues(self,
                         n_x: List = [1, 1],
                         n_y: List = [1, 1],
                         n_z: List = [1, 1]):
        eigenvalues = self.calc_eigenvalues(n_x, n_y, n_z)
        degeneracy = self.determine_degeneracy(eigenvalues)
        fig, ax = plt.subplots(layout='constrained')
        for level in degeneracy:
            ax.axhline(level[0], xmin=0, xmax=0.4)
            ax.text(1, level[0], str(level[2]), ha='right', va='center')
        # Style settings
        ax.set_xticks([0, 1], [0, 'a'])
        ax.set_xlabel('length')
        ax.set_ylabel(r'$E_n[eV]$')
        ax.set_title('Eigenvalues')
        plt.show()

    # Draw wavefunctions
    def _calc_wavefunction(self, n_x: int, n_y: int, x: int, y: int):
        """Calculate the wavefunction for given principle quantun numbers.

        Attention: Because of spatial limitation only 1D and 2D wavefunctions
        can be calculted.

        Parameters
        ----------
        n_x, n_y : int
            Priniciple quantum numbers for spatial directions x and y.
        x, y : int
            Values for the x-axis and the y-axis.

        Returns
        -------
        float
            Value for the z-axis.
        """
        return (np.sqrt(4 / self.length_x * self.length_y)
                * np.sin(n_x * np.pi * x / self.length_x)
                * np.sin(n_y * np.pi * y / self.length_y))

    def plot_wavefunctions(self,
                           n_x: list = [1,1],
                           n_y: list = [1,1]):
        """Plot wavefunctions for principle quantum numbers n_x and n_y.

        Parameters
        ----------
        n_x, n_y : list of int
            principle quantum numbers, with n = 1, 2, 3, ...
        """
        if n_y
            pass
        else:

    def _plot_1D_wavefuntion(self,
                             n_x: List):


    def _plot_2D_wavefunction(self,
                              n_x: List,
                              n_y: List):
        x_values = np.linspace(0.0, self.length_x, 100)
        y_values = np.linspace(0.0, self.length_y, 100)
        for i in range(n_x[0], n_x[1]+1):
            for j in range(n_y[0], n_y[1]+1):
                X, Y = np.meshgrid(x_values, y_values)
                Z = self._calc_wavefunction(i, j, X, Y)
                ax = plt.figure().add_subplot(projection='3d')
                ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5,
                                rstride=8, cstride=8, alpha=0.3)
                ax.contour(X, Y, Z, zdir='z', offset=-2, cmap='coolwarm')
                ax.contour(X, Y, Z, zdir='x', offset=-0.1, cmap='coolwarm')
                ax.contour(X, Y, Z, zdir='y', offset=1.3, cmap='coolwarm')
                plt.show()
