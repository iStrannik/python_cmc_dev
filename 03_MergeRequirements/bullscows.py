def bullscows(guess: str, secret: str) -> tuple[int, int]:
    return sum(map(lambda x: x[0] == x[1], zip(guess, secret))), sum(map(lambda x: x in secret, set(guess)))
