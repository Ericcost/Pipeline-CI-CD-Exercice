# test_average.py
from average import moyenne

def test_moyenne_vide():
    assert moyenne([]) == 0

def test_moyenne_simple():
    assert moyenne([1, 2, 3, 4]) == 2.5

def test_moyenne_negatif():
    assert moyenne([-1, 1]) == 0
