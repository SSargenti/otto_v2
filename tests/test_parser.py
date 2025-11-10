from app.core.parser import parse_input

def test_parse_basic():
    s = "E 1\nF 4 [[m]] / 37\nFRASE achado complementar"
    out = parse_input(s)
    assert out["E"] == ["1"]
    assert out["blocks"][0]["codes"] == ["4"]
    assert out["blocks"][0]["teeth"] == ["37"]
    assert out["blocks"][1]["type"] == "FRASE"
