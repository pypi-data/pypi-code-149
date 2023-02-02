"""
Fast random file generation.

Usage:
    create-files --size=<size> --count=<count> --root=<root>

Uses the fast and high-quality PCG64DXSM random number generator, one instance per cpu
core; each process writes a set of subfiles to a directory asynchronously. A file
manifest including the random state that generated each file is written to the root
directory. File generation is entirely deterministic.

On my M1 MacBook Pro creating 100k 40KB files (4.1GB) takes 7.8 seconds, or 530MB/s.
This is almost exactly the same speed as I get from `dd if=/dev/urandom of=target-file
bs=1M count=1000`, and is about 1/3 the speed of `dd if=/dev/zero of=target-file bs=1M
count=1000`. MacBooks have pretty fast SSDs, so we can assume that on most machines this
will run at least close to the maximum disk speed.
"""

import asyncio
from functools import partial
from pathlib import Path
from random import randbytes, randint
from typing import Optional


def random_hex_name(len: int = 8) -> str:
    return randbytes((len + 1) // 2).hex()


async def write_file(path: Path, min_size: int, max_size: int, random: bool) -> int:
    size = min_size if min_size == max_size else randint(min_size, max_size)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        if random:
            while size > 0:
                chunk = min(size, 2**16)
                size -= chunk
                f.write(randbytes(chunk))
        else:
            f.truncate(size)
    return size


async def fill_directory(
    root: Path, count: int, min_size: int, max_size: int, random: bool
) -> None:
    writer = partial(write_file, min_size=min_size, max_size=max_size, random=random)
    tasks = []
    for i in range(count):
        path = root / f"{i:07}.bin"
        tasks.append(asyncio.create_task(writer(path=path)))
    await asyncio.gather(*tasks)


async def split_directory(
    root: Path,
    count: int,
    min_size: int,
    max_size: int,
    random: bool,
    max_children: Optional[int],
):
    filler = partial(
        fill_directory, min_size=min_size, max_size=max_size, random=random
    )
    splitter = partial(
        split_directory,
        min_size=min_size,
        max_size=max_size,
        random=random,
        max_children=max_children,
    )
    if max_children is None or count <= max_children:
        return await filler(root=root, count=count)

    if count > (max_children**2):
        fn = splitter
        num_dirs = max_children - 1 if count % max_children else max_children
        per_dir = count // num_dirs
        remainder = count - num_dirs * per_dir
    else:
        fn = filler
        per_dir = max_children
        num_dirs = count // max_children
        remainder = count % max_children

    tasks = []
    for i in range(num_dirs):
        path = root / f"{i:04}"
        tasks.append(asyncio.create_task(fn(root=path, count=per_dir)))
    if remainder:
        path = root / f"{i + 1:04}"
        tasks.append(asyncio.create_task(fn(root=path, count=remainder)))
    await asyncio.gather(*tasks)


def create_files(
    root: Path,
    count: int,
    min_size: int,
    max_size: int,
    random: bool,
    max_children: Optional[int],
):
    task = None
    if count == 1:
        task = write_file(root.with_suffix(".bin"), min_size, max_size, random)
    elif max_children is None or count <= max_children:
        task = fill_directory(root, count, min_size, max_size, random)
    else:
        task = split_directory(root, count, min_size, max_size, random, max_children)

    asyncio.run(task)
