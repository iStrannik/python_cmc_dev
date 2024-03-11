import argparse
import random

import cowsay
import requests


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


def main():
    parser = argparse.ArgumentParser(
        prog='CowSay emulator',
        description='Program is wrapper of cowsay-py module'
    )
    parser.add_argument('dict', type=str,
                        help='path to dict or url')

    parser.add_argument('-l', '--len', type=int, default=5,
                        help='wordlen')

    args = parser.parse_args()
    words = []

    try:
        resp = requests.get(args.dict)
        words = [x.strip() for x in resp.text.split()]
    except:
        try:
            with open(args.dict, 'r') as file:
                words = [x.strip() for x in file.readlines()]
        except:
            print('Cant get words')
            return

    assert all(map(lambda x: len(x) == args.len, words))

    def ask(prompt: str, valid: list[str] = None) -> str:
        a = input(cowsay.cowsay(prompt, cow='./my_cow.cow')).strip()
        if valid:
            assert a in valid, "invalid word"
        return a

    def inform(format_string: str, bulls: int, cows: int) -> None:
        cow = random.choice(cowsay.list_cows())
        print(cowsay.cowsay(format_string.format(bulls, cows), cow=cow))

    print(f'Вам понадобилось {gameplay(ask, inform, words)} попыток')


if __name__ == '__main__':
    main()
