import random


def bullscows(guess: str, secret: str) -> tuple[int, int]:
    return sum(map(lambda x: x[0] == x[1], zip(guess, secret))), sum(map(lambda x: x in secret, set(guess)))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choices(words)
    guessed = None
    asked = 0
    while guessed != secret:
        guessed = ask("Введите слово: ", words)
        asked += 1
        b, c = bullscows(guessed, secret)
        inform("Быки: {}, Коровы: {}", b, c)
    return asked
