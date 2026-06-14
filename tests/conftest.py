from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from unittest.mock import MagicMock

    from pytest_mock import MockerFixture


@pytest.fixture
def fake_embedder(mocker: MockerFixture) -> MagicMock:
    embedder = mocker.MagicMock()
    embedder.model = "fake-model"
    embedder.embed.return_value = [1.0, 0.0, 0.0]
    embedder.embed_batch.side_effect = lambda texts: [[1.0, 0.0, 0.0]] * len(texts)
    return embedder
