from PIL import Image
import sys
from pprint import pprint
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

txt = tool.image_to_string(
    Image.open('../images/118033088-02.jpeg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
# txt is a Python string

word_boxes = tool.image_to_string(
    Image.open('../images/118033088-02.jpeg'),
    lang="eng",
    builder=pyocr.builders.WordBoxBuilder()
)
print("\nword boxes\n")
pprint(word_boxes)
print("\ntxt\n")
pprint(txt)

# list of box objects. For each box object:
#   box.content is the word in the box
#   box.position is its position on the page (in pixels)
#
# Beware that some OCR tools (Tesseract for instance)
# may return empty boxes

# line_and_word_boxes = tool.image_to_string(
#     Image.open('../images/img4.jpeg'), lang="fra",
#     builder=pyocr.builders.LineBoxBuilder()
# )
# list of line objects. For each line object:
#   line.word_boxes is a list of word boxes (the individual words in the line)
#   line.content is the whole text of the line
#   line.position is the position of the whole line on the page (in pixels)
#
# Each word box object has an attribute 'confidence' giving the confidence
# score provided by the OCR tool. Confidence score depends entirely on
# the OCR tool. Only supported with Tesseract and Libtesseract (always 0
# with Cuneiform).
#
# Beware that some OCR tools (Tesseract for instance) may return boxes
# with an empty content.

# Digits - Only Tesseract (not 'libtesseract' yet !)
# digits = tool.image_to_string(
#     Image.open('test-digits.png'),
#     lang=lang,
#     builder=pyocr.tesseract.DigitBuilder()
# )
# digits is a python string