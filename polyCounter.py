import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pywavefront import Wavefront

# Function calculating polygon count of an OBJ file
def calculate_obj_polygon_count(obj_filename):
    obj = Wavefront(obj_filename)
    polygon_count = len(obj.mesh_list[0].faces)
    return polygon_count

# Function processing OBJ files and checking polygon counts
def process_files():
    folder_path = filedialog.askdirectory(title="Select a folder containing OBJ files") 

    if not folder_path:
        return
    
    polygon_threshold = int(entry_threshold.get())

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.lower().endswith('.obj'):
            polygon_count = calculate_obj_polygon_count(file_path)

            if polygon_count >= polygon_threshold:
                result_label.config(text=f"{filename}: Polygon count exceeds {polygon_threshold}")
            else:
                result_label.config(text=f"{filename}: Polygon count below {polygon_threshold}")    
