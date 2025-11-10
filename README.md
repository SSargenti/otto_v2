# Otto v2 — Gerador de Laudos de Radiologia Odontológica

Gerador **determinístico** de laudos no **Formato A (Clássico)** com **modo estrito**, pronto para publicação no GitHub.
Sem dependência de serviços externos por padrão (sem LLMs na versão OSS).

## Principais recursos
- Parser de comandos `E` e `F` (e `FRASE`/`R`) com **validação estrita**.
- **Resolução canônica de diagnósticos** via `data/diagnosticos.json` (fonte única, inegociável).
- **Coerência por exame** via `data/regras_coerencia_exame.json` (E1, E2, E3, E4).
- **FRASES complementares imutáveis** (apenas correção linguística opcional), conforme política `config/otto_config.json`.
- Templates de frases em `data/frases.json` e bloco final padrão em `data/bloco_padrao_final.md`.
- API HTTP (FastAPI) e CLI para geração de laudos.
- Testes automatizados (pytest) e validações de esquema.

## Estrutura
```
otto_v2_repo/
├─ app/
│  ├─ main.py
│  ├─ routers/
│  │  └─ generate.py
│  └─ core/
│     ├─ parser.py
│     ├─ validator.py
│     ├─ coherence.py
│     ├─ renderer.py
│     ├─ errors.py
│     └─ constants.py
├─ config/
│  └─ otto_config.json
├─ data/
│  ├─ diagnosticos.json
│  ├─ regras_coerencia_exame.json
│  ├─ frases.json
│  ├─ bloco_padrao_final.md
│  └─ guia_unificado.md
├─ tests/
│  ├─ test_parser.py
│  ├─ test_validator.py
│  └─ test_end_to_end.py
├─ scripts/
│  └─ cli.py
├─ LICENSE
├─ SECURITY.md
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ .gitignore
└─ requirements.txt
```

## Rodando localmente
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# CLI:
python scripts/cli.py 'E 1 | F 53 73 / 18'
```

## API
`POST /generate` com JSON:
```json
{ "input": "E 1\nF 53 73 / 18 28\nFRASE imagem radiopaca bem delimitada..." }
```

Retorna:
```json
{ "laudo": "...texto..." , "warnings": [], "notes": [] }
```

## Licença
MIT — ver `LICENSE`.

## Aviso
Informação radiográfica é **complementar** à clínica. O uso deve seguir LGPD e boas práticas.
