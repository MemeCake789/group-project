def fizzBuzz(num : int, fizzNum : int, buzzNum : int) -> None:
    for i in range(1, num + 1):
        output = (
            f"FizzBuzz"  if i % fizzNum == 0 and i % buzzNum == 0
            else f"Fizz" if i % fizzNum == 0 
            else f"Buzz" if i % buzzNum == 0
            else i
        )
        print(output)
if __name__ == "__main__":
    fizzBuzz(100, 3, 5)
