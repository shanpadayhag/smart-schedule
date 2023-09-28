def getNestedValue(object: dict, keys: list):
    value = object

    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        elif isinstance(value, list) and isinstance(key, int) and key < len(value):
            value = value[key]
        else:
            return None

    return value
