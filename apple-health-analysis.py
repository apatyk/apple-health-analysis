# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "apple_health_parser",
#     "loguru",
# ]
# ///

import argparse
from argparse import Namespace
from loguru import logger

from apple_health_parser.utils.parser import Parser
from apple_health_parser.plot import Plot


def parse_args() -> Namespace:
    """Parse and return collected command-line arguments."""

    parser = argparse.ArgumentParser(description="Process Apple HealthKit data")
    parser.add_argument(
        "path", help="Path to the export.zip archive from the Apple Health app"
    )
    args = parser.parse_args()

    return args


def process_data(path: str) -> None:
    """Process and visualize Apple Health data from archive at path."""

    parser = Parser(export_file=path, overwrite=False)

    selected_flags = [
        "HKQuantityTypeIdentifierAppleExerciseTime",
        "HKQuantityTypeIdentifierDistanceWalkingRunning",
        "HKQuantityTypeIdentifierStepCount",
        "HKQuantityTypeIdentifierActiveEnergyBurned",
        "HKQuantityTypeIdentifierBasalEnergyBurned",
    ]
    available_flags = [f for f in selected_flags if f in parser.flags]

    for flag in available_flags:
        data = parser.get_flag_records(flag=flag)

        # plot data
        plt = Plot(data=data, operation="sum")
        plt.plot(save=True)

        # log basic stats
        data_name = flag.replace("HKQuantityTypeIdentifier", "")
        data_sum = sum(data.records["value"])
        units = data.records["unit"][0]
        logger.info(f"{data_name}: {data_sum} ({units})")


if __name__ == "__main__":
    args = parse_args()
    process_data(args.path)
