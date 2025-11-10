import sys
from app.core.parser import parse_input
from app.core.validator import validate_commands
from app.core.renderer import render_report

def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/cli.py 'E 1 | F 53 73 / 18'")
        raise SystemExit(1)
    text = sys.argv[1].replace("|", "\n")
    cmd = parse_input(text)
    validate_commands(cmd)
    laudo, notes, warnings = render_report(cmd)
    print(laudo)

if __name__ == "__main__":
    main()
