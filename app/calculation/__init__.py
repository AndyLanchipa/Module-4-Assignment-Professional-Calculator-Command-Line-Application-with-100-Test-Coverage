"""
Calculation module for managing calculations and calculation history.
"""

from decimal import Decimal
from typing import List
from app.operation import Operation


class Calculation:
    """Represents a single calculation with operands, operation, and result."""
    
    def __init__(self, a: Decimal, b: Decimal, operation: Operation):
        """
        Initialize a calculation.
        
        Args:
            a: First operand
            b: Second operand
            operation: Operation to perform
        """
        self.a = a
        self.b = b
        self.operation = operation
        self._result = None
    
    @property
    def result(self) -> Decimal:
        """
        Get the result of the calculation.
        
        Returns:
            The calculated result
        """
        if self._result is None:
            self._result = self.operation.execute(self.a, self.b)
        return self._result
    
    def __str__(self) -> str:
        """Return string representation of the calculation."""
        return f"{self.a} {self.operation} {self.b} = {self.result}"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__class__.__name__})"


class CalculationFactory:
    """Factory class for creating calculations."""
    
    @staticmethod
    def create_calculation(a: Decimal, b: Decimal, operation: Operation) -> Calculation:
        """
        Create a new calculation instance.
        
        Args:
            a: First operand
            b: Second operand
            operation: Operation to perform
            
        Returns:
            A new Calculation instance
        """
        return Calculation(a, b, operation)


class CalculationHistory:
    """Manages the history of calculations."""
    
    def __init__(self):
        """Initialize an empty calculation history."""
        self._history: List[Calculation] = []
    
    def add_calculation(self, calculation: Calculation) -> None:
        """
        Add a calculation to the history.
        
        Args:
            calculation: The calculation to add
        """
        self._history.append(calculation)
    
    def get_history(self) -> List[Calculation]:
        """
        Get the complete calculation history.
        
        Returns:
            List of all calculations in chronological order
        """
        return self._history.copy()
    
    def get_last_calculation(self) -> Calculation:
        """
        Get the most recent calculation.
        
        Returns:
            The last calculation performed
            
        Raises:
            IndexError: If no calculations have been performed
        """
        if not self._history:
            raise IndexError("No calculations in history")
        return self._history[-1]
    
    def clear_history(self) -> None:
        """Clear all calculations from history."""
        self._history.clear()
    
    def __len__(self) -> int:
        """Return the number of calculations in history."""
        return len(self._history)
    
    def __iter__(self):
        """Make the history iterable."""
        return iter(self._history)
