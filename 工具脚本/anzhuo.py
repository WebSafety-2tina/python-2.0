import scipy.io.wavfile as wavfile
samplerate, data = wavfile.read('telegram2wechat.wav')
left = []
right = []
for item in data:
    left.append(item[0])
    right.append(item[1])
diff = [left - right for left, right in zip(left, right)]
print(diff)