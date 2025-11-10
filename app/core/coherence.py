from typing import List
import json, os
from app.core.constants import DATA_DIR

with open(os.path.join(DATA_DIR, "regras_coerencia_exame.json"), "r", encoding="utf-8") as f:
    RULES = json.load(f)

def exam_label(exams: list) -> str:
    labels = []
    for e in exams:
        labels.append(RULES.get(f"E{e}", {}).get("nome", f"E{e}"))
    return " + ".join(labels) if labels else "Não informado"

def needs_e3_note(exams: list) -> bool:
    return "3" in exams and bool(RULES.get("E3", {}).get("nota_correcao"))
