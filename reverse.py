
# Make a function that reverses a string

def reverse(x: str) -> str:
    result = x[::-1]
    return result

x = "Hello"
print(reverse(x))

def test_reverse_function():
    input_string = "Hello"
    expected_output = "olleH"
    result = reverse(input_string)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

print("Test Passed")