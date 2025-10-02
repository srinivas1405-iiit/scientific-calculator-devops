import pytest
import math
from calculator import ScientificCalculator

class TestScientificCalculator:
    """Test cases for Scientific Calculator"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.calc = ScientificCalculator()
    
    # Square Root Tests
    def test_square_root_positive(self):
        """Test square root of positive numbers"""
        assert self.calc.square_root(4) == 2.0
        assert self.calc.square_root(9) == 3.0
        assert self.calc.square_root(16) == 4.0
    
    def test_square_root_zero(self):
        """Test square root of zero"""
        assert self.calc.square_root(0) == 0.0
    
    def test_square_root_negative(self):
        """Test square root of negative number raises error"""
        with pytest.raises(ValueError):
            self.calc.square_root(-4)
    
    # Factorial Tests
    def test_factorial_positive(self):
        """Test factorial of positive integers"""
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(10) == 3628800
    
    def test_factorial_negative(self):
        """Test factorial of negative number raises error"""
        with pytest.raises(ValueError):
            self.calc.factorial(-5)
    
    def test_factorial_non_integer(self):
        """Test factorial of non-integer raises error"""
        with pytest.raises(ValueError):
            self.calc.factorial(5.5)
    
    # Natural Logarithm Tests
    def test_natural_log_positive(self):
        """Test natural logarithm of positive numbers"""
        assert round(self.calc.natural_log(1), 2) == 0.0
        assert round(self.calc.natural_log(math.e), 2) == 1.0
        assert round(self.calc.natural_log(10), 2) == 2.30
    
    def test_natural_log_zero(self):
        """Test natural log of zero raises error"""
        with pytest.raises(ValueError):
            self.calc.natural_log(0)
    
    def test_natural_log_negative(self):
        """Test natural log of negative number raises error"""
        with pytest.raises(ValueError):
            self.calc.natural_log(-5)
    
    # Power Tests
    def test_power_positive(self):
        """Test power function with positive numbers"""
        assert self.calc.power(2, 3) == 8.0
        assert self.calc.power(5, 2) == 25.0
        assert self.calc.power(10, 0) == 1.0
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent"""
        assert self.calc.power(2, -1) == 0.5
        assert self.calc.power(10, -2) == 0.01
    
    def test_power_fractional(self):
        """Test power with fractional exponent"""
        assert self.calc.power(4, 0.5) == 2.0
        assert round(self.calc.power(27, 1/3), 2) == 3.0
