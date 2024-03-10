import argparse

import cowsay


def main():
    parser = argparse.ArgumentParser(
        prog='CowSay emulator',
        description='Program is wrapper of cowsay-py module'
    )
    parser.add_argument('-l', action='store_true')
    parser.add_argument('-e', default='oo', type=str)
    parser.add_argument('-f', default='default', type=str)
    parser.add_argument('-n', action='store_true')
    parser.add_argument('-T', type=str, default='  ')
    parser.add_argument('-W', default=40, type=int)
    # bdgpstwy
    parser.add_argument('-b', action='store_true')
    parser.add_argument('-d', action='store_true')
    parser.add_argument('-g', action='store_true')
    parser.add_argument('-p', action='store_true')
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-t', action='store_true')
    parser.add_argument('-w', action='store_true')
    parser.add_argument('-y', action='store_true')

    parser.add_argument('message', metavar='M', type=str, default='', nargs='*',
                        help='your message')

    args = parser.parse_args()
    if args.l:
        cowsay.list_cows()
        return
    p = 'bdgpstwy'
    res = ''
    for char in p:
        if getattr(args, char):
            res += char
    print(cowsay.cowsay(' '.join(args.message),
                        args.f,
                        res,
                        args.e,
                        args.T,
                        args.W,
                        args.n
                        ))


if __name__ == '__main__':
    main()
