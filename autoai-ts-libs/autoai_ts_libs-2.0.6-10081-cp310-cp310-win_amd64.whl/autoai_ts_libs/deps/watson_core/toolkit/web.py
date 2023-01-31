# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Web client for handling outgoing requests. Mainly used by model_manager.py
"""
import urllib.error

from autoai_ts_libs.deps.watson_core.toolkit import alog
from autoai_ts_libs.deps.watson_core.toolkit.errors import error_handler
from tqdm.auto import tqdm

log = alog.use_channel("TLKIT")
error = error_handler.get(log)


class WebClient:
    """WebClient to make simple REST requests for a given url/username/password."""

    @staticmethod
    @alog.logged_function(log.debug2)
    def request(
        url,
        username=None,
        password=None,
        headers=None,
        filename=None,
        timeout=900,
        method="GET",
    ):
        """Make a request to a url with optional username/password authentication.

        Args:
            url: str
                URL to make request to. Should be full path, the method will not alter URL.
            username:
                Username to authenticate the request if needed
            password:
                Password to authenticate the request if needed
            headers:  dict
                Map of <key: value> to pass as headers.
            filename:  str
                String name of file to upload. Only byte-files are supported currently.
            timeout:  int
                Timeout of request. Default: 900 seconds (15 minutes).
            method:  str
                One of GET, POST, PUT.

        Returns:
            http.client.HTTPResponse
                NOT CLOSED! This function always returns an object which can work as a context
                manager and has methods such as:
                    * geturl() - return the URL of the resource retrieved, commonly used to
                        determine if a redirect was followed
                    * info() - return the meta-information of the page, such as headers, in the form
                        of an email.message_from_string() instance (see Quick Reference to HTTP
                        Headers)
                    * getcode() - return the HTTP status code of the response. Raises URLError on
                        errors.
                For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse object
                slightly modified.
            _io.BufferedReader or None
                Opened file if filename is provided, else None.
        """
        # set up args, kwargs that will be sent in request
        args = [urllib.request.Request(url, method=method)]
        kwargs = {"timeout": timeout}

        # authentication management
        if username is None or password is None:
            error("<COR07530365E>", ValueError("Please provide username & password."))

        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, uri=url, user=username, passwd=password)
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

        # will be used for making request/opening URL request
        opener = urllib.request.build_opener(handler)
        urllib.request.install_opener(opener)

        # optionally pass headers & filename
        if isinstance(headers, dict):
            opener.addheaders = list(headers.items())

        mmapped_file = None
        if isinstance(filename, str):
            # use mmap to avoid memory kills
            mmapped_file = open(filename, mode="rb")
            args.append(mmapped_file)

        response = urllib.request.urlopen(*args, **kwargs)
        return response, mmapped_file

    @staticmethod
    def request_chunks(
        full_url_path,
        username,
        password,
        file_zip,
        chunk_size=1000000,
        show_progress_bar=False,
    ):
        """Method to download a zip file and write in chunks

        Args:
            full_url_path: str
                File URL to download
            username:
                Username to authenticate the request
            password:
                Password to authenticate the request
            file_zip:
                Path where file zip is stored
            chunk_size: int
                Size of chunk to download - Defaults to 1MiB
            show_progress_bar: bool
                Whether we want to show a tqdm progress bar for the download

        Returns:
            str
                Path where zip is downloaded to
        """
        response, _ = WebClient.request(full_url_path, username, password)

        # write to .zip file in chunks to then be extracted
        # we use chunks so that we don't run into broken pipe, memory limits, etc. errors when
        #     downloading very large models
        try:
            with open(file_zip, mode="wb") as raw_fh:
                with tqdm.wrapattr(
                    raw_fh, "write", total=getattr(response, "length", None)
                ) if show_progress_bar else raw_fh as fh:
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        fh.write(chunk)
        finally:
            response.close()

        return file_zip
