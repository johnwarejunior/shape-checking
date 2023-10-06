import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pywavefront import Wavefront

# Function to calculate polygon count of an OBJ file
def calculate_obj_polygon_count(obj_filename):
    obj = Wavefront(obj_filename)
    polygon_count = len(obj.mesh_list[0].faces)
    return polygon_count