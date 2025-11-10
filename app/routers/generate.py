from fastapi import APIRouter
from pydantic import BaseModel
from app.core.parser import parse_input
from app.core.validator import validate_commands
from app.core.renderer import render_report

router = APIRouter()

class GenerateBody(BaseModel):
    input: str

@router.post("/generate")
def generate(body: GenerateBody):
    commands = parse_input(body.input)
    validate_commands(commands)
    laudo, notes, warnings = render_report(commands)
    return {"laudo": laudo, "notes": notes, "warnings": warnings}
