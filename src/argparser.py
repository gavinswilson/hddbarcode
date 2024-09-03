import argparse

def setupargs():
    parser = argparse.ArgumentParser(description = "A barcode reader program!")
    
    # defining arguments for parser object
    parser.add_argument("-r", "--read", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Opens and reads the specified image file.")
    
    parser.add_argument("-c", "--camera", type = int, nargs = 1,
                        metavar = "cam_num", default = None,
                        help = "uses the specified camera to input the image")
     
    parser.add_argument("-s", "--show", type = str, nargs = 1,
                        metavar = "path", default = None,
                        help = "Shows all the text files on specified directory path.\
                        Type '.' for current directory.")
     
    parser.add_argument("-d", "--delete", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Deletes the specified text file.")
     
    parser.add_argument("--rename", type = str, nargs = 2,
                        metavar = ('old_name','new_name'),
                        help = "Renames the specified file to a new name.")
    
    parser.add_argument("-o", "--output", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "sets the output filename for the read image")
    
    return parser
    
