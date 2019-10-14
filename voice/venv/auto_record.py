import pyaudio
import wave
import os
import time


def record_wrapper(fun):
    def _wrapper(saved_path, record_num):
        for i in range(record_num):
            print("Recording {}".format(i))
            saved_file_name = "unlock_{}.wav".format(i)
            fun(saved_path, saved_file_name)
            time.sleep(2)
        print("finished recording")
    return _wrapper


@record_wrapper
def record_voice(saved_path, saved_file_name):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 2
    WAVE_OUTPUT_FILENAME = os.path.join(saved_path, saved_file_name)
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("\nrecording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording\n")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("Save .wav to {}".format(WAVE_OUTPUT_FILENAME))


if __name__ == "__main__":
    """
    看到recording...的时候立马录音，录音时间为1秒左右
    看到finished recording表示录音结束
    """
    saved_path = "/all_files/files/unlock_audio/unlock10_13"   # 在这里添加你自己存最终生成的wav文件的目录
    num = 20    # 这里填写你要录制的数量
    record_voice(saved_path, num)
