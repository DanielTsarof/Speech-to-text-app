import os
import traceback

import whisper
from loguru import logger


class SpeechRecognizer:
    def __init__(self, model: str):
        self.model_name = model
        self.model = whisper.load_model(model)

    def speech2text(
            self,
            file: str,
            save_dir: str = ''
    ) -> None:
        """
        :param file: audiofile in wav format
        :param save_dir: directory where the file with the extracted speech will be saved
        """
        result = self.model.transcribe(file)
        name = file.split(os.sep)[-1]
        save_name = name.split('.')[-2] + '.txt'
        save_path = os.path.join(save_dir, save_name)
        with open(save_path, 'w') as f:
            f.write(result['text'])
        logger.info(f'{file}|{result["text"][:100]}...')

    def speech2text_dir(
            self,
            directory: str,
            save_dir: str = ''
    ) -> None:
        """
        :param directory: audiofile in wav format
        :param save_dir: directory where the file with the extracted speech will be saved
        """
        files = [
            os.path.join(directory, f) for f in
            os.listdir(directory) if
            os.path.isfile(os.path.join(directory, f)) and f.endswith('wav')
        ]
        for file in files:
            print(file)
            try:
                self.speech2text(file, save_dir)
            except Exception:
                logger.error(f'{directory}/{file} | {traceback.format_exc()}')
