from importlib.metadata import version

from anndata_mcp_workshop.main import run_app
from anndata_mcp_workshop.mcp import mcp

__version__ = version("anndata_mcp_workshop")

__all__ = [
    "mcp",
    "run_app",
    "__version__"
]


if __name__ == "__main__":
    run_app()
