from flask import Flask, request, send_from_directory
import wandb
import json
import logging
from flask_cors import cross_origin
import pandas as pd  # imported to avoid a bug in wandb
import pathlib

app = Flask(__name__)

logging.getLogger("flask_cors").level = logging.DEBUG

api = wandb.Api()

build_directory = pathlib.Path(__file__).parent.absolute() / "build"


@app.route("/wandb")
@cross_origin()
def wandb_run():
    run = request.args.get("run")
    run = api.run(run)
    config = run.config
    history = run.history()

    # Return a JSON with config and history fields
    return {"config": config, "history": json.loads(history.to_json(orient="records"))}


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory(str(build_directory), "index.html")


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory(str(build_directory), path)


def main():
    app.run()


if __name__ == "__main__":
    main()
