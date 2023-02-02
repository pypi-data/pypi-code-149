import argparse
import io
import os
import sys

import speech_recognition as sr
import whisper
import torch

from datetime import datetime, timedelta
from queue import Queue
from tempfile import NamedTemporaryFile, gettempdir
from time import sleep, time
from sys import platform

from ffexec import get_ffmpeg_exe

os.environ["PATH"] += os.pathsep + os.path.join(os.path.dirname(__file__), 'bin')


def cli():
    parser = argparse.ArgumentParser(
        prog="stot", description="real-time transcription of speech to text using whisper"
    )
    parser.add_argument("-o", "--output", metavar="", default=None, help="output path")
    parser.add_argument(
        "--model",
        default="small",
        help="name of the whisper model to use",
        choices=whisper.available_models(),
    )
    parser.add_argument("--language", metavar="", default=None, help="language spoken in speech")
    parser.add_argument(
        "--energy_threshold",
        metavar="",
        default=1000,
        help="energy level for microphone to detect",
        type=int,
    )
    parser.add_argument(
        "--record_timeout",
        metavar="",
        default=2,
        help="how real-time the recording is lowering the value makes the recording more real-time",
        type=float,
    )
    parser.add_argument(
        "--phrase_timeout",
        metavar="",
        default=3,
        help="how much empty space between recordings before we consider it a new line in the transcription",
        type=float,
    )
    if "linux" in platform:
        parser.add_argument(
            "--default_microphone",
            metavar="",
            default="pulse",
            help="default microphone name run this with value 'list' to view available microphones",
            type=str,
        )

    return parser.parse_args().__dict__


def write_txt(transcription: list, output: str):
    if os.path.isdir(output):
        output = os.path.join(output, f"transcription_{time()}.txt")
    try:
        with open(output, "w", encoding="UTF-8") as f:
            f.write("\n".join(transcription))
    except PermissionError:
        print("Write permission denied, using TEMP directory as fallback.")
        output = os.path.join(gettempdir(), f"transcription_{time()}.txt")
        with open(output, "w", encoding="UTF-8") as f:
            f.write("\n".join(transcription))
    return output


def transcribe(
        output=None,
        model="small",
        language=None,
        energy_threshold=1000,
        record_timeout=2,
        phrase_timeout=3,
        default_microphone="pulse",
):
    gpu = torch.cuda.is_available()

    if not gpu:
        print("GPU not detected, using CPU.")

    print("Getting ready...")

    phrase_time = None
    last_sample = bytes()
    data_queue = Queue()
    recorder = sr.Recognizer()
    recorder.energy_threshold = energy_threshold
    recorder.dynamic_energy_threshold = False

    if "linux" in platform:
        if not default_microphone or default_microphone == "list":
            print("Available microphone devices are: ")
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                print(f'Microphone with name "{name}" found')
            return
        else:
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                if default_microphone in name:
                    source = sr.Microphone(sample_rate=16000, device_index=index)
                    break
    else:
        source = sr.Microphone(sample_rate=16000)

    model = whisper.load_model(model)

    temp_file = NamedTemporaryFile().name
    transcription = ['']

    with source:
        recorder.adjust_for_ambient_noise(source)

    def record_callback(_, audio: sr.AudioData) -> None:
        """
        Threaded callback function to recieve audio data when recordings finish.
        audio: An AudioData containing the recorded bytes.
        """
        data = audio.get_raw_data()
        data_queue.put(data)

    recorder.listen_in_background(
        source, record_callback, phrase_time_limit=record_timeout
    )

    print("Ready! Waiting for speech...")
    print("Press Ctrl+C to stop recording")

    while True:
        try:
            now = datetime.utcnow()
            if not data_queue.empty():
                phrase_complete = False
                if phrase_time and now - phrase_time > timedelta(
                        seconds=phrase_timeout
                ):
                    last_sample = bytes()
                    phrase_complete = True
                phrase_time = now

                while not data_queue.empty():
                    data = data_queue.get()
                    last_sample += data

                audio_data = sr.AudioData(
                    last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH
                )
                wav_data = io.BytesIO(audio_data.get_wav_data())

                with open(temp_file, "w+b") as f:
                    f.write(wav_data.read())

                result = model.transcribe(temp_file, fp16=gpu, language=language)
                text = result["text"].strip()

                if phrase_complete:
                    transcription.append(text)
                else:
                    transcription[-1] = text

                os.system("cls" if "win" in platform else "clear")
                for line in transcription:
                    print(line)
                print("", end="", flush=True)

                sleep(0.25)

        except KeyboardInterrupt:
            break
    print()
    print(
        "Result >> " + write_txt(transcription, output if output else os.getcwd())
    )


def main():
    get_ffmpeg_exe()
    args = cli()
    transcribe(**args)


if __name__ == "__main__":
    sys.exit(main())
