from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_speech(file_path, speed=1.0):
    # テキストファイルを読み込む
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # gTTSを使用してテキストを音声に変換
    tts = gTTS(text, lang='ja')
    tts.save("output.mp3")

    # 音声速度を変更
    sound = AudioSegment.from_file("output.mp3")
    sound_with_changed_speed = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
    }).set_frame_rate(sound.frame_rate)

    # 変更された速度の音声を保存
    sound_with_changed_speed.export("output_with_speed.mp3", format="mp3")

# 使用例
text_to_speech("example.txt", speed=1.5)  # 1.5倍速
