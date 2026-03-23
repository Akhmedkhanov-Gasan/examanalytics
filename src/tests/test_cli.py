from examanalytics.cli import parse_args


def test_cli_args(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["prog", "--files", "a.csv", "b.csv", "--report", "median-coffee"],
    )

    args = parse_args()

    assert args.files == ["a.csv", "b.csv"]
    assert args.report == "median-coffee"
