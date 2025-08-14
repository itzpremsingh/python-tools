# Length finder for whole number

def length(number: int) -> int:
    _len = 0
    
    while number > 0:
        number //= 10
        _len += 1
        
    return _len


if __name__ == "__main__":
    numbers = [10, 100, 1, 19, 453, 6555, 76753342]

    for num in numbers:
        print(f"{num} > {length(num)}")
