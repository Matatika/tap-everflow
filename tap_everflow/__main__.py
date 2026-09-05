# Copyright (c) 2026 Meltano.

"""Everflow entry point."""

from __future__ import annotations

from tap_everflow.tap import TapEverflow

TapEverflow.cli()
