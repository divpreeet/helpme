from neutts import NeuTTS
import soundfile as sf

tts = NeuTTS(
    backbone_repo="neuphonic/neutts-nano",
    backbone_device="cpu",
    codec_repo="neuphonic/neucodec",
    codec_device="cpu",
)

ref_text = open("voice.txt", "r").read().strip()
ref_codes = tts.encode_reference("voice.wav")
wav = tts.infer("Miss, the answer to the question is two forty five", ref_codes, ref_text)
sf.write("output.wav", wav, 24000)