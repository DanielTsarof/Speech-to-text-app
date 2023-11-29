import os
import traceback

import librosa
import soundfile as sf
from loguru import logger


def snd_transform(
        file: str,
        speed: float = 1,
        magnitude=1,
        save_dir: str = ''
) -> None:
    """
    Function for changing speed and magnitude of audio

    :param file: path to wav file to be transformed
    :param speed: speed multiplier, positive real number
    :param magnitude: magnitude multiplier, positive real number
    :param save_dir: directory where processed file will be saved
    """
    y, sr = librosa.load(file)
    name = file.split(os.sep)[-1]
    save_name = name.split('.')[-2] + '_processed' + '.' + name.split('.')[-1]
    save_path = os.path.join(save_dir, save_name)
    sf.write(save_path, y * magnitude, samplerate=int(sr * speed), subtype='PCM_24')
    logger.info(f'{file} -> {save_path} | success')


def snd_transform_dir(
        directory: str,
        speed: float = 1,
        magnitude=1,
        save_dir: str = ''
) -> None:
    """
    Function for changing speed and magnitude of multiple audios

    :param directory: path to directory with wav files to be transformed
    :param speed: speed multiplier, positive real number
    :param magnitude: magnitude multiplier, positive real number
    :param save_dir: directory where processed files will be saved
    """
    files = [
        os.path.join(directory, f) for f in
        os.listdir(directory) if
        os.path.isfile(os.path.join(directory, f)) and f.endswith('wav')
    ]
    for file in files:
        try:
            snd_transform(file, speed, magnitude, save_dir)
        except Exception:
            logger.error(f'{file} -> {directory}/{file} | {traceback.format_exc()}')
