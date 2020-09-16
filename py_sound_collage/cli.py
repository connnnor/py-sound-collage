from glob import glob
from pydub import AudioSegment
import click
import random
import os


@click.command()
@click.version_option()
@click.argument(
    "audio_dir",
    type=click.Path(file_okay=True, dir_okay=True, allow_dash=False))
@click.option(
    "--sample_len",
    type=int,
    default=1000,
    help="Length in milliseconds of each sample")
@click.option(
    "--output_len",
    type=int,
    help="Length in milliseconds of output collage")
@click.option(
    '--repeat', 
    is_flag=True,
    default=False,
    help="Repeat input songs")
def cli(audio_dir, sample_len, repeat, output_len):
    """Generate audio collage with random snippets local files

    AUDIO_DIR is the directory to search for audio files
    """
    os.chdir(audio_dir)
    print(f"reading in songs")
    all_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("*.mp3")]
    #print(f"flattening audio segments")
    #big_fat_sample = [item for sublist in all_songs for item in sublist]
    print(f"Original list of songs: {all_songs}")
    random.shuffle(all_songs)
    print(f"list after shuffle: {all_songs}")

    collage = AudioSegment.silent(1) 
    for song in all_songs:
        start = random.randint(0, len(song) - sample_len)
        clip = song[start: start + sample_len]
        collage = collage.append(clip, crossfade=0)

    collage_length = len(collage) / 1000 # ms
    print(f"Length of all mp3s: {collage_length} sec")
    collage.export("collage.mp3", format="mp3")

