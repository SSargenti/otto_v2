class OttoError(Exception):
    pass

class MissingExamError(OttoError):
    def __init__(self):
        super().__init__("Tipo de exame (E) não informado.")

class UnknownCodeError(OttoError):
    def __init__(self, code: str):
        super().__init__(f"Código [{code}] não encontrado. Verifique o manual de diagnósticos.")
