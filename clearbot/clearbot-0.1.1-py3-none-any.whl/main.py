import argparse
import os

import requests
from PIL import Image, ImageOps
from PIL.Image import Image as ImageType
from tqdm import tqdm

# https://clearbit.com/blog/logo
BASE_URL = "https://logo.clearbit.com"
FORMAT = "png"


def remove_white(image: ImageType, threshold: int) -> ImageType:
    """Remove the white background by setting alpha = 0"""
    gray = ImageOps.grayscale(image)
    nrows, ncols = image.size
    for j in range(ncols):
        for i in range(nrows):
            if gray.getpixel((i, j)) >= threshold:
                image.putpixel((i, j), (255, 255, 255, 0))
    return image


def download_logo(name: str, size: int = 512) -> ImageType:
    """Download image from domain name"""
    response = requests.get(
        f"{BASE_URL}/{name}?size={size}&format={FORMAT}",
        timeout=5,
        stream=True,
    )
    return Image.open(response.raw).convert("RGBA")


def save_file(image: ImageType, dest: str, name: str):
    """Save image to dest/name.png"""
    if not name.endswith(f".{FORMAT}"):
        name += f".{FORMAT}"

    file = os.path.join(dest, name)
    image.save(file, format=FORMAT)


def cli():
    parser = argparse.ArgumentParser(
        prog="clearbot",
        description="Clearbit Logo API client",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
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
        default=256,
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=str,
        default="/tmp",
        help="destination directory",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display progress bar",
    )
    parser.add_argument(
        "domains",
        metavar="DOMAIN.COM",
        type=str,
        nargs="+",
        help="List of domains to scrap",
    )
    args = parser.parse_args()

    for domain in tqdm(args.domains, disable=not args.verbose):
        img = download_logo(name=domain, size=args.size)
        img.load()
        img = remove_white(img, threshold=args.threshold)
        save_file(img, dest=args.destination, name=domain)
