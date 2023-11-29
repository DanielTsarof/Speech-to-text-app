# Speech to text app

---

This application utilizes the **OpenAI Whisper** library for speech recognition: https://github.com/openai/whisper.
Whisper is one of the best open-source libraries capable of functioning in offline mode.
The library also allows automatic language identification
and supports multilingual speech recognition. For proper functioning, the library requires the installation
of the command-line tool ffmpeg on your system.

The **Librosa** library was used to manipulate the speed and volume of the audio: https://librosa.org/doc/latest/index.html


## Installation
Install ffmpeg if not already installed:

on Ubuntu/Debian

    sudo apt update && sudo apt install ffmpeg

on Windows using Chocolatey (https://chocolatey.org/):

    choco install ffmpeg


on Windows using Scoop (https://scoop.sh/):

    scoop install ffmpeg

To run the application, you'll need Python version 3.10 or higher.

Create the virtual environment:

    # create venv
    python -m venv venv
    
    #activate venv
    source venv/bin/activate

Install the dependencies by running the following command in the repository's root:

```bash
pip install requirements.txt
```

Download the speech recognition model:

```bash
python main.py -m setup
```

## Usage
To use the application, run the main.py file. Here is a list of accepted arguments:

#### Specify the operation mode

    -m  --mode

Allowed values:

* _speech2text_ - Speech recognition mode


* _transform_ - Amplitude and speed transformation mode


* _setup_ - Initial setup mode. Downloads the model.


#### Audio speed multiplier

    -s --speed

A positive real number. If less than one, it slows down; if greater, it speeds up.

#### Audio volume (amplitude) multiplier

    -mag --magnitude

A positive real number. If less than one, it decreases; if greater, it increases.

* _speed_ and _magnitude_ are passed only if the _transform_ mode is selected.

Path to the audio file in wav format or a directory with such audio files

    -p --path

Path to the directory where processed audio files or extracted speech in txt format will be saved

    -out --out_dir

## Examples

### Speed and Amplitude Transformation
Speed up the audio file by a factor of 2 and increase the volume threefold:
    
    python main.py -m transform -p path/to/audio.wav -out oputput/dir/path -s 2 -mag 3

The output will be: _oputput/dir/path/audio_processed.wav_

Similarly, you can process all audio files in a directory:

    python main.py -m transform -p path/to/audio_dir -out oputput/dir/path -s 2 -mag 3

### Speech Recognition

Recognize speech from an audio file and save the result in txt format:

    python main.py -m speech2text -p path/to/audio.wav -out oputput/dir/path

The output will be: _oputput/dir/path/audio.txt_

You can process all files in a directory in the same way:

    python main.py -m speech2text -p path/to/audio_dir -out oputput/dir/path
