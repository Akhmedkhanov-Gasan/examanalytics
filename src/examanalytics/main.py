from tabulate import tabulate

from examanalytics.cli import parse_args
from examanalytics.reader import read_csv_files
from examanalytics.reports import REPORTS


def main():
    """
    Application entry point.
    """
    args = parse_args()

    report_class = REPORTS.get(args.report)
    if report_class is None:
        available = ", ".join(REPORTS.keys())
        raise ValueError(
            f"Unknown report: {args.report}. Available: {available}"
        )

    rows = read_csv_files(args.files)

    report = report_class()
    result = report.generate(rows)

    print(
        tabulate(
            result,
            headers=["student", "median_coffee"],
            tablefmt="grid",
        )
    )


if __name__ == "__main__":
    main()
