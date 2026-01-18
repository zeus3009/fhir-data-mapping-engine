from liquid import Template

def transform(source_data: dict, template_path: str) -> str:
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    template = Template(template_content)
    return template.render(**source_data)
