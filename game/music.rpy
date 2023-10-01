define tracks = ['bass_1', 'guitar_twang', 'guitar_dist', 'space']

init python:
    for channel in tracks:
        renpy.music.register_channel(channel, mixer='music', loop=True, stop_on_mute=False, tight=True, file_prefix='audio/', file_suffix='.flac')

init python:
    def init_music():
        play_A(1.0)
        update_sound(0.0, 0.0)

    def play_A(fadein=0):
        for track in tracks:
            renpy.music.queue(track+'_A', channel=track, fadein=fadein)

    def play_B(fadein=0):
        for track in tracks:
            renpy.music.queue(track+'_B', channel=track, fadein=fadein)

    def update_sound(mood, delay=5.0):
        volume = {
            'bass_1': 1.0,
            'guitar_twang': (1.0-mood)*0.8+0.2,
            'guitar_dist': mood*0.8+0.2,
            'space': (1.0-mood)*0.3+0.5,
            }
        for channel, volume in volume.items():
            renpy.music.set_volume(volume, delay, channel=channel)

    def shuffle_tracks():
        now_playing = renpy.music.get_playing(channel='space')
        looped = renpy.music.get_loop(channel='space')
        if now_playing == looped[0]:
            if random.random() < 0.7:
                play_A()
            else:
                play_B()
