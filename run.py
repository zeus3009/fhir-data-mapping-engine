from engine.loader import load_json
from engine.transformer import transform
from engine.validator import is_valid_fhir

INPUT_FILE = "input_samples/provider_source.json"
TEMPLATE_FILE = "liquid_templates/practitioner.liquid"
OUTPUT_FILE = "output_fhir/practitioner.fhir.json"

def main():
    source = load_json(INPUT_FILE)
    fhir_output = transform(source, TEMPLATE_FILE)

    if not is_valid_fhir(fhir_output):
        raise ValueError("Generated FHIR JSON is invalid")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(fhir_output)

    print("FHIR Practitioner resource generated successfully.")

if __name__ == "__main__":
    main()
