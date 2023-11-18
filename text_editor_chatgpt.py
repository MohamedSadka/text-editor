import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    file_path = askopenfilename(title="Open File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_edit.delete(1.0, tk.END)  # Clear previous content
                text_edit.insert(tk.END, content)
            window.title(f"Simple Text Editor - {file_path}")
        except Exception as e:
            error_message = f"Error opening file: {e}"
            tk.messagebox.showerror("Error", error_message)

def save_file():
    file_path = asksaveasfilename(title="Save As", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                content = text_edit.get(1.0, tk.END)
                file.write(content)
            window.title(f"Simple Text Editor - {file_path}")
        except Exception as e:
            error_message = f"Error saving file: {e}"
            tk.messagebox.showerror("Error", error_message)

# Create the main window
window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("600x400")

# Configure row and column weights for resizing
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Create Text widget for editing
text_edit = tk.Text(window, wrap="word", bg="lightgray", padx=20, pady=20)
text_edit.grid(row=0, column=1, sticky="nsew")

# Create frame for buttons
frame_borders = tk.Frame(window, relief=tk.RAISED)
frame_borders.grid(row=0, column=0, sticky='ns')

# Create Open File button
btn_open = tk.Button(frame_borders, text="Open File", command=open_file, bg="lightblue", fg="blue", font=("Arial", 10))
btn_open.grid(row=0, column=0, padx=5, pady=5, ipadx=2, ipady=2, sticky='ew')

# Create Save As button
btn_save = tk.Button(frame_borders, text="Save As", command=save_file, bg="lightblue", fg="blue", font=("Arial", 10))
btn_save.grid(row=1, column=0, padx=5, pady=5, ipadx=2, ipady=2, sticky='ew')

# Start the Tkinter event loop
window.mainloop()
