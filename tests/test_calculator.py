import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    def test_add(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
    
    def test_subtract(self, calc):
        assert calc.subtract(5, 2) == 3
        assert calc.subtract(0, 5) == -5
    
    def test_multiply(self, calc):
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-2, 3) == -6
    
    def test_divide(self, calc):
        assert calc.divide(6, 2) == 3
        with pytest.raises(ValueError):
            calc.divide(1, 0)