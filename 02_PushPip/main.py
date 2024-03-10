import argparse

import cowsay


def main():
    parser = argparse.ArgumentParser(
        prog='CowSay emulator',
        description='Program is wrapper of cowsay-py module'
    )
    parser.add_argument('-l',
                        action='store_true')

    args = parser.parse_args()
    if args.l:
        cowsay.list_cows()


if __name__ == '__main__':
    main()
