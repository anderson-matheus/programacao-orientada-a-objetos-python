class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Formato inválido')

        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'

    def play(self):
        return 'tocando arquivo mp3'


class WavFile(AudioFile):
    ext = 'wav'

    def play(self):
        return 'tocando arquivo wav'


class OggFile(AudioFile):
    ext = 'ogg'

    def play(self):
        return 'tocando arquivo ogg'


mp3 = MP3File('musica.mp3')
print(mp3.play())

wav = WavFile('musica.wav')
print(wav.play())

ogg = OggFile('musica.ogg')
print(ogg.play())
