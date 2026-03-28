import argparse
import md_2_jsonl
import fine_tuning

parser = argparse.ArgumentParser()
parser.add_argument("--suffix", default=None)
args = parser.parse_args()

fine_tuning.run(suffix=args.suffix)
