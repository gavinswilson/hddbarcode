# hddbarcode

## Description

A reader designed to look at HDD, SSD, NVME labels etc and read all manufacturer information, outputiing to a JSON for upload through and API.

## Usage
'''
usage: main.py [-h] [-i file_name] [-c cam_num] [-o file_name] [-d file_name]

A barcode reader program!

options:
  -h, --help            show this help message and exit
  -i file_name, --input file_name
                        Opens and reads the specified image file.
  -c cam_num, --camera cam_num
                        uses the specified camera to input the image
  -o file_name, --output file_name
                        sets the output filename for the read image
  -d file_name, --debug file_name
                        sets the output logging level for debug
'''
