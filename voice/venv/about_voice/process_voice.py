import time
import numpy as np
import os
import glob
from scipy.io import wavfile
from utils import softmax
import matplotlib.pyplot as plt
from sklearn import svm
from utils import softmax
def voice_process(wav_file, sample_num, process_fn):

    """
    :param wav_file: The audio file address
    :param sample_num: How many frequencies you would like to process
    :return: Bool to indicate whether the voice matches the password
    """
    data = preprocess_data(wav_file, sample_num)
    result = process_fn(data[0])
    return result


def preprocess_data(wav_dir, label, dims=200):
    """
    :param wav_dir:  The folder containing your .wav files
    :param label:   -1 or 1 to indicate different classes
    :return:    data and labels for training
    """
    wav_files = sorted(glob.glob(os.path.join(wav_dir, "*.wav")))
    total_data = []
    total_label = []
    for wav_file in wav_files:
        fs, data = wavfile.read(wav_file)
        data = np.array(data)
        data_fft = np.fft.fft(data)
        frequencies = np.abs(data_fft)
        # top_indexs = np.argsort(frequencies)[-dims:]
        # top_frequencies = frequencies[top_indexs]
        # total_data.append(np.concatenate(top_frequencies, top_indexs, label))
        # frequencies_label = np.concatenate([frequencies[:, 0], [label]])
        frequencies_normal = softmax(frequencies)
        total_data.append(frequencies_normal)
        total_label.append(label)
    total_data = np.array(total_data, dtype=np.float32)
    total_label = np.array(total_label, dtype=np.float32)

    return total_data, total_label

def preprocess_data_v2(wav_dir, label, dims=200):
    """
    :param wav_dir:  The folder containing your .wav files
    :param label:   -1 or 1 to indicate different classes
    :return:    data and labels for training
    """
    wav_files = sorted(glob.glob(os.path.join(wav_dir, "*.wav")))
    total_data = []
    total_label = []
    for wav_file in wav_files:
        fs, data = wavfile.read(wav_file)
        data = np.array(data)
        data_fft = np.fft.fft(data)
        frequencies = np.abs(data_fft)
        # top_indexs = np.argsort(frequencies)[-dims:]
        # top_frequencies = frequencies[top_indexs]
        # total_data.append(np.concatenate(top_frequencies, top_indexs, label))
        # frequencies_label = np.concatenate([frequencies[:, 0], [label]])
        frequencies_normal = softmax(frequencies[:, 0])
        total_data.append(frequencies_normal)
        total_label.append(label)
    total_data = np.array(total_data, dtype=np.float32)
    total_label = np.array(total_label, dtype=np.float32)

    return total_data, total_label


def train_svm(data, sample_num):
    pass



if __name__ == "__main__":
    wav_dir = "/home/yuanliu/桌面/voice_recog/unlock/unlock_wl"
    total_data = preprocess_data(wav_dir, 1)






