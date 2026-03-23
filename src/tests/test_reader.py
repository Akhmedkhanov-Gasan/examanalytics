from examanalytics.reader import read_csv_files


def test_read_single_file(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "student,coffee_spent\n"
        "Ivan,100\n"
        "Ivan,200\n",
        encoding="utf-8",
    )

    rows = read_csv_files([str(file)])

    assert len(rows) == 2
    assert rows[0]["student"] == "Ivan"
    assert rows[0]["coffee_spent"] == "100"
