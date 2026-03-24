import argparse


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate reports from exam CSV files."
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name (e.g. median-coffee)",
    )

    return parser.parse_args()
