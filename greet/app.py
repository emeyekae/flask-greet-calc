from flask import Flask, request

app=Flask(__name__)

@app.route("/welcome")
def welcome():
    return f'welcome'
"""Returns  'welcome'"""

@app.route("/welcome/home")
def welcomehome():
    return f'welcome home'
"""Returns 'welcome home'"""


@app.route("/welcome/back")
def welcomeback():
    return f'welcome back'
"""Returns 'welcome back"""
