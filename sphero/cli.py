import argparse
from .sphero import get_sphero_path

def main():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    # Build subparser
    go = sub_parser.add_parser("go", description="")
    args = parser.parse_args()

    # Execute
    get_sphero_path()

if __name__ == "__main__":
    main()
