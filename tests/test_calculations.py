"""
Test module for calculation classes.
"""

import pytest
from decimal import Decimal
from app.calculation import Calculation, CalculationFactory, CalculationHistory
from app.operation import Addition, Subtraction, Multiplication, Division


class TestCalculation:
    """Test cases for Calculation class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.addition = Addition()
        self.subtraction = Subtraction()
        self.multiplication = Multiplication()
        self.division = Division()
    
    @pytest.mark.parametrize("a, b, operation, expected", [
        (Decimal('5'), Decimal('3'), Addition(), Decimal('8')),
        (Decimal('5'), Decimal('3'), Subtraction(), Decimal('2')),
        (Decimal('5'), Decimal('3'), Multiplication(), Decimal('15')),
        (Decimal('6'), Decimal('3'), Division(), Decimal('2')),
    ])
    def test_calculation_result(self, a, b, operation, expected):
        """Test calculation results with various operations."""
        calc = Calculation(a, b, operation)
        assert calc.result == expected
    
    def test_calculation_result_caching(self):
        """Test that calculation result is cached after first access."""
        calc = Calculation(Decimal('5'), Decimal('3'), self.addition)
        
        # First access
        result1 = calc.result
        # Second access should return cached result
        result2 = calc.result
        
        assert result1 == result2
        assert result1 == Decimal('8')
    
    def test_calculation_str_representation(self):
        """Test string representation of calculation."""
        calc = Calculation(Decimal('5'), Decimal('3'), self.addition)
        assert str(calc) == "5 + 3 = 8"
    
    def test_calculation_repr(self):
        """Test detailed representation of calculation."""
        calc = Calculation(Decimal('5'), Decimal('3'), self.addition)
        assert repr(calc) == "Calculation(5, 3, Addition)"
    
    def test_calculation_with_division_by_zero(self):
        """Test calculation that results in division by zero."""
        calc = Calculation(Decimal('5'), Decimal('0'), self.division)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            _ = calc.result
    
    def test_calculation_properties(self):
        """Test calculation properties are set correctly."""
        a = Decimal('10')
        b = Decimal('5')
        operation = self.subtraction
        calc = Calculation(a, b, operation)
        
        assert calc.a == a
        assert calc.b == b
        assert calc.operation == operation


class TestCalculationFactory:
    """Test cases for CalculationFactory class."""
    
    def test_create_calculation(self):
        """Test factory creates calculation correctly."""
        a = Decimal('5')
        b = Decimal('3')
        operation = Addition()
        
        calc = CalculationFactory.create_calculation(a, b, operation)
        
        assert isinstance(calc, Calculation)
        assert calc.a == a
        assert calc.b == b
        assert calc.operation == operation
    
    @pytest.mark.parametrize("a, b, operation_class", [
        (Decimal('1'), Decimal('2'), Addition),
        (Decimal('10'), Decimal('5'), Subtraction),
        (Decimal('3'), Decimal('4'), Multiplication),
        (Decimal('8'), Decimal('2'), Division),
    ])
    def test_create_calculation_parameterized(self, a, b, operation_class):
        """Test factory with various operation types."""
        operation = operation_class()
        calc = CalculationFactory.create_calculation(a, b, operation)
        
        assert calc.a == a
        assert calc.b == b
        assert isinstance(calc.operation, operation_class)


class TestCalculationHistory:
    """Test cases for CalculationHistory class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.history = CalculationHistory()
        self.calc1 = Calculation(Decimal('5'), Decimal('3'), Addition())
        self.calc2 = Calculation(Decimal('10'), Decimal('2'), Division())
        self.calc3 = Calculation(Decimal('7'), Decimal('4'), Multiplication())
    
    def test_empty_history(self):
        """Test empty history behavior."""
        assert len(self.history) == 0
        assert self.history.get_history() == []
    
    def test_add_single_calculation(self):
        """Test adding a single calculation to history."""
        self.history.add_calculation(self.calc1)
        
        assert len(self.history) == 1
        assert self.history.get_last_calculation() == self.calc1
        assert self.calc1 in self.history.get_history()
    
    def test_add_multiple_calculations(self):
        """Test adding multiple calculations to history."""
        self.history.add_calculation(self.calc1)
        self.history.add_calculation(self.calc2)
        self.history.add_calculation(self.calc3)
        
        assert len(self.history) == 3
        assert self.history.get_last_calculation() == self.calc3
        
        history_list = self.history.get_history()
        assert history_list == [self.calc1, self.calc2, self.calc3]
    
    def test_get_last_calculation_empty_history(self):
        """Test getting last calculation from empty history raises error."""
        with pytest.raises(IndexError, match="No calculations in history"):
            self.history.get_last_calculation()
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.history.add_calculation(self.calc1)
        self.history.add_calculation(self.calc2)
        
        assert len(self.history) == 2
        
        self.history.clear_history()
        
        assert len(self.history) == 0
        assert self.history.get_history() == []
    
    def test_history_iteration(self):
        """Test that history is iterable."""
        self.history.add_calculation(self.calc1)
        self.history.add_calculation(self.calc2)
        
        calculations = list(self.history)
        assert calculations == [self.calc1, self.calc2]
    
    def test_get_history_returns_copy(self):
        """Test that get_history returns a copy, not the original list."""
        self.history.add_calculation(self.calc1)
        
        history_copy = self.history.get_history()
        history_copy.append(self.calc2)
        
        # Original history should not be modified
        assert len(self.history) == 1
        assert len(history_copy) == 2
