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
    help="Length in milliseconds of output collage. NOTE: Songs can repeat with this option")
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
    print(f"output_len = {output_len}")

    collage = AudioSegment.silent(1) 
    # generate output_len ms of audio
    if output_len:
      while len(collage) < output_len:
        song = random.choice(all_songs)
        start = random.randint(0, len(song) - sample_len)
        end = min(start + sample_len, len(song))
        clip = song[start : end]
        collage = collage.append(clip, crossfade=0)
    # sample each song once
    else:
      for song in all_songs:
          start = random.randint(0, len(song) - sample_len)
          end = min(start + sample_len, len(song))
          clip = song[start : end]
          collage = collage.append(clip, crossfade=0)

    # write output
    collage_length = len(collage) / 1000 # ms
    click.echo(f"Collage length: {collage_length} sec")
    collage.export("collage.mp3", format="mp3")

