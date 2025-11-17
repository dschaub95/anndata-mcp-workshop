from typing import Annotated

import anndata as ad
import scanpy as sc

from anndata_mcp_workshop.mcp import mcp


@mcp.tool()
def get_marker_genes(
    path: Annotated[str, "Path to the AnnData h5ad file"],
    cell_type: Annotated[str, "Cell type to get markers for"],
    topn: Annotated[int, "Number of top markers to return"] = 5,
    pval_cutoff: Annotated[float, "P-value cutoff for significance"] = 0.05,
) -> str:
    """Get the markers for the data in the AnnData object."""
    adata = ad.read_h5ad(path)
    marker_df = sc.get.rank_genes_groups_df(adata, group=cell_type, pval_cutoff=pval_cutoff)
    marker_df = marker_df.sort_values(by="scores", ascending=False)
    return marker_df.head(topn).to_csv()
