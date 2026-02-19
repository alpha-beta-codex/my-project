from main import main
from main import VERSION


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


def test_main_prints_shout_default_name(capsys):
    code = main(["--shout"])
    captured = capsys.readouterr()
    assert code == 0
    assert captured.out.strip() == "HELLO, WORLD!"


def test_main_prints_shout_custom_name(capsys):
    code = main(["--name", "Ada", "--shout"])
    captured = capsys.readouterr()
    assert code == 0
    assert captured.out.strip() == "HELLO, ADA!"


def test_main_prints_version_with_v(capsys):
    code = main(["--v"])
    captured = capsys.readouterr()
    assert code == 0
    assert captured.out.strip() == VERSION


def test_main_prints_flags_with_h(capsys):
    code = main(["--h"])
    captured = capsys.readouterr()
    assert code == 0
    assert captured.out.strip() == "--name, --shout, --v, --h"
