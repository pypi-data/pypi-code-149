import giacpy as g
from giacpy import giac, assume, pi, derive, factor, simplify, solve 

import subprocess
import shlex

print("HELLO FROM INSIDE")

# a, x,y,z = g.giac('a, x,y,z')
# g.assume('x>-pi && x<pi')
# l = g.solve('x^2-1=0',x)


def get_derivee(f:str,x:str):
    return simplify(derive(f,x))

def get_name_variable(fx: str):
    """ returns function name 'f', and function variable 'x'
    from string like "f(x)=x^3"
    """
    i_po = fx.index("(")
    i_pf = fx.index(")")
    i_eq = fx.index("=")
    if i_po < i_eq and i_pf < i_eq:
        return fx[:i_po], fx[i_po+1:i_pf]
    else:
        return "f", "x"

def get_latex(s:str):
    """ Converts Giac Expression to LaTex,
    AND then to python str,
    AND removes leading and tailing quotes,
    to be TeX-ready to be directly inserted in VarTables
    """
    return str(g.latex(s))[1:-1]

def escape_Tex_for_Python(s:str):
    newS = r""
    for c in s:
        if c == "{":
            c = r"{{"
        if c == "}":
            c = r"}}"
        newS += c
    return newS

def get_function_body(fx: str):
    """ returns function body 'x^3'
    from string like "f(x)=x^3"
    """
    i_eq = fx.index("=")
    return fx[i_eq+1:]

def get_solve(eqIneq:str, x:str)->list:
    return solve(eqIneq, x)
    # return g.resoudre(eqIneq, x)

def get_icas(command:str, content):
    # Start of Popen
    cmd_parts = [f"""icas '{command}'"""]
    i = 0
    p = {}
    for cmd_part in cmd_parts:
        try:
            cmd_part = cmd_part.strip()
            if i == 0:
                p[0]=subprocess.Popen(shlex.split(cmd_part),stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                p[i]=subprocess.Popen(shlex.split(cmd_part),stdin=p[i-1].stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            i += 1
        except Exception as e:
            err = str(e) + ' : ' + str(cmd_part)
            return (
                '<pre>Error : ' + err + '</pre>'
                '<pre>' + content + '</pre>').split('\n')
    (output, err) = p[i-1].communicate()
    exit_code = p[0].wait()
    output = output.decode("utf-8")
    i_co = output.index("list[")
    i_cf = output.index("]")
    # str to list
    output = output[i_co+5:i_cf+1].split(",")
    # list to Pygen.list
    output = giac(output)    
    return output

def get_xValuesInInterval(fpx:str, x:str, a:str , b:str)->list:
    fpx = factor(simplify(fpx))
    x = giac(f"{x}")
    # print(f"{x}>={a} && {x}<{b}")
    assume(f"{x}>={a} && {x}<={b}")
    return solve(f"{fpx}*({x}-{a})*({x}-{b})=0", x)
    # return g.resoudre(eqIneq, x)

def get_factor(s:str):
    return factor(s)

def tkzTabTexFrom(xValuesTex:list)->str:
    """prepares xValues for insertion into TkzTab VarTable
    """
    xValues = r""
    for value in xValuesTex:
        value = escape_Tex_for_Python(value)
        xValues += rf"""${value}$, """
    xValues = xValues.rstrip(" ")[:-1]
    xValues = rf"""{{{xValues}}}"""
    return xValues

def split_interval(interval):
    I = interval
    i_eq = I.index("=") if "=" in I else -1
    if i_eq >= 0:
        I = I[I.index("="):]
    i_comma = I.index(",") if "=" in I else -1
    if i_comma >= 0:
        I.replace(",", ";")
    openLeft = True if I[0] == "]" else False
    openRight = True if I[-1] == "[" else False
    I = I[1:-1]
    i_sep = I.index(";")
    a = I[:i_sep]
    b = I[i_sep+1:]
    # a = g.latex(a)
    # b = g.latex(b)
    return openLeft, a, b, openRight

if __name__ == "__main__":
    fprime = get_derivee("x^2")
    print("Hey")

