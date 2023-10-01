define tracks = ['bass_1', 'guitar_twang', 'guitar_dist', 'space']

init python:
    for channel in tracks:
        renpy.music.register_channel(channel, mixer='music', loop=True, stop_on_mute=False, tight=True, file_prefix='audio/', file_suffix='.flac')

init python:
    def init_music():
        for track in tracks:
            renpy.music.play(track+'_A', channel=track, fadein=5)
        update_sound(0.0, 0.0)

    def update_sound(mood, delay=5.0):
        volume = {
            'bass_1': 1.0,
            'guitar_twang': (1.0-mood)*0.8+0.2,
            'guitar_dist': mood*0.8+0.2,
            'space': (1.0-mood)*0.3+0.5,
            }
        for channel, volume in volume.items():
            renpy.music.set_volume(volume, delay, channel=channel)
