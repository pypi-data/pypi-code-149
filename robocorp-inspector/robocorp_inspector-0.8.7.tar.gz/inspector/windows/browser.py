import os
import signal
import psutil  # type: ignore
from inspector_commons.bridge.bridge_browser import BrowserBridge  # type: ignore
from inspector.windows.base import Window


class BrowserWindow(Window):
    BRIDGE = BrowserBridge
    DEFAULTS = {
        "title": "Robocorp - Web Locators",
        "url": "browser.html",
        "width": 480,
        "height": 0,
        "on_top": True,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._force_closing = False

    def on_closing(self):
        super().on_closing()

        self.logger.debug("The Browser PID (on closing): %s", self._bridge.browser_pid)
        if self._bridge.browser_pid:
            browser_proc = psutil.Process(self._bridge.browser_pid)
            if browser_proc.is_running():
                self.logger.debug("The Browser seems to be running. Killing it...")
                for child in browser_proc.children(recursive=True):
                    try:
                        self.logger.debug("Stopping child process: %s", child.pid)
                        os.kill(child.pid, signal.SIGTERM)
                        child.kill()
                    except Exception:  # pylint: disable=W0703
                        pass
                self.logger.debug("Finished stopping browser child processes!")
                self.logger.debug("Killing main process...")
                browser_proc.kill()

        self.logger.debug("Final Exit...")
        # force closing the entire app if the close app button is pressed
        os._exit(0)  # pylint: disable=protected-access
