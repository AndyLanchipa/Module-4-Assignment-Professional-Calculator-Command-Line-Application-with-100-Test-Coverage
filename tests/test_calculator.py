"""
Test module for calculator main class.
"""

import pytest
from decimal import Decimal
from io import StringIO
import sys
from unittest.mock import patch, MagicMock

from app.calculator import Calculator
from app.operation import Addition, Subtraction, Multiplication, Division


class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calculator = Calculator()
    
    def test_calculator_initialization(self):
        """Test calculator is initialized with correct operations and empty history."""
        assert '+' in self.calculator.operations
        assert '-' in self.calculator.operations
        assert '*' in self.calculator.operations
        assert '/' in self.calculator.operations
        assert 'add' in self.calculator.operations
        assert 'subtract' in self.calculator.operations
        assert 'multiply' in self.calculator.operations
        assert 'divide' in self.calculator.operations
        
        assert len(self.calculator.history) == 0
    
    @pytest.mark.parametrize("a, operation_str, b, expected", [
        (Decimal('5'), '+', Decimal('3'), Decimal('8')),
        (Decimal('5'), 'add', Decimal('3'), Decimal('8')),
        (Decimal('10'), '-', Decimal('4'), Decimal('6')),
        (Decimal('10'), 'subtract', Decimal('4'), Decimal('6')),
        (Decimal('7'), '*', Decimal('3'), Decimal('21')),
        (Decimal('7'), 'multiply', Decimal('3'), Decimal('21')),
        (Decimal('15'), '/', Decimal('3'), Decimal('5')),
        (Decimal('15'), 'divide', Decimal('3'), Decimal('5')),
    ])
    def test_calculate_method(self, a, operation_str, b, expected):
        """Test programmatic calculate method with various operations."""
        result = self.calculator.calculate(a, operation_str, b)
        assert result == expected
        assert len(self.calculator.history) == 1
    
    def test_calculate_unknown_operation(self):
        """Test calculate method with unknown operation raises error."""
        with pytest.raises(ValueError, match="Unknown operation: unknown"):
            self.calculator.calculate(Decimal('5'), 'unknown', Decimal('3'))
    
    def test_calculate_division_by_zero(self):
        """Test calculate method with division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.calculate(Decimal('5'), '/', Decimal('0'))
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_process_calculation_valid_input(self, mock_print, mock_input):
        """Test processing valid calculation input."""
        self.calculator._process_calculation("5 + 3")
        
        # Check that result was printed
        mock_print.assert_called()
        assert len(self.calculator.history) == 1
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_process_calculation_invalid_format(self, mock_print, mock_input):
        """Test processing invalid input format."""
        self.calculator._process_calculation("5 +")
        
        # Check that error was printed
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Invalid input format" in call for call in calls)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_process_calculation_invalid_operation(self, mock_print, mock_input):
        """Test processing invalid operation."""
        self.calculator._process_calculation("5 % 3")
        
        # Check that error was printed
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Unknown operation" in call for call in calls)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_process_calculation_invalid_number(self, mock_print, mock_input):
        """Test processing invalid number format."""
        self.calculator._process_calculation("abc + 3")
        
        # Check that error was printed
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Invalid number format" in call for call in calls)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_process_calculation_division_by_zero(self, mock_print, mock_input):
        """Test processing division by zero."""
        self.calculator._process_calculation("5 / 0")
        
        # Check that error was printed
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Cannot divide by zero" in call for call in calls)
    
    @patch('builtins.print')
    def test_show_help(self, mock_print):
        """Test help command displays help text."""
        self.calculator._show_help()
        
        # Check that help text was printed
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Available Commands" in call for call in calls)
    
    @patch('builtins.print')
    def test_show_history_empty(self, mock_print):
        """Test showing empty history."""
        self.calculator._show_history()
        
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("No calculations in history" in call for call in calls)
    
    @patch('builtins.print')
    def test_show_history_with_calculations(self, mock_print):
        """Test showing history with calculations."""
        # Add some calculations
        self.calculator.calculate(Decimal('5'), '+', Decimal('3'))
        self.calculator.calculate(Decimal('10'), '-', Decimal('2'))
        
        self.calculator._show_history()
        
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Calculation History" in call for call in calls)
    
    @patch('builtins.print')
    def test_clear_history(self, mock_print):
        """Test clearing calculation history."""
        # Add a calculation
        self.calculator.calculate(Decimal('5'), '+', Decimal('3'))
        assert len(self.calculator.history) == 1
        
        self.calculator._clear_history()
        
        assert len(self.calculator.history) == 0
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("history cleared" in call for call in calls)
    
    @patch('builtins.input', side_effect=['5 + 3', 'exit'])
    @patch('builtins.print')
    def test_start_repl_basic_calculation(self, mock_print, mock_input):
        """Test REPL with basic calculation and exit."""
        self.calculator.start()
        
        # Check that welcome message and result were printed
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Welcome" in call for call in calls)
        assert any("Goodbye" in call for call in calls)
    
    @patch('builtins.input', side_effect=['help', 'exit'])
    @patch('builtins.print')
    def test_start_repl_help_command(self, mock_print, mock_input):
        """Test REPL help command."""
        self.calculator.start()
        
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Available Commands" in call for call in calls)
    
    @patch('builtins.input', side_effect=['5 + 3', 'history', 'exit'])
    @patch('builtins.print')
    def test_start_repl_history_command(self, mock_print, mock_input):
        """Test REPL history command."""
        self.calculator.start()
        
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Calculation History" in call for call in calls)
    
    @patch('builtins.input', side_effect=['5 + 3', 'clear', 'history', 'exit'])
    @patch('builtins.print')
    def test_start_repl_clear_command(self, mock_print, mock_input):
        """Test REPL clear command."""
        self.calculator.start()
        
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("history cleared" in call for call in calls)
    
    @patch('builtins.input', side_effect=['', '   ', 'exit'])
    @patch('builtins.print')
    def test_start_repl_empty_input(self, mock_print, mock_input):
        """Test REPL with empty input."""
        self.calculator.start()
        
        # Should handle empty input gracefully
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Welcome" in call for call in calls)
    
    @patch('builtins.input', side_effect=[KeyboardInterrupt, 'exit'])
    @patch('builtins.print')
    def test_start_repl_keyboard_interrupt(self, mock_print, mock_input):
        """Test REPL handles keyboard interrupt."""
        self.calculator.start()
        
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("interrupted" in call for call in calls)
