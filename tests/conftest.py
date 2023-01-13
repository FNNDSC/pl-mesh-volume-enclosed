from pathlib import Path

import pytest

EXAMPLES_DIR_LIVE = Path(__file__).parent.parent / 'examples'


@pytest.fixture
def example_input_dir() -> Path:
    return _require_dir(EXAMPLES_DIR_LIVE / 'incoming')


@pytest.fixture
def expected_output_dir() -> Path:
    return _require_dir(EXAMPLES_DIR_LIVE / 'outgoing')


def _require_dir(p: Path) -> Path:
    if not p.is_dir():
        raise pytest.fail(f'{p} is not a directory.')
    return p
