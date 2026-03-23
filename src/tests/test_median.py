from examanalytics.reports.median import MedianCoffeeReport


def test_median_report():
    rows = [
        {"student": "Ivan", "coffee_spent": "100"},
        {"student": "Ivan", "coffee_spent": "200"},
        {"student": "Ivan", "coffee_spent": "300"},
        {"student": "Anna", "coffee_spent": "50"},
        {"student": "Anna", "coffee_spent": "150"},
    ]

    report = MedianCoffeeReport()
    result = report.generate(rows)

    result_dict = dict(result)

    assert result_dict["Ivan"] == 200
    assert result_dict["Anna"] == 100