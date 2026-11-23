import customtkinter as ctk
# pip install customtkinter

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"

TO_KM = {
    "meter (m)": 0.001,
    "centimeter (cm)": 0.00001,
    "millimeter (mm)": 0.000001,
    "inch (in)": 0.0000254,
    "foot (ft)": 0.0003048,
    "yard (yd)": 0.0009144,
    "kilometer (km)": 1,
    "miles (mi)": 1.60934,
    "nautical miles (nmi)": 1.852,
    "astronomical units (au)": 149597870.7,
    "light years (ly)": 9.4607e+12,
}

def convert():
    try:
        value = float(entry.get())
        fr = combo_from.get()
        to = combo_to.get()

        result = value * TO_KM[fr] / TO_KM[to]
        result_label.configure(text=f"{value:,.3f} {fr} → {result:,.3f} {to}")
    except ValueError:
        result_label.configure(
            text="Masukkan angka yang valid.")

app = ctk.CTk()
app.title("Konversi Jarak")
app.geometry("400x300")
app.resizable(False, False)

entry = ctk.CTkEntry(app, 
            font=("Helvetica", 12), 
            height=30, 
            width=200, 
            justify="center")
entry.pack(pady=20)
entry.focus()

from_frame = ctk.CTkFrame(app)
from_frame.pack(pady=10)
ctk.CTkLabel(from_frame, 
         text="Dari:", 
         font=("Helvetica", 12), 
         width=50, anchor="w").pack(side="left", padx=10)
combo_from = ctk.CTkComboBox(from_frame, 
                values=list(TO_KM.keys()), 
                width=200, 
                height=30, font=("Helvetica", 12))
combo_from.set("meter (m)")
combo_from.pack(side="left", padx=10)

to_frame = ctk.CTkFrame(app)
to_frame.pack(pady=10)
ctk.CTkLabel(to_frame, 
            text="Ke:", 
            font=("Helvetica", 12), 
            width=50, 
            anchor="w").pack(side="left", padx=10)
combo_to = ctk.CTkComboBox(to_frame, 
              values=list(TO_KM.keys()), 
              width=200, 
              height=30, font=("Helvetica", 12))
combo_to.set("kilometer (km)")
combo_to.pack(side="left", padx=10)

result_label = ctk.CTkLabel(app, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

app.bind("<Return>", lambda e: convert())
app.mainloop()