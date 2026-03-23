from collections import defaultdict
from statistics import median

from examanalytics.reports.base import BaseReport


class MedianCoffeeReport(BaseReport):
    """
    Median coffee spending per student.
    """

    name = "median-coffee"

    def generate(self,rows: list[dict[str, str]],):
        """
        Calculate median coffee_spent per student.
        """

        grouped: dict[str, list[int]] = defaultdict(list)

        for row in rows:
            student = row["student"]
            coffee = int(row["coffee_spent"])

            grouped[student].append(coffee)

        result = []

        for student, values in grouped.items():
            med = median(values)
            result.append((student, med))

        result.sort(key=lambda x: x[1], reverse=True)

        return result
