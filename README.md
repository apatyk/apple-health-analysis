# apple-health-analysis
Simple Python analysis script for Apple HealthKit data

This project leverages [`uv`](https://docs.astral.sh/uv/) and the [`apple-health-parser`](https://github.com/alxdrcirilo/apple-health-parser/tree/main?tab=readme-ov-file) Python library for process Apple HealthKit data to determine useful metrics.

To run the analysis:
1. Export data from the Apple Health app.
    1. Tap the user icon in the top right.
    1. Scroll to the bottom.
    1. Select "Export All Health Data"
1. Run `uv run apple-health-analysis.py <path_to_export_zip>`
