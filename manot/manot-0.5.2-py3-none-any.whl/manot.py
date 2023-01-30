from typing import Literal, Union, Optional, List
from .upload_manager import UploadManager
from tqdm.notebook import tqdm
from .logger import log
import requests
import ipyplot
import json
import time


class manotAI:

    def __init__(self, url: str, token: str) -> None:
        self.__url = url.rstrip('/')
        self.__token = token

    def setup(
            self,
            data_provider: Literal['s3', 'local', 'deeplake'],
            arguments: dict
    ) -> Union[bool, dict]:
        """
        :param data_provider: Provider name, it must be 's3', 'local' or 'deeplake'.
        :param arguments: Request data to start setup process.

            If data_provider is 'deeplake', arguments must contain such values::
                name: str,
                detections_metadata_format: Literal['cxcywh', 'xywh', 'xyx2y2'],
                classes_txt_path: str,
                deeplake_token: str,
                data_set: str,
                detections_boxes_key: str,
                detections_labels_key: str,
                detections_score_key: str,
                ground_truths_boxes_key: str,
                ground_truths_labels_key: str,
                classes: Optional[list[str]]
            Otherwise:
                name: str,
                images_path: str,
                ground_truths_path: str,
                detections_path: str,
                detections_metadata_format: Literal['cxcywh', 'xywh', 'xyx2y2'],
                classes_txt_path: str,
        """

        url = f"{self.__url}/api/v1/setup/"
        if data_provider == "deeplake":
            url = f"{url}deeplake"

        arguments.update({"data_provider": data_provider})

        try:
            response = requests.post(url=url, data=json.dumps(arguments), headers={"token": self.__token})
        except Exception:
            log.error("There is problem with request.")
            return False

        if response.status_code == 202:
            log.info("Setup is being prepared to be started.")
            if self.__check_progress(self.get_setup, response.json()["id"]):
                log.info("Setup has successfully created.")
            else:
                log.error(f'There is problem setup process with id {response.json()["id"]}.')

            return response.json()

        log.error(response.text)
        return False

    def get_setup(self, setup_id: int) -> Union[bool, None, dict]:

        url = f"{self.__url}/api/v1/setup/{setup_id}"

        try:
            response = requests.get(url=url)
        except Exception:
            log.error("There is problem with request.")
            return False

        if response.status_code != 200:
            log.warning("Setup not found.")
            return None

        return response.json()

    def insight(
            self,
            name: str,
            setup_id: int,
            data_path: Union[str, List[str]],
            data_provider: Literal['s3', 'local', 'deeplake'],
            weight_name: Optional[str] = None,
            deeplake_token: Optional[str] = None,
    ) -> Union[bool, dict]:

        url = f"{self.__url}/api/v1/insight/"
        data = {
            "name": name,
            "setup_id": setup_id,
            "data_path": data_path,
            "data_provider": data_provider,
            "deeplake_token": deeplake_token
        }
        if weight_name:
            data["weight_name"] = weight_name

        try:
            response = requests.post(url=url, data=json.dumps(data), headers={"token": self.__token})
        except Exception:
            log.error("There is problem with request.")
            return False

        if response.status_code == 202:
            log.info("Insights process is successfully started.")
            return response.json()

        log.error(response.text)
        return False

    def get_insight(self, insight_id: int) -> Union[bool, None, dict]:

        url = f"{self.__url}/api/v1/insight/{insight_id}"

        try:
            response = requests.get(url=url)
        except Exception:
            log.error("There is problem with request.")
            return False

        if response.status_code != 200:
            log.warning("Insight not found.")
            return None

        log.info("Insight is successfully found.")
        return response.json()


    def visualize_data_set(self, data_set_id: int):
        url = f"{self.__url}/api/v1/data_set/{data_set_id}"

        try:
            response = requests.get(url=url).json()
        except Exception:
            log.error("There is problem with request.")
            return False

        if not response:
            log.warning("Data Set not found.")
            return None

        images = response['data_set_images']
        images_urls = []
        for file in images:
            images_urls.append(self.__process(file['id']))

        return ipyplot.plot_images(images_urls, img_width=200, show_url=False)


    def upload_data(self, dir_path: str, process: Literal["setup", "insight"]):

        upload_manager = UploadManager(directory=dir_path, url=self.__url, token=self.__token)
        if process == "setup":
            return upload_manager.upload_setup_data()
        elif process == "insight":
            return upload_manager.upload_insight_data()
        else:
            log.error("Process must be 'setup' or 'insight'.")
            return False


    def calculate_map(
            self,
            ground_truths_path: str,
            detections_path: str,
            classes_txt_path: str,
            data_provider: Literal['s3', 'local'],
            data_set_id: Optional[int] = None
    ):
        url = f"{self.__url}/api/v1/map/"
        data = {
            "ground_truths_path": ground_truths_path,
            "detections_path": detections_path,
            "classes_txt_path": classes_txt_path,
            "data_provider": data_provider,
            "data_set_id": data_set_id
        }

        try:
            response = requests.post(url=url, data=json.dumps(data), headers={"token": self.__token})
        except Exception:
            log.error("There is problem with request.")
            return False

        if response.status_code == 200:
            log.info("mAP has successfully calculated.")
            return response.json()

        log.error(response.text)
        return False


    def __process(self, image_id: int):
        url = f"{self.__url}/api/v1/image/{image_id}"
        return url


    def __check_progress(self, process_method, id):
        progress = 0
        progress_bar = tqdm(desc="Progress", total=100)
        while progress < 100:
            result = process_method(id)
            if result and result["status"] != "failure":
                progress_bar.update(result['progress'] - progress)
                progress = result['progress']
            else:
                progress_bar.close()
                return False
            time.sleep(2)
        progress_bar.close()
        return True
