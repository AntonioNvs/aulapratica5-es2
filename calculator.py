import builtins


class AdvancedCalculator:

    def factorial(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("factorial() only accepts integers")
        if n < 0:
            raise ValueError("factorial() not defined for negative values")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def exponential(self, base, exponent):
        return base ** exponent

    def sums(self, *args):
        if len(args) == 0:
            return 0
        if len(args) == 1 and hasattr(args[0], "__iter__") and not isinstance(args[0], (str, bytes)):
            return builtins.sum(args[0])
        return builtins.sum(args)
