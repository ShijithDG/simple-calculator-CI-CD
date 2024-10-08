class SimpleCalculator:
    def add(self, a: int, b: int) -> int:
        """Return the sum of two positive integers."""
        self._validate_input(a, b)
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Return the difference of two positive integers."""
        self._validate_input(a, b)
        return a - b if a >= b else 0

    def multiply(self, a: int, b: int) -> int:
        """Return the product of two positive integers."""
        self._validate_input(a, b)
        return a * b

    def _validate_input(self, a: int, b: int) -> None:
        """Ensure both inputs are positive integers."""
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Both inputs must be integers.")
        if a < 0 or b < 0:
            raise ValueError("Both inputs must be positive integers.")
