import unittest


"""
Q: Given an integer n, find the fibonacci sequence at that number n (Assuming we start at 0)

A: the fibonaccia number at each position n is derived by looking at the nos at n-1 and n-2
The 2 special cases are when n ==0 and n==1 - So we start with a dict of these 2 values
Then we iterate until we reach n. 
Since we store the results in a dict and lookup is O(1), the Run time and space complexity of this solution is O(n)
"""

def fibonacci(n: int) -> int:
    fibo = {i:i for i in range(2)}
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]


class TestFibonacciDPSolution(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)
    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), 2)
    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)
    def test_fibonacci_7(self):
        self.assertEqual(fibonacci(7), 13)
    def test_user_input(self):
        try:
            # Get input from user
            n = int(input("Enter a number to test fibonacci: "))
            expected = int(input("Enter the expected fibonacci result: "))
            # Calculate actual result
            result = fibonacci(n)
            # Custom message for assertion
            message = f"For fibonacci({n}): Expected {expected}, but got {result}"
            # Assert with custom message
            self.assertEqual(result, expected, message)
        except ValueError:
            self.fail("Please enter valid integer numbers")

if __name__ == "__main__":
    unittest.main()