import argparse
import json
import sys
from black_mirror.core import BlackMirror
from black_mirror.utils import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Black Mirror OSINT Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Lookup command
    lookup_parser = subparsers.add_parser("lookup", help="Perform a lookup")
    lookup_parser.add_argument("--type", required=True, choices=["email", "username", "domain", "phone"], help="Type of query")
    lookup_parser.add_argument("--value", required=True, help="Value to query")
    lookup_parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    if args.command == "lookup":
        setup_logging(args.verbose)
        bm = BlackMirror()
        result = bm.lookup(args.type, args.value)
        print(json.dumps(result, indent=2))
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
