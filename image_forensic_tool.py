# Digital Forensic Tool for Images
# Author: Aryan Dumale
# Tool: Image Metadata + Hashing Forensic Analyzer

import os
import hashlib
from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return "No metadata found."
        metadata = ""
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata += f"{tag:25}: {value}\n"
        return metadata
    except Exception as e:
        return f"Error reading metadata: {e}"

def calculate_hash(image_path):
    try:
        md5 = hashlib.md5()
        sha = hashlib.sha256()
        with open(image_path, "rb") as f:
            data = f.read()
            md5.update(data)
            sha.update(data)
        return md5.hexdigest(), sha.hexdigest()
    except Exception as e:
        return None, None

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif")]
    )
    if file_path:
        display_results(file_path)

def display_results(image_path):
    metadata = extract_metadata(image_path)
    md5_hash, sha_hash = calculate_hash(image_path)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"File: {os.path.basename(image_path)}\n")
    result_text.insert(tk.END, f"Location: {image_path}\n\n")
    result_text.insert(tk.END, "---- METADATA ----\n")
    result_text.insert(tk.END, metadata + "\n")
    result_text.insert(tk.END, "---- HASH VALUES ----\n")
    result_text.insert(tk.END, f"MD5:  {md5_hash}\n")
    result_text.insert(tk.END, f"SHA256: {sha_hash}\n")

# GUI setup
root = tk.Tk()
root.title("Digital Forensic Tool for Images")
root.geometry("750x600")
root.configure(bg="#e0f7fa")

tk.Label(root, text="Digital Forensic Tool for Images", 
         font=("Arial", 16, "bold"), bg="#e0f7fa", fg="#00695c").pack(pady=10)

tk.Button(root, text="Browse Image", command=browse_file, 
          bg="#00796b", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=5)

result_text = tk.Text(root, wrap=tk.WORD, width=80, height=25)
result_text.pack(padx=10, pady=10)

root.mainloop()
