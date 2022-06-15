def test_hello_world(capfd):
    import hello_world
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n"
