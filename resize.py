import argparse
parser = argparse.ArgumentParser(description="Resize an image.")
parser.add_argument("path", help="path to the image")
parser.add_argument("--width", type=int, default= 800)
parser.add_argument("-v","--verbose", action="store_true")

args = parser.parse_args()

if args.verbose:
    print(f"Resizing {args.path} to width {args.width}")

