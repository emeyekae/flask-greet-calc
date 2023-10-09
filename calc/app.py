
from flask import Flask, request
from operations import add, sub ,mult ,div

app=Flask(__name__)

@app.route("/add")
def go_add():
    """Add a and b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return(str(result))

@app.route("/sub")
def go_sub():
    """Subtract a from  b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return(str(result))

@app.route("/mult")
def go_mult():
    """Multiply a and b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return(str(result))

@app.route("/div")
def go_div():
    """Divide a by  b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return(str(result))

fun = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<op>")
def asmd(op):
    """Handle add, sub, mult and div in one function"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = fun[op](a, b)
    return(str(result))
