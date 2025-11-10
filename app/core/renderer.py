import os
from typing import Dict, List
from app.core.coherence import exam_label, needs_e3_note
from app.core.constants import DATA_DIR
from app.core.validator import bootstrap, DIAG

def _load(path): 
    with open(path, "r", encoding="utf-8") as f: 
        return f.read()

def render_report(cmd: Dict):
    bootstrap()
    exams = cmd.get("E", [])
    titulo = f"Laudo de Radiografia(s) {exam_label(exams)}."
    analise_rows = []
    notes = []
    warnings = []

    for block in cmd.get("blocks", []):
        if block["type"] == "F":
            nomes = [DIAG[c]["nome"] for c in block.get("codes", []) if c.isdigit() and c in DIAG]
            analise_rows.append({"comando":"F","diagnosticos":nomes,"dentes":block.get("teeth", []),"notas":block.get("notes", [])})
        else:
            analise_rows.append({"comando":"FRASE","texto":block.get("text","")})

    nota_correcao = None
    if needs_e3_note(exams):
        nota_correcao = "Nota de Correção: O exame interproximal não avalia porções radiculares; os achados foram descritos considerando apenas coroas e cristas alveolares."

    frases_out = []
    for block in cmd.get("blocks", []):
        if block["type"] == "FRASE":
            t = block.get("text","").strip()
            if t:
                frases_out.append(f"- {t[0].upper() + t[1:]}")
        else:
            dentes = " ".join(block.get("teeth", [])) or "região informada"
            nomes = [DIAG[c]["nome"] for c in block.get("codes", []) if c.isdigit() and c in DIAG]
            notas = " ".join(block.get("notes", []))
            nomes_txt = "; ".join(nomes)
            frases_out.append(f"- {nomes_txt} em {dentes}. {('Notas: ' + notas) if notas else ''}".strip())

    bloco_final = _load(os.path.join(DATA_DIR, "bloco_padrao_final.md")).strip()

    linhas = [f"## {titulo}", "", "### Análise Diagnóstica"]
    for r in analise_rows:
        if r["comando"] == "F":
            linhas.append(f"- F: {', '.join(r['diagnosticos'])} / {', '.join(r['dentes'])} {('[' + ' '.join(r['notas']) + ']') if r['notas'] else ''}")
        else:
            linhas.append(f"- FRASE: {r['texto']}")
    if nota_correcao:
        linhas.append("")
        linhas.append("### Nota de Correção")
        linhas.append(nota_correcao)
    linhas.append("")
    linhas.append("### Sugestão e Recomendação")
    linhas.append("```")
    linhas.extend(frases_out)
    linhas.append(bloco_final)
    linhas.append("```")
    return "\n".join(linhas), notes, warnings
