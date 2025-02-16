import pytest
from src.template.main import main

def test_main(capfd):
    main()

    out, err = capfd.readouterr()
    assert out == "hello.\n"
    assert err is ''
