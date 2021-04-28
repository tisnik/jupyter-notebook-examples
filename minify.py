#!/usr/bin/python
# vim: set fileencoding=utf-8

import json
import sys
import csv

from os import listdir, stat, walk
from os.path import isfile, join

input_directory = "input"
pretty_printed_directory = "prettyprinted"
minified_directory = "minified"


# Retrieve list of files in current directory.
input_files = [f for f in listdir(input_directory)
               if isfile(join(input_directory, f))]

# Iterate over all input files found in current directory.
for filename in input_files:
    print("Processing input file", filename)

    # Just proper JSON files needs to be processed.
    if filename.endswith(".json"):
        # Try to open the given file, read its content, parse it as JSON and
        # use the processed payload later
        with open(join(input_directory, filename)) as fin:
            data = json.load(fin)

            # Delete unused data
            if "Report" in data:
                del data["Report"]["system"]
                del data["Report"]["fingerprints"]
                del data["Report"]["skips"]
                del data["Report"]["info"]
                if "pass" in data["Report"]:
                    del data["Report"]["pass"]
                for report in data["Report"]["reports"]:
                    del report["type"]
                    del report["tags"]
                    del report["links"]

            # Export the updated report in pretty printed format
            outfilename = join(pretty_printed_directory, filename)
            with open(outfilename, "w") as fout:
                json.dump(data, fout, indent=4)

            # Export the updated report in minified format
            outfilename = join(minified_directory, filename)
            with open(outfilename, "w") as fout:
                json.dump(data, fout, separators=(',', ':'))

# Statistic


def file_size(filename):
    info = stat(filename)
    return info.st_size


with open("record_sizes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Filename", "Original", "Cleaned up", "Minified",
                     "Shrinked (%)"])

    for filename in input_files:
        s1 = file_size(join(input_directory, filename))
        s2 = file_size(join(pretty_printed_directory, filename))
        s3 = file_size(join(minified_directory, filename))
        writer.writerow([filename, s1, s2, s3, int(100.0*s3/s1)])
