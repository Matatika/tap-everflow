# tap-everflow

`tap-everflow` is a Singer tap for Everflow.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

[![Python version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMatatika%2Ftap-everflow%2Fmain%2Fpyproject.toml&query=project.requires-python&label=python)](https://docs.python.org/3/)
[![License](https://img.shields.io/github/license/Matatika/tap-everflow)](https://github.com/Matatika/tap-everflow/blob/main/LICENSE)
[![Code style](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fastral-sh%2Fruff%2Fmain%2Fassets%2Fbadge%2Fformat.json)](https://docs.astral.sh/ruff/)

## Overview

`tap-everflow` extracts raw data from the [Everflow Network API](https://developers.everflow.io/docs/network/) for the following resources:
- [Offers](https://developers.everflow.io/docs/network/offers/)
- [Clicks](https://developers.everflow.io/docs/network/reporting/raw_clicks/)
- [Conversions](https://developers.everflow.io/docs/network/reporting/raw_conversions/)

## Installation

Install from GitHub:

```bash
# pip
pip install git+https://github.com/Matatika/tap-everflow

# pipx
pipx install git+https://github.com/Matatika/tap-everflow

# poetry
poetry add git+https://github.com/Matatika/tap-everflow

#uv
uv tool install git+https://github.com/Matatika/tap-everflow
uv pip install git+https://github.com/Matatika/tap-everflow
```

## Configuration

### Accepted Config Options

Name | Required | Default | Description
--- | --- | --- | ---
`api_key` | Yes |  | Everflow network API key
`start_date` | No | One year before the current date | The earliest record date to sync

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-everflow --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

You can easily run `tap-everflow` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-everflow --version
tap-everflow --help
tap-everflow --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

Prerequisites:

- Python 3.9+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

### Create and Run Tests

Create tests within the `tests` subfolder and
then run:

```bash
uv run pytest
```

You can also test the `tap-everflow` CLI interface directly using `uv run`:

```bash
uv run tap-everflow --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-everflow
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-everflow --version

# OR run a test ELT pipeline:
meltano run tap-everflow target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
