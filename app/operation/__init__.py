"""
Operation module for calculator operations.
"""

from abc import ABC, abstractmethod
from decimal import Decimal


class Operation(ABC):
    """Abstract base class for mathematical operations."""
    
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Execute the operation with two operands."""
        pass  # pragma: no cover
    
    @abstractmethod
    def __str__(self) -> str:
        """Return string representation of the operation."""
        pass  # pragma: no cover


class Addition(Operation):
    """Addition operation implementation."""
    
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Perform addition of two numbers."""
        return a + b
    
    def __str__(self) -> str:
        """Return string representation of addition."""
        return "+"


class Subtraction(Operation):
    """Subtraction operation implementation."""
    
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction of two numbers."""
        return a - b
    
    def __str__(self) -> str:
        """Return string representation of subtraction."""
        return "-"


class Multiplication(Operation):
    """Multiplication operation implementation."""
    
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication of two numbers."""
        return a * b
    
    def __str__(self) -> str:
        """Return string representation of multiplication."""
        return "*"


class Division(Operation):
    """Division operation implementation."""
    
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Perform division of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def __str__(self) -> str:
        """Return string representation of division."""
        return "/"
