import argparse

def setupargs():
    parser = argparse.ArgumentParser(description = "A barcode reader program!")
    
    # defining arguments for parser object
    parser.add_argument("-i", "--input", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Opens and reads the specified image file.")
    
    parser.add_argument("-c", "--camera", type = int, nargs = 1,
                        metavar = "cam_num", default = None,
                        help = "uses the specified camera to input the image")
    
    parser.add_argument("-o", "--output", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "sets the output filename for the read image")
    
    parser.add_argument("-d", "--debug", type = int, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "sets the output logging level for debug")
    
    return parser
    
