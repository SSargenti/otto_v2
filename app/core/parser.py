import re
from typing import List, Dict

def normalize_voice(s: str) -> str:
    repl = {" e ": " E ", " efe ": " F ", " frase ": " FRASE ", " Frase ": " FRASE "}
    o = " " + s + " "
    for k, v in repl.items():
        o = o.replace(k, v)
    return o.strip()

def parse_input(s: str) -> Dict:
    s = normalize_voice(s)
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    result = {"E": [], "blocks": []}
    for ln in lines:
        if ln.upper().startswith("E"):
            payload = ln[1:].strip()
            exams = [x.strip() for x in re.split(r"[ ,]+", payload) if x.strip()]
            result["E"] = exams
        elif ln.upper().startswith("FRASE"):
            text = ln.split(" ", 1)[1] if " " in ln else ""
            result["blocks"].append({"type": "FRASE", "text": text})
        elif ln.upper().startswith("F"):
            body = ln[1:].strip()
            parts = [p.strip() for p in body.split("/")]
            left = parts[0]
            right = parts[1] if len(parts) > 1 else ""
            tokens = [t for t in re.split(r"[ ]+", left) if t]
            codes, notes = [], []
            for t in tokens:
                if t.startswith("[[") and t.endswith("]]"):
                    notes.append(t.strip("[]").strip())
                else:
                    codes.append(t)
            teeth = [t for t in re.split(r"[ ,]+", right) if t]
            result["blocks"].append({"type": "F", "codes": codes, "teeth": teeth, "notes": notes})
        else:
            result["blocks"].append({"type": "FRASE", "text": ln})
    return result
