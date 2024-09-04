from pprint import pprint

def outputJSON(barcodes, strdt):
    filename = "json/" + strdt + ".json"
    file = open(filename, 'w')
    print(barcodes, file=file)
    file.close()
    return 0, filename