import math
from pathlib import Path

import pytest

from surfvol.vol import volume


@pytest.mark.parametrize('file_name, radius', [
    ('unit_sphere.obj', 1.0),
    ('radius3_sphere.obj', 3.0)
])
def test_volume(file_name: str, radius: float, example_input_dir: Path):
    file_name = example_input_dir / file_name
    if not file_name.is_file():
        pytest.fail(f"File not found: {file_name}")

    actual = volume(file_name)
    expected = volume_of_sphere(radius)
    assert actual == pytest.approx(expected, 0.1)


def volume_of_sphere(radius: float) -> float:
    return 4 / 3 * math.pi * (radius ** 3)
