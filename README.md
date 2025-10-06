# Professional Calculator Application

A modular, professional-grade command-line calculator application written in Python with comprehensive testing, error handling, and continuous integration.

## Features

- **REPL Interface**: Interactive Read-Eval-Print Loop for continuous user interaction
- **Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Input Validation**: Comprehensive validation with clear error messages
- **Error Handling**: Implements both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) paradigms
- **Calculation History**: Maintains session history with special commands
- **Modular Design**: Clean architecture with separation of concerns
- **100% Test Coverage**: Comprehensive test suite with parameterized tests
- **Professional Documentation**: Detailed docstrings and comments

## Project Structure

```
MOD4/
├── app/
│   ├── __init__.py                 # Main application module
│   ├── calculator/
│   │   └── __init__.py            # Calculator REPL interface
│   ├── calculation/
│   │   └── __init__.py            # Calculation management
│   └── operation/
│       └── __init__.py            # Operation implementations
├── tests/
│   ├── __init__.py                # Test configuration
│   ├── test_calculator.py         # Calculator tests
│   ├── test_calculations.py       # Calculation tests
│   └── test_operations.py         # Operation tests
├── .github/
│   └── workflows/
│       └── python-app.yml         # CI/CD pipeline
├── main.py                        # Application entry point
├── requirements.txt               # Dependencies
├── pyproject.toml                 # Project configuration
└── README.md                      # This file
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd MOD4
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Calculator

Start the calculator application:

```bash
python main.py
```

### Available Commands

- **Calculations**: `<number> <operation> <number>`
  - Example: `5 + 3`, `10.5 subtract 2.3`
- **help**: Display available commands and operations
- **history**: Show calculation history
- **clear**: Clear calculation history
- **exit**: Exit the calculator

### Supported Operations

| Operation | Symbols | Examples |
|-----------|---------|----------|
| Addition | `+`, `add` | `5 + 3`, `10 add 2` |
| Subtraction | `-`, `subtract` | `10 - 3`, `15 subtract 5` |
| Multiplication | `*`, `multiply` | `4 * 5`, `3 multiply 7` |
| Division | `/`, `divide` | `15 / 3`, `20 divide 4` |

### Example Session

```
Welcome to the Professional Calculator!
Type 'help' for available commands or 'exit' to quit.
--------------------------------------------------

Calculator> 5 + 3
Result: 5 + 3 = 8

Calculator> 10 multiply 2.5
Result: 10 * 2.5 = 25

Calculator> history
Calculation History:
------------------------------
 1. 5 + 3 = 8
 2. 10 * 2.5 = 25

Calculator> exit
Thank you for using the calculator. Goodbye!
```

## Development

### Running Tests

Run all tests with coverage:
```bash
pytest --cov=app tests/
```

Run tests with detailed coverage report:
```bash
pytest --cov=app --cov-report=html tests/
```

### Test Coverage

The project maintains 100% test coverage. Coverage reports can be found in:
- Terminal output: `--cov-report=term-missing`
- HTML report: `htmlcov/index.html`

### Code Quality

The codebase follows Python best practices:
- **DRY Principle**: No code repetition
- **Modular Design**: Clear separation of concerns
- **Error Handling**: Comprehensive error management
- **Type Hints**: Using Decimal for precise arithmetic
- **Documentation**: Detailed docstrings and comments

## Architecture

### Design Patterns

1. **Factory Pattern**: `CalculationFactory` for creating calculation instances
2. **Strategy Pattern**: Different operation implementations
3. **Command Pattern**: REPL command handling

### Error Handling Paradigms

- **LBYL (Look Before You Leap)**: Input validation before processing
- **EAFP (Easier to Ask Forgiveness than Permission)**: Try-catch for number parsing and division

### Key Components

1. **Operation Module** (`app/operation/`):
   - Abstract `Operation` base class
   - Concrete implementations: `Addition`, `Subtraction`, `Multiplication`, `Division`

2. **Calculation Module** (`app/calculation/`):
   - `Calculation`: Represents a single calculation
   - `CalculationFactory`: Creates calculation instances
   - `CalculationHistory`: Manages calculation history

3. **Calculator Module** (`app/calculator/`):
   - `Calculator`: Main REPL interface and calculation logic

## Continuous Integration

The project uses GitHub Actions for CI/CD:

- **Automated Testing**: Runs on every push and pull request
- **Coverage Enforcement**: Fails if coverage drops below 100%
- **Multi-Python Support**: Tests against Python 3.x
- **Dependency Management**: Automatic dependency installation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure tests pass and coverage remains 100%
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Error Handling Examples

### Division by Zero
```
Calculator> 5 / 0
Error: Cannot divide by zero
```

### Invalid Input Format
```
Calculator> 5 +
Error: Invalid input format. Expected: <number> <operation> <number>
```

### Invalid Operation
```
Calculator> 5 % 3
Error: Unknown operation: %
```

### Invalid Number
```
Calculator> abc + 3
Error: Invalid number format: [Invalid decimal literal]
```

## Technical Details

- **Precision**: Uses Python's `Decimal` class for accurate arithmetic
- **Input Validation**: Comprehensive validation with clear error messages
- **Memory Management**: Efficient calculation history management
- **Performance**: Optimized for interactive use with result caching
- **Extensibility**: Modular design allows easy addition of new operations
