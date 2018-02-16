#!/usr/bin/env python

import argparse
import csv

INDEX_AYSO_ID = 15

# Reads in consolidated ratings files and updates a target with rating
# information from a source target

# For example, the All-Star consolidated ratings will be a subset of
# the Fall consolidated ratings.  This script can be used to update the
# Fall (master) consolidated ratings with the updated information from
# the All-Star ratings.

# Input src and target files should match the column layout that looks like this:
# https://docs.google.com/spreadsheets/d/1_8_pq3rl2F-TjtmW0_daFIuTk_k3kbnJIUrfqQ8VSGM/edit?usp=sharing


def parse_args():
    parser = argparse.ArgumentParser(
        description='update target ratings with updated information')
    parser.add_argument(
        '--src',
        '-s',
        required=True,
        help='csv file of player ratings to be updated')
    parser.add_argument(
        '--target', '-t', required=True, help='csv file of new player ratings')
    parser.add_argument(
        '--out',
        '-o',
        required=True,
        help='output file for updated master ratings file')
    return parser.parse_args()


def read_data_from_file(filename):
    result = {}
    fp = open(filename)
    csv_reader = csv.reader(fp, quotechar='"')
    for row in csv_reader:
        try:
            ayso_id = row[INDEX_AYSO_ID]
        except IndexError:
            continue
        result[ayso_id] = row
    fp.close()
    return result


def update_target_data(src_data, target_data):
    for src_ayso_id in src_data:
        try:
            target_data[src_ayso_id]
        except KeyError:
            continue
        target_data[src_ayso_id] = src_data[src_ayso_id]
    return target_data


def write_data_to_file(filename, data):
    fp = open(filename, 'w')
    csv_writer = csv.writer(fp, quotechar='"')
    for ayso_id, details in data.items():
        csv_writer.writerow(details)
    fp.close()


def main():
    args = parse_args()
    src_data = read_data_from_file(args.src)
    target_data = read_data_from_file(args.target)
    updated = update_target_data(src_data, target_data)
    write_data_to_file(args.out, updated)


if __name__ == '__main__':
    main()
