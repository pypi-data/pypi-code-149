import contextlib
import json
import os
import subprocess
import sys
from functools import wraps
from pathlib import Path
from typing import Optional, TypeVar, Any, Generator, IO, Callable
if sys.version_info < (3, 10):
    from typing_extensions import ParamSpec
else:
    from typing import ParamSpec

from a13e.exception import ProcessError

Param = ParamSpec("Param")
RetType = TypeVar("RetType")
OriginalFunc = Callable[Param, RetType]


def process_error_decorator(
        exception: Optional[Exception] = None
) -> Callable[[OriginalFunc], OriginalFunc]:
    def decorator(func: OriginalFunc) -> OriginalFunc:
        @wraps(func)
        def wrapper(*args: Param.args, **kwargs: Param.kwargs) -> RetType:
            try:
                return func(*args, **kwargs)
            except subprocess.CalledProcessError as e:
                print(e.returncode, e.output.decode())
                if exception:
                    raise exception

        return wrapper

    return decorator


@process_error_decorator(ProcessError())
def get_audio_data(audio_fp: Path) -> Any:
    """Get audio data via ffprobe.
    Args:
        audio_fp: Audio file path

    Return:
        Audio data Python object (use json.loads)
    Raises:
        ProcessError: Will raise if FFmpeg return code is non-zero.

    """
    output = subprocess.check_output(
        [
            'ffprobe',
            '-v',
            'error',
            '-hide_banner',
            '-print_format',
            'json',
            '-show_format',
            '-show_streams',
            str(audio_fp),
        ],
        stderr=subprocess.STDOUT
    )
    return json.loads(output)


@process_error_decorator(ProcessError())
def resample(audio_fp: Path, *, sample_rate: str) -> Path:
    """Resample the audio to single-channel audio at the specified sample rate.

    Use FFmpeg to generate a copy of the audio at the specified sample rate,
    Returns the original file path if the audio's sample rate is the same as
    specified.

    Args:
        audio_fp: Audio file path.
        sample_rate: Sampling Rate.

    Return:
        Path to audio file copy (if sample rate is different)

    Raises:
        ProcessError: Will raise if FFmpeg return code is non-zero.
    """
    data = get_audio_data(audio_fp)
    if data['streams'][0]['sample_rate'] == sample_rate:
        return audio_fp

    temp_file_path = audio_fp.parent / f'{audio_fp.stem}-{sample_rate}MHz{audio_fp.suffix}'
    subprocess.check_call(
        [
            'ffmpeg',
            '-i',
            str(audio_fp),
            '-ac',
            '2',
            '-ar',
            sample_rate,
            '-y',
            str(temp_file_path)
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    return temp_file_path


@contextlib.contextmanager
def remove_file_context(fp: Path):
    """Delete the file when the context exits."""
    try:
        yield
    finally:
        fp.unlink(missing_ok=True)


@contextlib.contextmanager
def temp_file_context(temp_fp: Path, *args, **kwargs) -> Generator[IO, Any, None]:
    """Files are opened or created on entry to the context and deleted on exit.

    Args:
        temp_fp: File path.
        args: The variable length parameter of Path.open.
        **kwargs: Keyword arguments to Path.open.

    Returns:
        File object.
    """
    with remove_file_context(temp_fp), temp_fp.open(*args, **kwargs) as f:
        yield f


@contextlib.contextmanager
def chdir_context(workdir: Path) -> Generator[Any, Any, None]:
    """Switch the working directory when entering the context,
    and switch back to the original path when exiting"""
    cwd = Path.cwd()
    os.chdir(workdir)
    yield
    os.chdir(cwd)
