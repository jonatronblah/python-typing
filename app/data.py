import librosa as lb
import os

def get_melspec(input_path: str | os.PathLike = lb.ex('trumpet')):
    y, sr = lb.load(input_path)