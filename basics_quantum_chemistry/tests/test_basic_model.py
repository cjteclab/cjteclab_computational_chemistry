import pytest

from basic_models import calc_eigenvalues

@pytest.mark.parametrize('n_x, n_y, n_z, expected',
                         [(1, None, None, XXX),     # specific n in 1D
                          (4, None, None, XXX),     # specific n in 1D
                          (2, 2, None, XXX),        # specific n in 2D
                          (3, 2, 1, XXX),           # specific n in 3D
                          ((1,3), None, None, XXX), # range of n in 1D
                          ((1,2), (1,2), None, XXX),# range of n in 2D
def test_calc_eigenvalues(n_x, n_y, n_z, expected):
    test_particle = main.ParticleBox()
    assert test_particle.calc_eigenvalues(n_x, n_y, n_z) == expected
