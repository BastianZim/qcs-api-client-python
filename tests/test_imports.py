"""
Test that all modules in the package can be successfully imported from.
"""

from importlib import import_module
from pathlib import Path


def test_import_all():
    base_path = Path(__file__).parent.parent / "qcs_api_client"
    paths = base_path.rglob("*.py")
    for path in paths:
        import_path = ".".join(path.relative_to(base_path.parent).with_suffix("").parts)
        import_module(import_path)
