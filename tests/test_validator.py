import pytest
from app.core.validator import validate_commands

def test_missing_E():
    with pytest.raises(Exception) as e:
        validate_commands({"blocks":[{"type":"F","codes":["4"],"teeth":["37"],"notes":[]}]})
    assert "Tipo de exame" in str(e.value)

def test_unknown_code():
    with pytest.raises(Exception) as e:
        validate_commands({"E":["1"],"blocks":[{"type":"F","codes":["999"],"teeth":["37"],"notes":[]}]})
    assert "Código [999]" in str(e.value)
