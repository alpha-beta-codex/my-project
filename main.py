import argparse

VERSION = "1.0.0"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Simple greeting CLI")
    parser.add_argument("--name", default="world", help="Name to greet")
    parser.add_argument(
        "--shout",
        action="store_true",
        help="Print greeting in uppercase",
    )
    parser.add_argument(
        "--v",
        action="store_true",
        help="Print script version and exit",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.v:
        print(VERSION)
        return 0

    greeting = f"Hello, {args.name}!"
    if args.shout:
        greeting = greeting.upper()
    print(greeting)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
