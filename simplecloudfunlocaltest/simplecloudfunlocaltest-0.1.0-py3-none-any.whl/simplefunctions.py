from flask import Flask,request


def event_decorator(fun):
    import flask
    from google.cloud.functions_v1.context import Context
    def wrapper(*args):

        if(isinstance(args[0],flask.Request)):
            import json
            fun(json.loads(args[0].get_data()))
        if(isinstance(args[0],dict) and isinstance(args[1],Context)):
            fun(*args)
        return 
    return wrapper

def create_app(func_name,host,port,debug):

    app = Flask(__name__, instance_relative_config=True)
    
    import sys
    import os
    
    sys.path.append(os.getcwd())
    
    gcs_fun = getattr(__import__("main"), func_name)

    def wrapper_func():
        gcs_fun(request)
        return "Function has executed correctly."
    
    app.add_url_rule("/", view_func=wrapper_func)

    app.run(host,port,debug)