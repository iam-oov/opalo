def convert_bool(cad):
    return cad in ['true', '1', 'True', 1]

def convert_float(cad):
    return float(str(cad).replace(',', ''))