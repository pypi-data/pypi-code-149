import argparse
from .Loader import Loader
from revChatGPT.Official import Chatbot

class FinGen:
    @staticmethod
    def CreateFinding(api_key, titles):
        chatbot = Chatbot(api_key=api_key)

        for title in titles:
            loader = Loader("Thinking...", "").start()
            prompt = (
                "Write me a penetration testing finding about " + title + "." 
                "It should contain a description and remediation section. "
                "It should also have a risk rating based on the likelihood and impact of exploitation."
            )
            message = chatbot.ask(prompt)
            loader.stop()
            print(message["choices"][0]["text"])
            print("")

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FinGen CLI", prog="python -m FinGen")
    parser.add_argument(
        "-t",
        "--title",
        required=True,
        action='append',
        help="Finding Title",
    )
    parser.add_argument(
        "-k",
        "--api_key",
        type=str,
        required=True,
        help="OpenAI API key",
    )
    return parser

def main(args):
    FinGen.CreateFinding(args.api_key, args.title)

if __name__ == "__main__":
    main(get_parser().parse_args())