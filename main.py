import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Simple greeting CLI")
    parser.add_argument("--name", default="world", help="Name to greet")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    print(f"Hello, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())