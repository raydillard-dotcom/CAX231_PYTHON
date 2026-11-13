
def logic_bits_demo():
    print(" Logical Operators ")
    # Asking the user for inputs

    raw_input1 = input("Enter first boolean (True/False or 1/0): ")
    raw_input2 = input("Enter second boolean (True/False or 1/0): ")
    
    a = raw_input1.strip().lower() in ["true", "1"]
    b = raw_input2.strip().lower() in ["true", "1"]
    
    print(f"\nYour inputs evaluated as: a = {a}, b = {b}")
    print(f"1. a and b : {a and b}")
    print(f"2. a or b  : {a or b}")
    print(f"3. not a   : {not a}")
    print(f"4. not b   : {not b}")
    
    print("\n" + "=" * 40 + "\n")
    
    print(" Bitwise Operators")
    # Using 2 small integers: 5 (binary 0101) and 3 (binary 0011)
    num1 = 5
    num2 = 3
    
    print(f"Integer 1: {num1} -> Binary: {bin(num1)}")
    print(f"Integer 2: {num2} -> Binary: {bin(num2)}")
    print("-" * 40)
    
    # Bitwise AND (&)
    bitwise_and = num1 & num2
    print(f"Bitwise AND (5 & 3): {bitwise_and} (Binary: {bin(bitwise_and)})")
    
    # Bitwise OR (|)
    bitwise_or = num1 | num2
    print(f"Bitwise OR  (5 | 3): {bitwise_or} (Binary: {bin(bitwise_or)})")
    
    # Bitwise XOR (^)
    bitwise_xor = num1 ^ num2
    print(f"Bitwise XOR (5 ^ 3): {bitwise_xor} (Binary: {bin(bitwise_xor)})")
    
    # Bitwise NOT (~)
    bitwise_not = ~num1
    print(f"Bitwise NOT (~5):    {bitwise_not} (Binary: {bin(bitwise_not)})")
    
    # Left Shift (<<)
    left_shift = num1 << 1
    print(f"Left Shift  (5 << 1):{left_shift} (Binary: {bin(left_shift)})")
    
    # Right Shift (>>)
    right_shift = num1 >> 1
    print(f"Right Shift (5 >> 1):{right_shift} (Binary: {bin(right_shift)})")

if __name__ == "__main__":
    logic_bits_demo()