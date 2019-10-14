import pyaudio
import wave  #使用wave模式

def recording(record_seconds):
    CHUNK = 1024  # 缓存区设置 1024个字节
    FORMAT = pyaudio.paInt16  # 取样值的量化格式
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* 录音中...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* 录音完成")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

chunk=1024

# open a wav format music
f = wave.open(r"C:\Users\stacy\PycharmProjects\venv\reminder.wav", "rb")
# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True)
# read data
data = f.readframes(chunk)

# paly stream
while data != b'':
    stream.write(data)
    data = f.readframes(chunk)

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()

recording(4)

