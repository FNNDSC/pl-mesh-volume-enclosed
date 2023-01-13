#!/usr/bin/env python

import sys
from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter

from chris_plugin import chris_plugin, PathMapper
from surfvol import __version__, DISPLAY_TITLE
from surfvol.vol import volume as calculate_volume

parser = ArgumentParser(description='Calculate volume enclosed by surfaces',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--pattern', default='**/*.obj', type=str,
                    help='input filter glob for MNI surface files')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')


@chris_plugin(
    parser=parser,
    title='Volume enclosed by polygonal mesh',
    category='Surfaces',  # ref. https://chrisstore.co/plugins
    min_memory_limit='100Mi',  # supported units: Mi, Gi
    min_cpu_limit='1000m',  # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0  # set min_gpu_limit=1 to enable GPU
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    print(DISPLAY_TITLE, file=sys.stderr, flush=True)

    mapper = PathMapper.file_mapper(
        inputdir, outputdir,
        glob=options.pattern,
        suffix='.volume.txt'
    )
    for input_file, output_file in mapper:
        vol = calculate_volume(input_file)
        output_file.write_text(str(vol))
        print(f"{input_file} -> {output_file} ({vol})", flush=True)


if __name__ == '__main__':
    main()
