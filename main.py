import os

import argparse

from src.config import config
from src.logger import setup_logger
from src.sound_transform import snd_transform, snd_transform_dir
from src.speech2text import SpeechRecognizer

if __name__ == '__main__':
    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-m',
        '--mode',
        required=True,
        type=str,
        help='Application operation mode',
        choices=['speech2text', 'transform', 'setup'],
    )

    parser.add_argument(
        '-p',
        '--path',
        default='.',
        type=str,
        help='Path to sound file or directory with sound files'
    )

    parser.add_argument(
        '-out',
        '--out_dir',
        default='.',
        type=str,
        help='The directory where the processed files will be uploaded'
    )

    parser.add_argument(
        '-s',
        '--speed',
        type=float,
        default=1,
        help="Sound speed multiplier (only if mode is 'transform')"
    )

    parser.add_argument(
        '-mag',
        '--magnitude',
        type=float,
        help="Sound magnitude multiplier (only if mode is 'transform')"
    )

    args = parser.parse_args()

    if args.mode == 'transform':
        if args.speed == 1 and args.magnitude == 1:
            raise ValueError("Set 'speed' or/and 'magnitude' parameter")
        if os.path.isfile(args.path):
            snd_transform(
                args.path,
                args.speed,
                args.magnitude,
                args.out_dir
            )
        elif os.path.isdir(args.path):
            snd_transform_dir(
                args.path,
                args.speed,
                args.magnitude,
                args.out_dir
            )
        else:
            raise ValueError(f'Invalid path: {args.path}')

    elif args.mode == 'speech2text':
        recognizer = SpeechRecognizer(config.speech2text.model)
        if os.path.isfile(args.path):
            recognizer.speech2text(args.path,
                                   args.out_dir)
        elif os.path.isdir(args.path):
            recognizer.speech2text_dir(args.path,
                                       args.out_dir)
        else:
            raise ValueError(f'Invalid path: {args.path}')
    elif args.mode == 'setup':
        SpeechRecognizer(config.speech2text.model)
        print(f'Model "{config.speech2text.model}" has been downloaded')
    else:
        raise ValueError(f'Invalid argument: {args.mode}')
