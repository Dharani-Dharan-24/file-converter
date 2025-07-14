import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

from pygments.lexer import default


# from PIL import Image
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

def browse_input():

    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", '*.json'), ("All Files", '*.*')])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def save_as():

    ext = format_var.get()
    default_ext = {'csv' : '.csv', 'excel' : '.xls', 'text' : '.txt'}[ext]
    file_path = filedialog.asksaveasfilename(defaultextension=default_ext)
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def run_conversion():

    input_file = input_entry.get()
    output_file = output_entry.get()
    output_format = format_var.get()

    if not input_file or not output_file:
        messagebox.showwarning("Warning", "Please select a input or output file")

    convert_json(input_file, output_file, output_format)

root = tk.Tk()
root.title("JSON FILE CONVERTER")
root.geometry("500x500")

tk.Label(root, text = 'Select Json file: ').pack(pady = 10)
input_entry = tk.Entry(root, width = 40)
input_entry.pack(padx = 5)
tk.Button(root, text = 'Browse', command=browse_input).pack(pady = 5)

tk.Label(root, text= 'Select Output Format: ').pack(pady = 10)
format_var = tk.StringVar(value='csv')
tk.OptionMenu(root, format_var, 'csv', 'excel', 'text').pack()

tk.Label(root, text = 'Save as').pack(pady = 10)
output_entry = tk.Entry(root, width = 40)
output_entry.pack(pady = 5)
tk.Button(root, text = 'Choose Location', command=save_as).pack(pady = 5)

tk.Button(root, text='Convert', command=run_conversion, bg='green', fg='white').pack(pady = 15)

root.mainloop()


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





