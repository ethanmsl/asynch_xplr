"""
Test __main__
"""

import asyncio

from src.asynch_xplr.main import main


def test_main() -> None:
    """Test main function"""
    assert asyncio.run(main(1)) is None
