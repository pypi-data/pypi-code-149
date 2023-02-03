import argparse
import sys
from pathlib import Path

import a13e
from a13e.json_helper import dump_json


def audio_file(args):
    params = args.extra_params or dict()
    if args.random:
        result = (a13e.random_recognize(args.audio_file, name=args.recognize_name, **params))
    else:
        result = a13e.recognize(args.audio_file, name=args.recognize_name, **params)
    if not result:
        print('No recognition result found.')
        sys.exit(1)
    if args.set_tag:
        a13e.set_tag(args.audio_file, result[0])
    if args.output:
        dump_json(args.output, result)
    if args.silent:
        print(result)

    return result


class StoreDict(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        kv = {}
        if not isinstance(values, list):
            values = (values,)
        for value in values:
            n, v = value.split('=')
            kv[n] = v
        setattr(namespace, self.dest, kv)


def main():
    parser = argparse.ArgumentParser(prog='a13e')
    parser.add_argument('audio_fp', type=Path, help='Audio file path.')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {a13e.__version__}')
    parser.add_argument('-s', '--silent', action='store_false', help='silent output.')
    parser.add_argument('-n', '--recognize-name', nargs='*', help='specify the recognizer to use.')
    parser.add_argument('-r', '--random', action='store_true', help='Randomly returns one from recognition results.')
    parser.add_argument('-t', '--set-tag', action='store_true', help='assign the first result as a tag to the audio file.')
    parser.add_argument('-o', '--output', type=Path, help='Output the result to a json file.')
    parser.add_argument('--extra-params', nargs='*', action=StoreDict,
                        help='Pass extra parameters required by some recognizers in the format of key=value')
    parser.set_defaults(func=audio_file)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
