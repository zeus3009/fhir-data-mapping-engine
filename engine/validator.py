import json

def is_valid_fhir(fhir_json_str: str) -> bool:
    try:
        json.loads(fhir_json_str)
        return True
    except json.JSONDecodeError:
        return False
