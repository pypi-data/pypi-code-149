from ._exceptions import DriveException
from ._sessions import Session


class Drive:
    def __init__(
        self,
        store_token: str,
        space_id: str,
        region: str,
        base_url: str = "https://drive.huddu.io",
    ) -> None:
        """
        This class provides a simple way to interface with the **Store API** in python
        The endpoint for the drive api is: https://drive.huddu.io
        :param store_token:
        :param space_id:
        :param region:
        :param base_url:
        """
        self.session = Session(
            headers={
                "Authorization": f"Token {store_token}",
                "X-Space": space_id,
                "X-Region": region,
            },
            base_url=base_url,
        )

    def upload(
        self, name: str, data: str = "", path: str = None, safe: bool = True
    ) -> None:
        """
        Upload a file with name by specifying one of data or path
        If safe is True (which it is by default). Files with the same name won't be overridden
        :param name:
        :param data:
        :param path:
        :param safe:
        :return:
        """
        if safe:
            if self.read(f"{name}__chunk__0"):  # check for first chunk
                raise DriveException("Another entry with the same id already exists")

        file_data = data
        if path:
            file_data = open(path).read()

        if not file_data:
            raise DriveException("One of data or path has to be specified")
        max_bytes = int(1e7)

        file_items = [
            file_data[i : i + max_bytes] for i in range(0, len(file_data), max_bytes)
        ]

        for i in range(0, len(file_items)):
            self.session.request(
                "POST",
                "/upload",
                data={
                    "name": f"{name}__chunk__{i}",
                    "data": file_items[i],
                },
            )

    def delete(self, name: str) -> None:
        """
        Delete a file by name
        :param name:
        :return:
        """
        has_more = True
        run = 0

        while has_more:
            try:
                self.session.request("DELETE", f"/{name}__chunk__{run}")
                run += 1
            except Exception:
                has_more = False

    def read_iterator(self, name: str):
        """
        Iterate over a file by name
        :param name:
        :return:
        """
        has_more = True
        run = 0

        while has_more:
            try:
                yield self.session.request("GET", f"/{name}__chunk__{run}")["data"]
                run += 1
            except Exception:
                has_more = False

    def read(self, name: str):
        """
        Read the entire file by name
        :param name:
        :return:
        """
        response = ""
        for i in self.read_iterator(name):
            response += i

        return response
