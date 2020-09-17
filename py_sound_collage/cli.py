from glob import glob
import random
import os
from pydub import AudioSegment
import click


@click.command()
@click.version_option()
@click.argument(
    "audio_dir", type=click.Path(file_okay=True, dir_okay=True, allow_dash=False)
)
@click.option(
    "--sample_len", type=int, default=1000, help="Length in milliseconds of each sample"
)
@click.option("--output_len", type=int, help="Length in milliseconds of output collage")
def cli(audio_dir, sample_len, output_len):
    """Generate audio collage with random snippets local files

    Concatenates random segments of length sample_len ms from mp3 files
    located in audio_dir. If OUTPUT_LEN is not specified the collage
    output will be SAMPLE_LEN * (the number of input files)

    NOTE: each input file may be sampled from more than once
    or not at all

    AUDIO_DIR is the directory to search for audio files
    """
    os.chdir(audio_dir)
    songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("*.mp3")]
    click.echo(f"Found {len(songs)} songs")

    if not output_len:
        output_len = len(songs) * sample_len

    weights = [len(x) for x in songs]

    collage = AudioSegment.silent(1)  # create output
    while len(collage) < output_len:
        song = random.choices(songs, weights=weights, k=1)[0]

        start = random.randint(0, len(song) - sample_len)
        end = min(start + sample_len, len(song))
        clip = song[start:end]
        collage = collage.append(clip, crossfade=0)

    # write output
    click.echo(f"Collage length: {len(collage) / 1000} sec")
    collage.export("collage.mp3", format="mp3")
