from typing import List
from powerml import PowerML
from powerml.utils.constants import MAX_TEMPLATE_TOKENS


class SummarizeTopicModel:
    '''
    This model removes duplicates and attempts to generate topics relevant
    to topic_type.
    '''

    def __init__(
            self,
            config={},):
        self.model = PowerML(config, "unblocked/summarize-topics")


    def predict(self, topic: str, documents: List[str],) -> str:
        document_string = ""
        for document in documents:
            if len(document_string) + len(document) > MAX_TEMPLATE_TOKENS:
                break
            document_string += document + "\n"
        prompt = {
            "{{documents}}": document_string,
            "{{topic}}": topic,
        }
        completion = self.model.predict(prompt)
        return self._post_process(completion)

    def _post_process(self, completion: str):
        return completion.strip()
       