import tensorflow as tf

import numpy as np

import matplotlib.pyplot as plt


import pyaudio
import wave
import soundfile as sf

import sys

sys.path.append('C:/Users/Rhywu/innovation/tensorflowtts/tts-demo-master/TensorFlowTTS')

from tensorflow_tts.inference import AutoConfig
from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor


tacotron2_config = AutoConfig.from_pretrained('TensorFlowTTS/examples/tacotron2/conf/tacotron2.baker.v1.yaml')

tacotron2 = TFAutoModel.from_pretrained(
    config=tacotron2_config,
    pretrained_path="tacotron2.h5",
    name="tacotron2"
)

mb_melgan_config = AutoConfig.from_pretrained(
    'TensorFlowTTS/examples/multiband_melgan/conf/multiband_melgan.baker.v1.yaml')
mb_melgan = TFAutoModel.from_pretrained(
    config=mb_melgan_config,
    pretrained_path="mb.melgan.h5",
    name="mb_melgan"
)

processor = AutoProcessor.from_pretrained(pretrained_path="./baker_mapper.json")

# 合成
def do_synthesis(input_text, text2mel_model, vocoder_model):
    input_ids = processor.text_to_sequence(input_text, inference=True)

    _, mel_outputs, stop_token_prediction, alignment_history = text2mel_model.inference(
        tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        tf.convert_to_tensor([len(input_ids)], tf.int32),
        tf.convert_to_tensor([0], dtype=tf.int32)
    )

    remove_end = 1024
    audio = vocoder_model.inference(mel_outputs)[0, :-remove_end, 0]
    #print("ENDSyn")
    return mel_outputs.numpy(), alignment_history.numpy(), audio.numpy()


#写入
def play(f):
    chunk = 1024
    wf = wave.open(f, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)
    data = wf.readframes(chunk)
    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()
    #print("ENDPlay")


#播放
def say(word):
    mels, alignment_history, audios = do_synthesis(word, tacotron2, mb_melgan)
    sf.write('demo.wav', audios, 24000)
    play('demo.wav')

    