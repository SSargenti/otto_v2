import json, os
from typing import Dict
from app.core.errors import MissingExamError, UnknownCodeError
from app.core.constants import DATA_DIR, CONFIG_FILE

def _load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

DIAG = None
CFG = None
RULES = None

def bootstrap():
    global DIAG, CFG, RULES
    if DIAG is None:
        DIAG = _load_json(os.path.join(DATA_DIR, "diagnosticos.json"))
    if CFG is None:
        CFG = _load_json(CONFIG_FILE)
    if RULES is None:
        RULES = _load_json(os.path.join(DATA_DIR, "regras_coerencia_exame.json"))

def validate_commands(cmd: Dict):
    bootstrap()
    if not cmd.get("E"):
        raise MissingExamError()
    for block in cmd.get("blocks", []):
        if block["type"] == "F":
            for code in block.get("codes", []):
                if not code.isdigit():
                    continue
                if code not in DIAG:
                    raise UnknownCodeError(code)
