
def parity(x: int) -> int: 
    result = 0

    while x: 
        result ^= x & 1
        x >>= 1 
    return result

print(f"Parity of 10001000: {parity(100010000)}")
