define tracks = ['bass_1', 'guitar_twang', 'guitar_dist', 'space']
define drum_tracks = ['drums']
define drum_variations = {'A': 4, 'B': 1}

init python:
    for channel in tracks + drum_tracks:
        renpy.music.register_channel(channel, mixer='music', loop=True, stop_on_mute=False, tight=True, file_prefix='audio/', file_suffix='.opus')

init python:
    def init_music():
        play_A(5.0)
        queue_drums('A')
        renpy.music.set_volume(2.0, channel='drums')
        update_sound(0.0, 0.0)

    def play_A(fadein=0):
        for track in tracks:
            renpy.music.queue(track+'_A', channel=track, fadein=fadein)

    def play_B(fadein=0):
        for track in tracks:
            renpy.music.queue(track+'_B', channel=track, fadein=fadein)

    def weighted_drum_variation(n):
        if n == 1:
            return 1
        elif n == 4:
            random_choice = random.random()*10
            if random_choice < 7:
                return 1
            return int(random_choice)-5
        else:
            raise ValueError("TODO: support more drum variation options")

    def queue_drums(what):
        nv = drum_variations[what]
        toplay = [f'drums_{what}{weighted_drum_variation(nv)}' for _ in range(6)]
        renpy.music.queue(toplay, channel='drums')

    def update_sound(mood, delay=5.0):
        volume = {
            'bass_1': 1.0,
            'guitar_twang': (1.0-mood)*0.8+0.2,
            'guitar_dist': mood*0.8+0.2,
            'space': (1.0-mood)*0.3+0.5,
            }
        for channel, volume in volume.items():
            renpy.music.set_volume(volume, delay, channel=channel)

    playing_queue = []
    now_playing = None

    def fill_the_queue(position):
        last_pos = position
        last_queued = 'A'
        if playing_queue:
            last_pos = playing_queue[-1][0]
            last_queued = playing_queue[-1][1]
        for i in range(10):
            if last_queued == 'A':
                last_pos += 14 + random.random()*28
                random_choice = random.random()*10
                if random_choice < 5:
                    last_queued = 'B'
                else:
                    last_queued = 'A'
            else:
                last_pos += 2
                last_queued = 'A'
            playing_queue.append((last_pos, last_queued))

    def clean_the_queue(position):
        while playing_queue and playing_queue[0][0] < position:
            playing_queue.pop(0)

    def shuffle_tracks(position):
        if not playing_queue:
            fill_the_queue(position)
        now_playing = playing_queue[0][1]
        if now_playing == 'A':
            play_A()
        else:
            play_B()
        clean_the_queue(position)
