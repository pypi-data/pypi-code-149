import logging
import os
import uuid

import logging_loki

from blazetest.core.config import LOKI_URL, CWD


def setup_logging(
    debug: bool = False,
    stdout_enabled: bool = True,
    loki_api_key: str = None,
    session_uuid: str = uuid.uuid4(),
):
    """
    Sets up basic logging.
    If stdout_enabled, stdout is shown to the user. Otherwise, saved to the file.
    If loki_api_key is provided, logs are sent to Loki.
    """
    level = logging.DEBUG if debug else logging.INFO

    handlers = None
    if loki_api_key:
        logging_loki.emitter.LokiEmitter.level_tag = "level"
        handler = logging_loki.LokiHandler(
            url=LOKI_URL.format(loki_api_key=loki_api_key),
            tags={"service": "blazetest", "session_uuid": session_uuid},
            version="1",
        )
        handlers = [handler]

    if stdout_enabled:
        logging.basicConfig(
            format="%(process)d-%(levelname)s-%(message)s",
            level=level,
            handlers=handlers,
        )
    else:
        logging.basicConfig(
            filename=os.path.join(CWD, "blazetest.log"),
            format="%(process)d-%(levelname)s-%(message)s",
            level=level,
            handlers=handlers,
        )
