import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("simple text editor")
window.rowconfigure(0 , minsize=300)
window.columnconfigure(1 , minsize=200)

def open_file():
    file_path = askopenfilename(title="Open File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_edit.delete(1.0, tk.END)  # Clear previous content
            text_edit.insert(tk.END, content)
            
    window.title(f"simpletexteditor.{file_path}")

def save_file():
    file_path = asksaveasfilename(title="Save As", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text_edit.get(1.0, tk.END)
            file.write(content)

    window.title(f"simpletexteditor.{file_path}")

text_edit = tk.Text(window, bg="lightgray", padx=20, pady=20)
frame_borders = tk.Frame(window , relief=tk.RAISED)
btn_open = tk.Button(frame_borders , text="Open File", command=open_file , bg="lightblue", fg="blue", font=("Arial", 8))
btn_save = tk.Button(frame_borders , text="Save As", command=save_file, bg="lightblue", fg="blue", font=("Arial", 8))

btn_open.grid(column=0 , row=0 , padx=5 , pady=5 , ipadx=2 , ipady=2 , sticky='ew')
btn_save.grid(column=0 , row=1 , padx=5 , pady=5 , ipadx=2 , ipady=2, sticky='ew')

frame_borders.grid(column=0 , row=0 , sticky='ns')
text_edit.grid(column=1 , row=0 ,)

window.mainloop()