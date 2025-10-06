"""
Calculator module containing the main REPL interface and calculator logic.
"""

from decimal import Decimal, InvalidOperation
from typing import Dict, Optional
import sys

from app.operation import Addition, Subtraction, Multiplication, Division, Operation
from app.calculation import CalculationFactory, CalculationHistory, Calculation


class Calculator:
    """Main calculator class with REPL interface."""
    
    def __init__(self):
        """Initialize the calculator with operations and history."""
        self.operations: Dict[str, Operation] = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            'add': Addition(),
            'subtract': Subtraction(),
            'multiply': Multiplication(),
            'divide': Division()
        }
        self.history = CalculationHistory()
        self.factory = CalculationFactory()
    
    def start(self) -> None:
        """Start the REPL interface."""
        print("Welcome to the Professional Calculator!")
        print("Type 'help' for available commands or 'exit' to quit.")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nCalculator> ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() == 'exit':
                    print("Thank you for using the calculator. Goodbye!")
                    break
                elif user_input.lower() == 'help':
                    self._show_help()
                elif user_input.lower() == 'history':
                    self._show_history()
                elif user_input.lower() == 'clear':
                    self._clear_history()
                else:
                    self._process_calculation(user_input)
                    
            except KeyboardInterrupt:
                print("\n\nCalculator interrupted. Type 'exit' to quit gracefully.")
            except EOFError:  # pragma: no cover
                print("\n\nExiting calculator...")
                break
    
    def _process_calculation(self, user_input: str) -> None:
        """
        Process a calculation input from the user.
        
        Args:
            user_input: The user's input string
        """
        try:
            # Parse the input using LBYL approach
            parts = user_input.split()
            
            if len(parts) != 3:
                raise ValueError("Invalid input format. Expected: <number> <operation> <number>")
            
            # LBYL: Check if operation exists before proceeding
            operation_str = parts[1].lower()
            if operation_str not in self.operations:
                raise ValueError(f"Unknown operation: {operation_str}")
            
            # Parse numbers using EAFP approach
            try:
                a = Decimal(parts[0])
                b = Decimal(parts[2])
            except InvalidOperation as e:
                raise ValueError(f"Invalid number format: {e}")
            
            operation = self.operations[operation_str]
            
            # Create and execute calculation
            calculation = self.factory.create_calculation(a, b, operation)
            
            # EAFP: Try to get result, handle division by zero
            try:
                result = calculation.result
                self.history.add_calculation(calculation)
                print(f"Result: {calculation}")
            except ValueError as e:
                print(f"Error: {e}")
                
        except ValueError as e:
            print(f"Error: {e}")
            print("Use 'help' command for usage instructions.")
    
    def _show_help(self) -> None:
        """Display help information."""
        help_text = """
Available Commands:
  <number> <operation> <number>  - Perform calculation
  help                           - Show this help message
  history                        - Show calculation history
  clear                          - Clear calculation history
  exit                           - Exit the calculator

Operations:
  +, add        - Addition
  -, subtract   - Subtraction
  *, multiply   - Multiplication
  /, divide     - Division

Examples:
  5 + 3
  10.5 subtract 2.3
  7 * 8
  15 divide 3
        """
        print(help_text)
    
    def _show_history(self) -> None:
        """Display calculation history."""
        if len(self.history) == 0:
            print("No calculations in history.")
            return
        
        print("\nCalculation History:")
        print("-" * 30)
        for i, calculation in enumerate(self.history, 1):
            print(f"{i:2d}. {calculation}")
    
    def _clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear_history()
        print("Calculation history cleared.")
    
    def calculate(self, a: Decimal, operation_str: str, b: Decimal) -> Decimal:
        """
        Perform a single calculation programmatically.
        
        Args:
            a: First operand
            operation_str: Operation string
            b: Second operand
            
        Returns:
            The calculation result
            
        Raises:
            ValueError: If operation is unknown or calculation fails
        """
        if operation_str not in self.operations:
            raise ValueError(f"Unknown operation: {operation_str}")
        
        operation = self.operations[operation_str]
        calculation = self.factory.create_calculation(a, b, operation)
        result = calculation.result
        self.history.add_calculation(calculation)
        return result


def main():  # pragma: no cover
    """Main entry point for the calculator application."""
    calculator = Calculator()
    calculator.start()


if __name__ == "__main__":
    main()  # pragma: no cover
