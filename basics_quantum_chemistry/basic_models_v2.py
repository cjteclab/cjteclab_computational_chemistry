from typing import List, Tuple, Dict, Set
import itertools
from scipy import constants

class ParticleBox_1D():
    def __init__(self,
                 mass,
                 length):
        self._mass = mass
        self._length = length
    
    def calc_single_eigenvalue(self,
                               n: int) -> float:
        return ((constants.h**2 / (8 * self._mass))
                * (n ** 2 / self._length ** 2))
    
    def calc_multi_eigenvalues(self,
                              n: Tuple) -> Dict:
        eigenvalues = {}
        for i in range(n[0], n[1] + 1):
            eigenvalues[i] = self.calc_single_eigenvalue(i)
        return eigenvalues
    
    def plot_eigenvalues(self, eigenvalues: dict):
        pass
    
    def _calc_wavefunction(self, n):
        pass
    
    def plot_single_wavefunction(self, n: int):
        pass
    
    def plot_wavefunctions(self, eigenvalues: dict):
        pass
    
class ParticleBox_multiD():
    def __init__(self,
                 mass,
                 length: Tuple):
        self._mass = mass
        self._length = length
        
    def calc_single_eigenvalue(self,
                               n: Tuple) -> Dict:
        eigenvalue = 0
        for spatial_n, spatial_length in zip(n, self._length):
            eigenvalue += ((constants.h ** 2 / (8 * self._mass)) 
                           * ((spatial_n ** 2 / spatial_length ** 2)))
            
        return eigenvalue
    
    def calc_multi_eigenvalues(self,
                               *n_i: Tuple) -> Dict:
        eigenvalues = {}
        for i in itertools.product(*[range(n_spatial[0], n_spatial[1] + 1)
                                     for n_spatial in n_i]):
            eigenvalues[i] = self.calc_single_eigenvalue(i)
        return eigenvalues

    def _determine_discrete_eigenvalues(self, eigenvalues: Dict) -> Set:
        return sorted({value for value in eigenvalues.values()})
    
    def determine_degeneracy(self, eigenvalues: Dict) -> Dict:
        degeneracy = []
        # Determine discrete eigenvalues for searching degenerated eigenvalues
        discrete_eigenvalues = self._determine_discrete_eigenvalues(eigenvalues)
        for i in discrete_eigenvalues:
            same_quantum_states = [state for state, value
                                   in eigenvalues.items() if value == i]
            degeneracy.append([i,
                               len(same_quantum_states),
                               same_quantum_states])
        return degeneracy
    
    def plot_eigenvalues(self, eigenvalues: dict):
        pass
    
class ParticleBox_2D(ParticleBox_multiD):
    def _calc_wavefunction(self, n: Tuple):
        pass
    
    def plot_single_wavefunction(self, n: Tuple):
        pass
    
    def plot_wavefunctions(self, eigenvalues: dict):
        pass
    
    
class ParticleBox_3D(ParticleBox_multiD):
    pass