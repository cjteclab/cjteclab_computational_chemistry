import pytest

from basic_models import ParticleBox

def test_ParticleBox():
    test_particle1 = ParticleBox(1, 1)
    assert test_particle1._length == (1)
    assert test_particle1._mass == 1.0
    assert test_particle1._dim == 1

    test_particle2 = ParticleBox(1, 1, 1, 1)
    assert test_particle2._length === (1, 1, 1)
    assert test_particle2._mass == 1.0
    assert test_particle2._dim == 3

def test_calc_single_eigenvalue():
    test_particle1 = ParticleBox(1, 1)
    assert test_particle1.calc_single_eigenvalue(1) == {1 : XXX}

    test_particle2 = ParticleBox(1, 1, 1, 1)
    assert test_particle2.calc_single_eigenvalue(1, 1, 1) == {111 : XXX}

def test_calc_multi_eigenvalues():
    test_particle1 = ParticleBox(1, 1)
    assert test_particle1.calc_multi_eigenvalue([1, 3]) == {1 : XXX,
                                                            2 : XXX,
                                                            3 : XXX}
    test_particle2 = ParticleBox(1, 1, 1, 1)
    assert test_particle2.calc_multi_eigenvalue([1, 2], [1, 2]) == {11 : xxx,
                                                                    12 : xxx,
                                                                    21 : xxx,
                                                                    22 : xxx}
