import argparse
import random


def main():
    parser = argparse.ArgumentParser(description="Tesco's deal mistake, implemented in Python.")
    parser.add_argument('barcode', type=str, help='Original barcode')
    parser.add_argument('price', type=str, help='Desired price in pence')
    parser.add_argument('mystery', type=str, nargs="?", default=False, help='Manually set the mystery arg')
    args = parser.parse_args()

    print calculate_barcode(args.barcode, args.price, args.mystery)


def calculate_barcode(barcode, price, mystery=False):
    new = "971{barcode}{mystery}{price}0".format(
        barcode=barcode,
        mystery=mystery or str(random.randint(0, 9)),
        price=price.zfill(5))

    evens_checksum = sum(int(char) for i, char in enumerate(new) if (i + 1) % 2 == 0)
    odds_checksum = sum(int(char) for i, char in enumerate(new) if (i + 1) % 2 != 0) * 3
    checksum = 10 - ((evens_checksum + odds_checksum) % 10)

    return new + str(checksum)


if "__main__" == __name__:
    main()
