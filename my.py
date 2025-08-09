# -*- coding: utf-8 -*-
import os
import sys
import argparse
# from termcolor import colored

os.environ.setdefault("TESTING_ZVT", "True")
os.environ.setdefault("SQLALCHEMY_WARN_20", "1")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "./src")))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
            "--zvt",
            help="zvt main",
            action="store_true",
        )
    parser.add_argument(
        "--server",
        help="zvt server",
        action="store_true",
    )
    parser.add_argument(
        "--plugin",
        help="zvt plugin",
        action="store_true",
    )
    args = parser.parse_args()

    if args.zvt:
        from src.zvt.main import main as zvt_main

        zvt_main()
    elif args.server:
        from src.zvt.zvt_server import main as zvt_server_main

        zvt_server_main()
    elif args.plugin:
        from src.zvt.plugin import main as plugin_main

        plugin_main()
    else:
        parser.print_help()
    pass


if __name__ == "__main__":
    main()
