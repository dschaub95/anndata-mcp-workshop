from typing import Annotated

import anndata as ad

from anndata_mcp_workshop.mcp import mcp


@mcp.tool()
def get_summary(path: Annotated[str, "Path to the AnnData h5ad file"]) -> str:
    """Summarize the data in the AnnData object."""
    adata = ad.experimental.read_lazy(path)
    return str(adata)
