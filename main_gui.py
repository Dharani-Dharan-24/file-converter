import json
from json import JSONDecodeError
from tkinterdnd2 import DND_FILES, TkinterDnD
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, OptionMenu, ttk
import customtkinter as ctk



# from PIL import Image
def convert_json(input_file, output_file, output_format):

    try:
        df = pd.read_json(input_file)
    except:
        try:
            df = pd.read_json(input_file, lines = True)
        except (ValueError, JSONDecodeError) as e:
            raise ValueError(f"Failed to read JSON file {e}")

    if output_format == 'csv 🧾':
        df.to_csv(output_file, index = False)

    elif output_format == 'excel 📊':
        df.to_excel(output_file, index = False, engine = 'openpyxl')

    elif output_format == 'text 📄':
        df.to_string(output_file, index = False)

    else:
        raise ValueError("Invalid Output Format")

def browse_input():

    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", '*.json'), ("All Files", '*.*')])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)


def save_as():

    ext = format_var.get()
    default_ext = {'csv 🧾' : '.csv', 'excel 📊' : '.xls', 'text 📄' : '.txt'}[ext]
    file_path = filedialog.asksaveasfilename(defaultextension=default_ext)
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def run_conversion():

    input_file = input_entry.get()
    output_file = output_entry.get()
    output_format = format_var.get()

    if not input_file or not output_file:
        messagebox.showwarning("Warning", "Please select a input or output file")
        return
    try:
        convert_json(input_file, output_file, output_format)
        show_success()
    except Exception as e:
        messagebox.showerror("Error", f"Conversion Failed:\n {e}")

def show_success():

    success = tk.Label(root, text = " ✅ File Converted Successfully ! ", font=('Arial', 16, 'bold'), fg = 'green', bg = '#EBEBEB')
    success.place(relx = 0.5, rely=0.5, anchor='center')

    def fade():
        alpha = success.winfo_fpixels('1i')
        current_col = success.cget('fg')

        success.after(2000, success.destroy)

    fade()


ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("JSON FILE CONVERTER")
root.geometry("500x500")
root.configure(bg='white')

style = ttk.Style()
style.theme_use("clam")
style.configure("Rounded.TEntry",
                padding=10,
                relief="flat",
                borderwidth=0,
                fieldbackground="white")

tk.Label(root, text = 'Select Json file: ',font = ('Times New Roman', 15, 'bold'), fg = '#36454F', bg = '#EBEBEB').place(x = 20, y = 10)
input_entry = ctk.CTkEntry(root, width=200, height=40, corner_radius=15, placeholder_text="Type File Path or Upload File")
input_entry.pack(pady=(55, 10))
button = ctk.CTkButton(root,
                       command=browse_input,
                       text="Upload File 📤",
                       width=140,
                       height=50,
                       corner_radius=25,
                       fg_color="#00BFFF",
                       hover_color="darkblue",
                       text_color="white",
                       font=("Arial", 16, "bold"))
button.pack()

tk.Label(root, text= 'Select Output Format: ', font = ('Times New Roman', 15, 'bold'), fg = '#36454F', bg = '#EBEBEB').place(x=20, y = 170)
format_var = tk.StringVar(value='csv 🧾')
om = ttk.OptionMenu(root, format_var, 'csv 🧾', 'csv 🧾', 'excel 📊', 'text 📄')

style = ttk.Style(root)
style.theme_use('default')
style.configure("Custom.TMenubutton", font=("Arial", 11, "bold italic"), foreground = '#003366', background = '#EBEBEB', padding=5)
om.config(style="Custom.TMenubutton")
om.pack(pady = (75, 20))

tk.Label(root, text = 'Save as: ', font = ('Times New Roman', 15, 'bold'), fg = '#36454F', bg = '#EBEBEB').pack(pady = (10, 0))
output_entry = ctk.CTkEntry(root, width=200, height=40, corner_radius=15, placeholder_text="Type or Choose Location")
output_entry.pack(pady = (10, 10))
tk.Button(root, text = 'Choose Location  👆', fg = 'brown',command=save_as).pack(pady = 1)

bt = ctk.CTkButton(root,
                       text="CONVERT 🔄",
                       command=run_conversion,
                       width=140,
                       height=50,
                       corner_radius=25,
                       fg_color="green",
                       hover_color="darkgreen",
                       text_color="white",
                       font=("Arial", 16, "bold"))
bt.pack(pady = 15)

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





