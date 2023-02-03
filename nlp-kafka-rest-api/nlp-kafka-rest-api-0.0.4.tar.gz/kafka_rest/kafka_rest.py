import base64
import json
import os
import time
from typing import Any, Dict, List, Optional, Union, Collection
from uuid import uuid4

import requests


class Client:
    def __init__(self, kafka_rest_api_url: Optional[str] = None, auth_headers: Optional[Dict[str, str]] = None):
        """
        Create a client instance.
        :param kafka_rest_api_url: Kafka REST API URL.
        :param auth_headers: Authentication Headers.
        """
        self.kafka_rest_api_url = os.environ['KAFKA_REST_API_URL'] if not kafka_rest_api_url else kafka_rest_api_url
        self.auth_headers = auth_headers

    def request(self, **kwargs):
        kwargs["url"] = f"{self.kafka_rest_api_url}{kwargs['url']}"
        if self.auth_headers:
            kwargs.get("headers", {}).update(self.auth_headers)

        response = requests.request(**kwargs)

        if not response.ok:
            print(response.content)
            response.raise_for_status()

        return response


class Producer(Client):
    def __init__(self, producer_data_max_size: int = 67_108_864, **kwargs):
        """
        Create a producer instance.
        :param producer_data_max_size: Maximum size of each request payload in bytes.
        :param kwargs:
            kafka_rest_api_url: Provide a Kafka REST Proxy API URL if it is not set as environment variable.
            auth_headers: Optional dictionary of authentication headers.
        """
        super().__init__(kwargs.get("kafka_rest_api_url", ""), kwargs.get("auth_headers"))

        self.max_data_bytes = os.environ.get('PRODUCER_DATA_MAX_SIZE', producer_data_max_size)
        self.key_history, self.key_last_request = [], []

    @staticmethod
    def __manage_keys(len_messages: int, keys: Optional[List[str]] = None):
        if keys:
            try:
                assert len(keys) == len_messages
            except AssertionError:
                raise ValueError("List of keys must have the same size as list of messages.")
            return keys

        return [str(uuid4()) for _ in range(len_messages)]

    def produce(self, messages: Collection, topic: str, keys: Optional[List[str]] = None) -> List[str]:
        """
        Produce messages to a given topic.
        :param messages: JSON serializable Collection of messages.
        :param topic: Corresponding topic.
        :param keys: Optional list of customized keys. Number of keys must match the number of messages.
        :return: List of generated UUID keys.
        """
        headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}
        keys = self.__manage_keys(len(messages), keys)
        records = {"records": [{"key": k, "value": v} for k, v in zip(keys, messages)]}
        record_data = json.dumps(records)

        self._check_data_size(record_data.encode("utf-8"))

        self.request(method="POST", url=f"/topics/{topic}", headers=headers, data=record_data)

        self.key_history.extend(keys)
        self.key_last_request = keys
        return self.key_last_request

    def _check_data_size(self, data: bytes):
        if self.max_data_bytes < len(data):
            raise RuntimeError(f"Producer request data exceeded allowed number bytes: {self.max_data_bytes} bytes")

    def produce_files(self, files: Collection, topic: str, file_max_size: int = 500_000, keys: Optional[List[str]] = None) -> List[str]:
        """
        Produce files to a given topic.
        :param files: List of dictionaries with keys:
                       - name: string with filename.
                       - bytes: bytes.
                       - type: string with type. (optional)
        :param topic: Target topic.
        :param file_max_size: Maximum file size in bytes.
        :param keys: Optional list of customized keys. Number of keys must match the number of messages.
        :return: List of generated UUID keys.
        """

        assert all(
            isinstance(field, str) if field == "name" else (
                field == "bytes" and file[field] <= file_max_size if isinstance(field, bytes) else True)
            for file in files for field in file) is True

        assert all(len(file["bytes"]) for file in files)

        messages = [
            {
                "name": f["name"],
                "bytes": base64.b64encode(f["bytes"]).decode(),
                "type": f["type"]
            } for f in files]

        return self.produce(messages, topic, keys=keys)


class Consumer(Client):
    def __init__(self, **kwargs):
        """
        Create a consumer instance.
        :param kwargs:
            kafka_rest_api_url: Provide a Kafka REST Proxy API URL if it is not set as environment variable.
            auth_headers: Optional dictionary of authentication headers.
            topics: List of topics to consume messages from.
            consumer_group: Assign a consumer group name. Otherwise, assign a randomly generated UUID.
            instance: Assign an instance name. Otherwise, assign a randomly generated UUID.
        """
        super().__init__(kwargs.get("kafka_rest_api_url", ""), kwargs.get("auth_headers"))

        self.created = False

        self.topics = kwargs.get("topics", [])
        self.consumer_group = kwargs.get("consumer_group", str(uuid4()).replace("-", ""))
        self.instance = kwargs.get("instance", str(uuid4()).replace("-", ""))
        self.remaining_keys = set()

    def __enter__(self):
        return self.create().subscribe(self.topics)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delete()

    def create(self):
        """
        Create a Consumer instance in binary format.
        :return: self.
        """

        if not self.created:
            url = f"/consumers/{self.consumer_group}"
            headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}
            config = json.dumps({"name": self.instance, "format": "binary", "auto.offset.reset": "earliest"})

            response = self.request(method="POST", url=url, headers=headers, data=config)
            self.created = True

        return self

    def subscribe(self, topics: List[str]):
        """
        Subscribe to the given topics.
        :param topics: List of topics to consume messages from.
        :return: self.
        """

        if not topics:
            raise ValueError("No topics to subscribe to.")

        self.topics = topics
        url = f"/consumers/{self.consumer_group}/instances/{self.instance}/subscription"
        headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}
        topics_data = json.dumps({"topics": self.topics})

        r = self.request(method="POST", url=url, headers=headers, data=topics_data)
        return self

    def consume_earliest(self) -> List[Dict[str, Any]]:
        """
        Consume the earliest messages in the assigned topics.
        :return: List of dictionaries where the "value" key contains the message and the "key" key contains its key.
        """
        url = f'/consumers/{self.consumer_group}/instances/{self.instance}/records'
        headers = {'Accept': 'application/vnd.kafka.binary.v2+json'}

        response = self.request(method="GET", url=url, headers=headers, data="")
        response_decoded = [self.decode_record(r) for r in response.json()]

        return response_decoded

    def delete(self):
        """
        Delete the current client instance from the kafka cluster.
        """
        url = f'/consumers/{self.consumer_group}/instances/{self.instance}'
        headers = {'Content-Type': 'application/vnd.kafka.v2+json'}

        self.request(method="DELETE", url=url, headers=headers, data="")
        self.created = False

    def consume(self, keys: List[str], interval_sec: Union[int, float] = 5) -> List[dict]:
        """
        Consume messages from the assigned topics as iterator.
        :param keys: List of keys to choose from the topics.
        :param interval_sec: Minimum interval in seconds between polling requests.
        :return: List of dictionaries where the "value" key contains the message and the "key" key contains its key.
        """

        if interval_sec < 0:
            raise ValueError("'interval_sec' should be an 'int' or 'float' greater or equal to 0.")

        self.remaining_keys = set(keys)

        while self.remaining_keys:
            time.sleep(interval_sec)
            incoming_data = self.consume_earliest()
            data = [d for d in incoming_data if d['key'] in self.remaining_keys]
            yield data
            self.remaining_keys = self.remaining_keys - set(d['key'] for d in incoming_data)

    def consume_all(self, keys: List[str], interval_sec: Union[int, float] = 5) -> List[Dict[str, Any]]:
        """
        Consume all messages from all keys.
        :param keys: List of keys to choose from the topics.
        :param interval_sec: Minimum interval in seconds between polling requests.
        :return: List of dictionaries where the "value" key contains the message and the "key" key contains its key.
        """
        all_data = []

        for data in self.consume(keys, interval_sec):
            all_data.extend(data)

        return all_data

    @staticmethod
    def decode_base64(string: str):
        if string:
            try:
                return json.loads(base64.b64decode(string))
            except json.decoder.JSONDecodeError:
                return base64.b64decode(string)
        return string

    @staticmethod
    def decode_record(record: dict):
        record.update({
            "key": Consumer.decode_base64(record["key"]),
            "value": Consumer.decode_base64(record["value"])
        })

        return record


if __name__ == "__main__":

    import pprint

    producer_messages = [
        {
            "text": "Genome engineering is a powerful tool for a wide range of applications in biomedical research",
            "algorithm": "TopicRank",
            "n_best": 10
        },
        {
            "text": "Genome engineering is a powerful tool for a wide range of applications in biomedical research",
            "algorithm": "TopicRank",
            "n_best": 5
        }
    ]

    # # Auth Headers

    x_api_key = os.environ['X_API_KEY']
    user_agent = os.environ['USER_AGENT']
    auth_headers = {"x-api-key": x_api_key, "User-Agent": user_agent}

    print("Kafka URL:", os.environ["KAFKA_REST_API_URL"])

    target_topic = "pke"

    # Producer

    print("\n", " Producer ".center(100, "#"), end="\n\n")
    print(f"Send these messages to topic '{target_topic}':", "\n", pprint.pformat(producer_messages, indent=4), "\n")

    producer = Producer(auth_headers=auth_headers)
    new_keys = producer.produce(producer_messages, target_topic)

    print(f"The producer generated these message keys:", "\n", pprint.pformat(new_keys, indent=4))

    # Consumer
    interval_sec = 5

    # Pattern 1 - Instantiation via context manager

    print("\n", " Pattern 1 - Step-by-step instantiation ".center(100, "#"), end="\n\n")

    with Consumer(topics=["pke-response"], auth_headers=auth_headers) as c:
        print(f"Consumer instance '{c.instance}' checks every {interval_sec} second{'s' if interval_sec != 1 else ''}",
              f"and consumes all keys ({', '.join(new_keys)})")
        new_data = c.consume_all(new_keys, interval_sec=interval_sec)

    print("Response Data:", pprint.pformat(new_data, indent=4))

    # ## Pattern 2 - Step-by-step instantiation

    print("\n", " Pattern 2 - Step-by-step instantiation ".center(100, "#"), end="\n\n")

    consumer = Consumer(auth_headers=auth_headers)

    print("Create consumer instance...")
    consumer.create()

    print(f"New consumer instance: '{consumer.instance}'.")

    print(f"Subscribe to topic{'s' if len(target_topic) > 1 and isinstance(target_topic, list) else ''}:",
          f"{', '.join(target_topic) if type(target_topic) in [list, set, tuple] else target_topic}")
    consumer.subscribe(topics=["pke-response"])

    print(f"Produce data to topic '{target_topic}'...")
    keys = producer.produce(producer_messages, target_topic)

    print(f"Consume data every {interval_sec} seconds...")
    consumed_data = consumer.consume_all(keys=keys, interval_sec=interval_sec)  # or consumer.create().subscribe().consume_all(keys)
    print("Response Data:", "\n", pprint.pformat(consumed_data, indent=4))

    print("Delete consumer to release resources...")
    consumer.delete()

    # ## Pattern 3 - Consumer with iterator

    print("\n", " Pattern 3 - Consumer with iterator ".center(100, "#"), end="\n\n")

    new_keys = producer.produce(producer_messages, target_topic)

    with Consumer(topics=["pke-response"], auth_headers=auth_headers) as consumer:
        print(f"Data from consumer instance '{consumer.instance}'",
              f"(every {interval_sec} second{'s' if interval_sec != 1 else ''}):")

        for i, iter_data in enumerate(consumer.consume(new_keys, interval_sec=1)):
            print(f"Data in iteration {i}:", "\n", pprint.pformat(iter_data, indent=4))

            if iter_data:
                print("Do something with the data...", "\n", "Continue...")
        print("Iteration finished because all keys were processed!")

    print("\n", " Producer with files ".center(100, "#"), end="\n\n")

    file_names = ["test_1.pdf", "test_2.pdf", "test_3.pdf"]

    messages = []
    for name in file_names:
        with open(f"snippet/{name}", "rb") as f:
            messages.append({"name": name, "bytes": f.read(), "type": "application/pdf"})

    target_topic = "pdf2text"

    print(f"Sending files '{', '.join(file_names)}' to topic '{target_topic}'...")

    producer = Producer(auth_headers=auth_headers)
    new_keys = producer.produce_files(messages, target_topic)

    print(f"Consuming responses...")

    with Consumer(topics=[f"{target_topic}-response"], auth_headers=auth_headers) as consumer:
        for i, iter_data in enumerate(consumer.consume(new_keys, interval_sec=1)):
            print(f"Response in iteration {i}:", "\n", pprint.pformat(iter_data, indent=4))

            if iter_data:
                print("Do something with the data...", "\n", "Continue...")
        print("Iteration finished because all keys were processed!")

    print("#" * 100, "\n\n", "-> Snippet finished!")
