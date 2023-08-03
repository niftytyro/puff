import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="puff is yet another programming language."
    )
    parser.add_argument("path", help="Path to source file.")
    args = parser.parse_args()
    print(args.path)
