from glob import glob
from pydub import AudioSegment
import click
import random
import os


@click.command()
@click.version_option()
@click.argument(
    "audio_dir", type=click.Path(file_okay=True, dir_okay=True, allow_dash=False)
)
@click.option(
    "--sample_len", type=int, default=1000, help="Length in milliseconds of each sample"
)
@click.option(
    "--output_len", type=int, help="Length in milliseconds of output collage."
)
def cli(audio_dir, sample_len, output_len):
    """Generate audio collage with random snippets local files

    Concatenates random segments of length sample_len ms from mp3 files
    located in audio_dir.
    NOTE: If OUTPUT_LEN is not specified each input file will only
    be sampled once. When OUTPUT_LEN is specified each input file
    may be sampled from more than once or not at all

    AUDIO_DIR is the directory to search for audio files
    """
    os.chdir(audio_dir)
    all_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("*.mp3")]
    random.shuffle(all_songs)
    click.echo(f"Found {len(all_songs)} songs")
    total_len = sum(len(s) for s in all_songs)

    weights = list(map(lambda x: len(x), all_songs))  # weight by length
    collage = AudioSegment.silent(1)  # create output
    while True:
        # sample any song
        if output_len:
            song = random.choices(all_songs, weights=weights, k=1)[0]
            if len(collage) > output_len:
                break
        # sample each song once
        else:
            if not all_songs:
                break
            song = all_songs.pop()

        start = random.randint(0, len(song) - sample_len)
        end = min(start + sample_len, len(song))
        clip = song[start:end]
        collage = collage.append(clip, crossfade=0)

    # write output
    collage_length = len(collage) / 1000  # ms
    click.echo(f"Collage length: {collage_length} sec")
    collage.export("collage.mp3", format="mp3")
