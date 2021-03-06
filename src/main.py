import argparse
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.ZigModel import ZigModel
from src.ZoneModel import ZoneModel
from src.ModelRunner import ModelRunner


def main():
    parser = argparse.ArgumentParser(description="Simulate Plane Boarding")

    parser.add_argument("--rows", "-r", help="Number of rows on the plane", default=3, type=int)
    parser.add_argument("--visualize", "-v", help="Display Visualizer", default=False, action="store_true")
    parser.add_argument("--model", "-m", help="Model to use", default="zig", choices=["zig", "zone"], type=str)
    parser.add_argument("--constant", "-c", help="Set constant Aisle Movement Rates", default=True, action="store_true")

    args = parser.parse_args()

    if (args.model == "zig"):
        model = ZigModel(args.constant)
    else:
        model = ZoneModel(args.constant)

    runner = ModelRunner()
    runner.run(model, args.rows, 3, args.visualize)


if __name__ == '__main__':
    main()
