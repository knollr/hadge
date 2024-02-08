#!/usr/bin/env python
import argparse
import pandas as pd

# Create a parser
parser = argparse.ArgumentParser(description="Parameters for Demuxmix")
parser.add_argument("--path_hto", help="cell hashing path, filtered HTO matrix")
parser.add_argument(
    "--hto_name_gmm",
    help="a list of sample tags (HTOs) separated by ',' without whitespace",
)
parser.add_argument(
    "--summary",
    help="Generate the statistical summary of the dataset. Requires an estimated total number of cells in the assay as input",
)
parser.add_argument("--report", help="Name for the summary file generated by GMM")
parser.add_argument("--mode", help="mode csv or tsv")
parser.add_argument(
    "--extract",
    help="Names of the sample barcoding tag(s) to extract, separated by ','. Joint tags are linked with '+'.",
    default="None",
)
parser.add_argument(
    "--threshold_gmm",
    help="Provide the confidence threshold value. Requires a float in (0,1). Default value: 0.8.",
)
parser.add_argument("--outputdir", help="Output directory")
args = parser.parse_args()

# Create parameters DataFrame
params = pd.DataFrame(
    {
        "Argument": [
            "path_hto",
            "hto_name_gmm",
            "summary",
            "report",
            "mode",
            "extract",
            "threshold_gmm",
        ],
        "Value": [
            args.path_hto,
            args.hto_name_gmm,
            args.summary,
            args.report,
            args.mode,
            args.extract,
            args.threshold_gmm,
        ],
    }
)

params.to_csv(f"{args.outputdir}/params.csv", index=False)
