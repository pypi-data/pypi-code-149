def content_type_from_model(name: str) -> str:
    return f'application/vnd.adobe.dc+json; profile="https://dc-api.adobe.io/schemas/{name}.json"'


def build_content_type(*types: str) -> str:
    return ";".join(types)
