# py-sound-collage

`py-sound-collage` is a tool to concatenate random audio snippets from your local audio files into a sound collage (think radio dial effect). 


## Usage

```
> poetry run py-sound-collage --help
Usage: py-sound-collage [OPTIONS] AUDIO_DIR

  Generate audio collage with random snippets local files

  Concatenates random segments of length sample_len ms from mp3 files
  located in audio_dir. If OUTPUT_LEN is not specified the collage output
  will be SAMPLE_LEN * (the number of input files)

  NOTE: each input file may be sampled from more than once or not at all

  AUDIO_DIR is the directory to search for audio files

Options:
  --version             Show the version and exit.
  --sample_len INTEGER  Length in milliseconds of each sample
  --output_len INTEGER  Length in milliseconds of output collage
  --help                Show this message and exit.
```

__Example__: This will concatenate 500msec samples from the nature directory into a collage of 20sec `collage.mp3`. 

```
> ls nature
ls nature
1017amsterdam.mp3         hummingbirds.mp3          palermo-traffic.MP3
church-bells-salzburg.mp3 lagos.mp3                 pulse-emitter.mp3
gronant-beach.mp3         morning-birds.mp3         wastepaper.mp3
> poetry run py-sound-collage --sample_len 500 nature/  --output_len 20000
Found 8 songs
Collage length: 20.0 sec
```
Here is the [sample output](https://gist.github.com/connnnor/36eb27a6ae15911b030f4c42d6cf9883/raw/01f47bbfb30f8b1dcb7173ee24c5788c73ea60fd/collage.mp3) from the command used above. Credits for the original audio files used to generate the collage given below.

## Songs / Audio Credits

* [Pulse Emitter - Oppressive Nature](https://archive.org/details/Oppressive_Nature-4243)
* [1017 Amsterdam, Nederlands - Street ambiance](https://archive.org/details/aporee_43428_49466)
* [Unnamed Road, Prestatyn LL19 7HU, UK - Gronant Beach Walking Meditation](https://archive.org/details/aporee_37542_42986)
* [church bells, Salzburg, Austria - church bells](https://archive.org/details/aporee_15426_17968)
* [traffic](https://archive.org/details/aporee_6832_8504)
* [wastepaper-feeding-room](https://archive.org/details/aporee_27365_31525)
* [morning-birds](https://archive.org/details/aporee_7083_8788)
* [lagos](https://archive.org/details/aporee_5762_7243)
* [hummingbirds](https://archive.org/details/aporee_32356_37202)
