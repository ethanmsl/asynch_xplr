"""
Test __main__
"""

from src.asynch_xplr.main import main


def test_main() -> None:
    """Test main function"""
    assert main() is None
