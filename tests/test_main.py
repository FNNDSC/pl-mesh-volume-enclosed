from unittest.mock import patch, MagicMock
from pathlib import Path

from surfvol.__main__ import parser, main


@patch('surfvol.__main__.calculate_volume')
def test_main(mock_volume_fn: MagicMock, example_input_dir: Path, expected_output_dir: Path, tmp_path: Path):
    # simulate run of main function
    # smell: mock_volume_fn won't capture any calls because we are using multiprocessing
    #        capsys doesn't work either
    mock_volume_fn.return_value = 5.5
    options = parser.parse_args([])
    main(options, example_input_dir, tmp_path)

    assert files_in(tmp_path) == files_in(expected_output_dir)


def files_in(p: Path) -> frozenset:
    return frozenset(f.relative_to(p) for f in p.rglob('*'))
