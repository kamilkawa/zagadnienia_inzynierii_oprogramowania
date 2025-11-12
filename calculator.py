from typing import Optional, Union


class Calculator:
    """Prosty kalkulator wykonujący operacje na dwóch liczbach."""

    def __init__(
        self, op1: Union[int, float, str], op2: Union[int, float, str]
    ) -> None:
        self._op1 = self._convert_operand(op1, "op1")
        self._op2 = self._convert_operand(op2, "op2")

    def sum(self) -> float:
        """Zwraca sumę argumentów."""
        return self._op1 + self._op2

    def subtract(self) -> float:
        """Zwraca różnicę argumentów (op1 - op2)."""
        return self._op1 - self._op2

    def multiply(self) -> float:
        """Zwraca iloczyn argumentów."""
        return self._op1 * self._op2

    def divide(self) -> Optional[float]:
        """Zwraca iloraz argumentów (op1 / op2) lub None w przypadku błędu."""
        try:
            return self._op1 / self._op2
        except ZeroDivisionError:
            print("Błąd: dzielenie przez zero, operacja nie została wykonana.")
            return None

    def _convert_operand(self, value: Union[int, float, str], name: str) -> float:
        """Przekonwertuj wartość na liczbę zmiennoprzecinkową lub zgłoś błąd. Obsługa stringów na wejściu."""
        try:
            return float(value)
        except (TypeError, ValueError) as exception:
            raise ValueError(f"Argument {name} musi być liczbą.") from exception


if __name__ == "__main__":
    kalkulator = Calculator(9, 3)
    print("Suma 9 + 3 =", kalkulator.sum())
    print("Różnica 9 - 3 =", kalkulator.subtract())
    print("Iloczyn 9 * 3 =", kalkulator.multiply())
    print("Iloraz 9 / 3 =", kalkulator.divide())

    kalkulator_zero = Calculator(5, 0)
    print("Iloraz 5 / 0 =", kalkulator_zero.divide())

    kalkulator_zero_zero = Calculator(0, 0)
    print("Iloraz 0 / 0 =", kalkulator_zero_zero.divide())
