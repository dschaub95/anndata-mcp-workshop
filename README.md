# anndata-mcp-workshop

[![BioContextAI - Registry](https://img.shields.io/badge/Registry-package?style=flat&label=BioContextAI&labelColor=%23fff&color=%233555a1&link=https%3A%2F%2Fbiocontext.ai%2Fregistry)](https://biocontext.ai/registry)
[![Tests][badge-tests]][tests]
[![Documentation][badge-docs]][documentation]

[badge-tests]: https://img.shields.io/github/actions/workflow/status/dschaub95/anndata-mcp-workshop/test.yaml?branch=main
[badge-docs]: https://img.shields.io/readthedocs/anndata-mcp-workshop

A very interesting piece of code

## Getting started

Please refer to the [documentation][],
in particular, the [API documentation][].

You can also find the project on [BioContextAI](https://biocontext.ai), the community-hub for biomedical MCP servers: [anndata-mcp-workshop on BioContextAI](https://biocontext.ai/registry/dschaub95/anndata-mcp-workshop).

## Installation

You need to have Python 3.10 or newer installed on your system.
If you don't have Python installed, we recommend installing [uv][].

There are several alternative options to install anndata-mcp-workshop:

### 1. Use `uvx` to run it immediately
After publication to PyPI:
```bash
uvx anndata_mcp_workshop
```

Or from a Git repository:

```bash
uvx git+https://github.com/dschaub95/anndata-mcp-workshop.git@main
```

### 2. Include it in one of various clients that supports the `mcp.json` standard

If your MCP server is published to PyPI, use the following configuration:

```json
{
  "mcpServers": {
    "anndata-mcp-workshop": {
      "command": "uvx",
      "args": ["anndata_mcp_workshop"]
    }
  }
}
```
In case the MCP server is not yet published to PyPI, use this configuration:

```json
{
  "mcpServers": {
    "anndata-mcp-workshop": {
      "command": "uvx",
      "args": ["git+https://github.com/dschaub95/anndata-mcp-workshop.git@main"]
    }
  }
}
```

For purely local development (e.g., in Cursor or VS Code), use the following configuration:

```json
{
  "mcpServers": {
    "anndata-mcp-workshop": {
      "command": "uvx",
      "args": [
        "--refresh",
        "--from",
        "path/to/repository",
        "anndata_mcp_workshop"
      ]
    }
  }
}
```

If you want to reuse and existing environment for local development, use the following configuration:

```json
{
  "mcpServers": {
    "anndata-mcp-workshop": {
      "command": "uv",
      "args": ["run", "--directory", "path/to/repository", "anndata_mcp_workshop"]
    }
  }
}
```

### 3. Install it through `pip`:

```bash
pip install --user anndata_mcp_workshop
```

### 4. Install the latest development version:

```bash
pip install git+https://github.com/dschaub95/anndata-mcp-workshop.git@main
```

## Contact

If you found a bug, please use the [issue tracker][].

## Citation

> t.b.a

[uv]: https://github.com/astral-sh/uv
[issue tracker]: https://github.com/dschaub95/anndata-mcp-workshop/issues
[tests]: https://github.com/dschaub95/anndata-mcp-workshop/actions/workflows/test.yaml
[documentation]: https://anndata-mcp-workshop.readthedocs.io
[changelog]: https://anndata-mcp-workshop.readthedocs.io/en/latest/changelog.html
[api documentation]: https://anndata-mcp-workshop.readthedocs.io/en/latest/api.html
[pypi]: https://pypi.org/project/anndata-mcp-workshop
