import pandas as pd
from PIL import Image
def convert_json(input_file, output_file, output_format):

    try:
        df = pd.read_json(input_file)
    except:
        df = pd.read_json(input_file, lines = True)

    if output_format == 'csv':
        df.to_csv(output_file, index = False)

    elif output_format == 'excel':
        df.to_excel(output_file, index = False, engine = 'openpyxl')

    elif output_format == 'text':
        df.to_string(output_file, index = False)

    else:
        raise ValueError("Invalid Output Format")

out_file : str = input("Enter Output format: ")

convert_json("input/example.json", "output", out_file)


# def image_conversion(output_format, output_file):
#     with Image.open('input.jpg') as img:
#
#         if output_format == 'png':
#             img.save(output_file + '.png')
#
#         elif output_format == 'bmp':
#             img.save(output_file + '.bmp')
#
#         elif output_format == 'tiff':
#             img.save(output_file + '.tiff')
#
#         else:
#             raise ValueError("Invalid Output Format")





