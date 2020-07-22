from hello import hello

def test_hello_default(capsys):
    hello()
    out, err = capsys.readouterr()
    assert out == "Hello, world.\n"

def test_hello_with_name(capsys):
    hello("foo")
    hello("bar")
    out, err = capsys.readouterr()
    assert out == "Hello, foo.\n" "Hello, bar.\n"
