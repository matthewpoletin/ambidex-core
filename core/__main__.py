#!/usr/bin/env python3

from core.communication.server import run_server


def main():
    run_server(9000, True)


if __name__ == "__main__":
    main()
