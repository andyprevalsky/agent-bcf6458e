"""Print the Collatz sequence starting at 27 and its step count."""


def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    steps = len(sequence) - 1
    print(f"Steps: {steps}")


if __name__ == "__main__":
    main()
