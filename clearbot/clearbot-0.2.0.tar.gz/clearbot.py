"""Clearbit Logo API client
"""

from __future__ import annotations

import argparse
import os
import sys
from io import TextIOWrapper
from typing import List, Optional

import loguru
import requests
from loguru import logger
from PIL import Image, ImageOps
from PIL.Image import Image as ImageType

# https://clearbit.com/blog/logo
BASE_URL = "https://logo.clearbit.com"
FORMAT = "png"

OK = "\033[32mOK\033[0m"
FAIL = "\033[31mFAIL\033[0m"


def remove_white(image: ImageType, threshold: int) -> ImageType:
    """Remove the white background by setting alpha = 0"""
    gray = ImageOps.grayscale(image)
    nrows, ncols = image.size
    for j in range(ncols):
        for i in range(nrows):
            if gray.getpixel((i, j)) >= threshold:
                image.putpixel((i, j), (255, 255, 255, 0))
    return image


def download_logo(name: str, size: int = 512) -> Optional[ImageType]:
    """Download image from domain name"""
    response = requests.get(
        f"{BASE_URL}/{name}?size={size}&format={FORMAT}",
        timeout=5,
        stream=True,
    )
    if response.status_code == 200:
        return Image.open(response.raw).convert("RGBA")
    return None


def save_file(image: ImageType, dest: str, name: str):
    """Save image to dest/name.png"""
    if not name.endswith(f".{FORMAT}"):
        name += f".{FORMAT}"

    file = os.path.join(dest, name)
    image.save(file, format=FORMAT)


def parse_file(file: TextIOWrapper) -> List[str]:
    """Return the domains found in the file (one domain by line)"""
    return [line.rstrip("\n") for line in file if len(line) > 1]


# ========================================================================== #
# Logging
# ========================================================================== #


def formatter(record: loguru.Record) -> str:
    """Formatter that allows to change EOL character"""
    end = record["extra"].get("end", "\n")
    return "{message}" + end


def init_logger(verbose: bool):
    """Set the level of the logger depending of the verbose flag"""
    # remove default handler
    logger.remove(0)
    # add custom one
    logger.add(
        sys.stdout,
        format=formatter,
        level="DEBUG" if verbose else "ERROR",
    )


def log(domain: str, end: str = ""):
    """Log a domain with optional EOL char"""
    logger.bind(end=end).debug(f"{domain:20s}")


def fail():
    """Print FAIL in red"""
    logger.debug(FAIL)


def done():
    """Print OK in green"""
    logger.debug(OK)


def error(msg: str):
    """Print error message in red"""
    logger.error(f"\033[31m{msg}\033[0m")


# ========================================================================== #
# Entrypoint
# ========================================================================== #


def cli():
    """Script entrypoint"""
    parser = argparse.ArgumentParser(
        prog="clearbot",
        description="Clearbit Logo API client",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display progress bar",
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=str,
        default="/tmp",
        help="destination directory",
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        default=512,
        help="Image size (length of longest side in pixels)",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        help="remove pixels (alpha=0) with gray values higher than the threshold",
        required=False,
    )

    input_parser = parser.add_argument_group("input")
    input_parser.add_argument(
        "-f",
        "--file",
        type=argparse.FileType("r", encoding="utf-8"),
        help="use file as input",
        required=False,
    )
    input_parser.add_argument(
        "domains",
        metavar="DOMAIN.COM",
        type=str,
        nargs="*",
        help="List of domains to scrap",
    )
    args = parser.parse_args()

    init_logger(args.verbose)

    # check the input domains
    domains: List[str] = args.domains
    if args.file:
        domains += parse_file(args.file)

    if len(domains) == 0:
        error("no input provided (use positional arguments of the -f option)")
        parser.print_usage()
        return

    # work
    for domain in domains:
        log(domain)
        img = download_logo(name=domain, size=args.size)
        if img is None:
            fail()
            continue
        img.load()
        if args.threshold:
            img = remove_white(img, threshold=args.threshold)
        save_file(img, dest=args.destination, name=domain)
        done()
