from typing import Annotated, Literal

import anndata as ad

from anndata_mcp_workshop.mcp import mcp


@mcp.tool()
def get_value_counts(
    path: Annotated[str, "Path to the AnnData h5ad file"],
    column: Annotated[str, "Column name to get value counts for"],
    attribute: Annotated[Literal["obs", "var"], "Attribute to get value counts from (obs or var)"],
) -> str:
    """Get value counts for a column in obs or var attributes of the AnnData object."""
    adata = ad.read_h5ad(path)

    if attribute == "obs":
        value_counts = adata.obs[column].value_counts()
    else:  # attribute == "var"
        value_counts = adata.var[column].value_counts()

    # Convert to DataFrame with proper column names for CSV output
    result_df = value_counts.reset_index()
    result_df.columns = [column, "count"]

    return result_df.to_csv(index=False)
