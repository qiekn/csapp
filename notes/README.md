# Zensical Template

A documentation template powered by [Zensical](https://zensical.org/).

## Quick Start

```bash
git clone -b zensical git@github.com:qiekn/docs.git my-docs
cd my-docs
pip install zensical
zensical serve
```

Or with uv:

```bash
git clone -b zensical git@github.com:qiekn/docs.git my-docs
cd my-docs
uv run --with zensical zensical serve
```

## Structure

```
.
├── docs/
│   ├── images/
│   ├── stylesheets/
│   └── index.md
├── overrides/
│   └── partials/
├── zensical.toml
├── .gitignore
└── README.md
```

## Configuration

Edit `zensical.toml` to customize your site:

- `site_name` — your site title
- `site_url` — your deployment URL
- `repo_url` — link to your repository

See [Zensical documentation](https://zensical.org/) for full configuration reference.
