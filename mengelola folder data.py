import tkinter as tk
from tkinter import filedialog
import os, shutil

root = tk.Tk()
root.title("Pengelola File")
root.geometry("400x200")
root.configure(bg="#f0f0f0")

status_var = tk.StringVar(value="Siap untuk mengelola file.")
tk.Label(root, textvariable=status_var, bg="#111",
            fg="#0ff", font=("Arial", 16, "bold"),
            height=2).pack(fill="x", padx=10, pady=20)

TYPE = {
    "Gambar": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".doc", ".docx", ".pdf", ".txt"],
    "Video": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "code": [".py", ".java", ".cpp", ".js", ".html", 
    ".css", ".PHP", ".json", ".xml", ".c", ".h", 
    ".rb", ".go", ".rs", ".swift", ".kt", ".ts", ".sql", 
    ".sh", ".bat", ".pl", ".lua", ".r", ".m", ".vbs", ".ps1", 
    ".asm", ".s", ".d", ".erl", ".ex", ".exs", ".hs", ".lisp", ".clj", ".scala"],
    "lainnya": []
}

def organize_files(event):
    folder = filedialog.askdirectory()
    if not folder: return

    count = 0 
    for file in os.listdir(folder):
        if "." not in file: continue
        ext = os.path.splitext(file)[1].lower()

        for category, extensions in TYPE.items():
            if ext in extensions:
                target_dir = os.path.join(folder, category)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                    shutil.move(os.path.join(folder, file), os.path.join(target_dir, file))
                count += 1
                break
    status_var.set(f"Berhasil mengelola {count} file.")

frame = tk.Frame(root, bg="#000")
frame.pack(pady=20)

btn_text = "select folder"
btn_widget = tk.Label(frame, text=btn_text, 
                font=("Arial", 12), 
                bg="#f39c12", fg="white", 
                width=20, height=2, relief="flat")
btn_widget.bind("<Button-1>", organize_files)
btn_widget.pack()

tk.Label(root, text="Sorts: Gambar, Docs, Video, Audio, code, lainnya",
         bg="#f0f0f0", fg="#333", 
         font=("Arial", 10, "bold")).pack(side="bottom", pady=10)
         
root.mainloop()