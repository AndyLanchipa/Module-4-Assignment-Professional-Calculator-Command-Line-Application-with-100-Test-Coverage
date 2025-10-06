"""
Test module for operation classes.
"""

import pytest
from decimal import Decimal
from app.operation import Addition, Subtraction, Multiplication, Division, Operation


class TestAddition:
    """Test cases for Addition operation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Addition()
    
    @pytest.mark.parametrize("a, b, expected", [
        (Decimal('5'), Decimal('3'), Decimal('8')),
        (Decimal('0'), Decimal('0'), Decimal('0')),
        (Decimal('-5'), Decimal('3'), Decimal('-2')),
        (Decimal('5'), Decimal('-3'), Decimal('2')),
        (Decimal('-5'), Decimal('-3'), Decimal('-8')),
        (Decimal('10.5'), Decimal('2.3'), Decimal('12.8')),
        (Decimal('1000000'), Decimal('1'), Decimal('1000001')),
    ])
    def test_execute(self, a, b, expected):
        """Test addition execution with various inputs."""
        result = self.operation.execute(a, b)
        assert result == expected
    
    def test_str_representation(self):
        """Test string representation of addition."""
        assert str(self.operation) == "+"


class TestSubtraction:
    """Test cases for Subtraction operation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Subtraction()
    
    @pytest.mark.parametrize("a, b, expected", [
        (Decimal('5'), Decimal('3'), Decimal('2')),
        (Decimal('0'), Decimal('0'), Decimal('0')),
        (Decimal('-5'), Decimal('3'), Decimal('-8')),
        (Decimal('5'), Decimal('-3'), Decimal('8')),
        (Decimal('-5'), Decimal('-3'), Decimal('-2')),
        (Decimal('10.5'), Decimal('2.3'), Decimal('8.2')),
        (Decimal('1'), Decimal('1000000'), Decimal('-999999')),
    ])
    def test_execute(self, a, b, expected):
        """Test subtraction execution with various inputs."""
        result = self.operation.execute(a, b)
        assert result == expected
    
    def test_str_representation(self):
        """Test string representation of subtraction."""
        assert str(self.operation) == "-"


class TestMultiplication:
    """Test cases for Multiplication operation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Multiplication()
    
    @pytest.mark.parametrize("a, b, expected", [
        (Decimal('5'), Decimal('3'), Decimal('15')),
        (Decimal('0'), Decimal('5'), Decimal('0')),
        (Decimal('5'), Decimal('0'), Decimal('0')),
        (Decimal('-5'), Decimal('3'), Decimal('-15')),
        (Decimal('5'), Decimal('-3'), Decimal('-15')),
        (Decimal('-5'), Decimal('-3'), Decimal('15')),
        (Decimal('2.5'), Decimal('4'), Decimal('10')),
        (Decimal('0.1'), Decimal('0.1'), Decimal('0.01')),
    ])
    def test_execute(self, a, b, expected):
        """Test multiplication execution with various inputs."""
        result = self.operation.execute(a, b)
        assert result == expected
    
    def test_str_representation(self):
        """Test string representation of multiplication."""
        assert str(self.operation) == "*"


class TestDivision:
    """Test cases for Division operation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Division()
    
    @pytest.mark.parametrize("a, b, expected", [
        (Decimal('6'), Decimal('3'), Decimal('2')),
        (Decimal('5'), Decimal('2'), Decimal('2.5')),
        (Decimal('-6'), Decimal('3'), Decimal('-2')),
        (Decimal('6'), Decimal('-3'), Decimal('-2')),
        (Decimal('-6'), Decimal('-3'), Decimal('2')),
        (Decimal('0'), Decimal('5'), Decimal('0')),
        (Decimal('1'), Decimal('3'), Decimal('0.3333333333333333333333333333')),
    ])
    def test_execute(self, a, b, expected):
        """Test division execution with various inputs."""
        result = self.operation.execute(a, b)
        assert result == expected
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.operation.execute(Decimal('5'), Decimal('0'))
    
    def test_str_representation(self):
        """Test string representation of division."""
        assert str(self.operation) == "/"


class TestOperationAbstractClass:
    """Test the abstract Operation class."""
    
    def test_cannot_instantiate_abstract_class(self):
        """Test that Operation abstract class cannot be instantiated."""
        with pytest.raises(TypeError):
            Operation()
