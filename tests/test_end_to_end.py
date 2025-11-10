from app.core.parser import parse_input
from app.core.validator import validate_commands
from app.core.renderer import render_report

def test_end_to_end():
    s = "E 1 3\nF 43 / 15 25\nFRASE observação adicional"
    cmd = parse_input(s)
    validate_commands(cmd)
    laudo, notes, warnings = render_report(cmd)
    assert "Laudo de Radiografia(s)" in laudo
    assert "FRASE: observação adicional" in laudo
