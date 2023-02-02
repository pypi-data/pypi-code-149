import re

def is_fun_declaration(line, fun_id):
    type_re = r"[a-z*&]+"
    id_re = r"[a-z_][a-z0-9_]*"
    param_re = r"({}\s+{})*".format(type_re, id_re)
    declaration_re = r"{}\s+{}(\(\)|\({}(\s*,\s*{})*\))\s*{{?".format(type_re, fun_id, param_re, param_re)
    return bool(re.match(declaration_re, line, re.IGNORECASE))    

def extract_fun(cpp, fun_id):
    in_declaration = False
    result = []
    for line in cpp.split("\n"):
        if is_fun_declaration(line, fun_id):
            in_declaration = True
            result.append(line)
            num_braces = line.count("{")
        else:
            if in_declaration:
                result.append(line)
                for c in line:
                    if c == "{":
                        num_braces += 1
                    elif c == "}":
                        num_braces -= 1
                if num_braces == 0:
                    in_declaration = False
                    return "\n".join(result)
    return ""
            
