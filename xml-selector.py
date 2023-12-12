import os
import tkinter as tk
from tkinter import filedialog, messagebox

def list_xml_files(directory):
    """Return a list of all XML files in the specified directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith('.xml')]

def delete_files(directory, files):
    """Delete the specified files in the given directory."""
    for file in files:
        file_path = os.path.join(directory, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    # Create a root window and immediately hide it (we only want the dialog)
    root = tk.Tk()
    root.withdraw()

    # Open a folder selection dialog
    folder_path = filedialog.askdirectory(title="Select a Folder")

    if not folder_path:  # User closed or canceled the dialog
        print("No folder selected!")
    else:
        xml_files = list_xml_files(folder_path)

        if xml_files:
            print("Found XML files:")
            for file in xml_files:
                print(file)
            
            # Confirm deletion
            response = messagebox.askyesno("Confirm Deletion", "Do you really want to delete these XML files?")
            
            if response:
                delete_files(folder_path, xml_files)
        else:
            print("No XML files found in the specified directory.")
