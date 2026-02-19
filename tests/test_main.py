from main import main


def test_main_prints_default(capsys):
    code = main([])
    captured = capsys.readouterr()
    assert code == 0
    assert captured.out.strip() == "Hello, world!"


def test_main_prints_name(capsys):
    code = main(["--name", "Ada"])
    captured = capsys.readouterr()
    assert code == 0
    assert captured.out.strip() == "Hello, Ada!"