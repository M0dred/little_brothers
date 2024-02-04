import argparse

def init_argparse():
    arg = argparse.ArgumentParser(
        description="Little Brothers - Your friendly OSINT helper",
    )
    arg.add_argument(
        "-v", "--version", action="version", version="0.1"
    )
    return arg

def main():
    args = init_argparse().parse_args()

if __name__ == "__main__":
    main()