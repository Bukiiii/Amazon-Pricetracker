import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def entry():
    print("Test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Produkt URL", font=("Roboto", 24))
label.pack(pady=12, padx=10)

url_entry= customtkinter.CTkEntry(master=frame, placeholder_text="URL eingeben...")
url_entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Eingeben", command=entry)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
button.pack(pady=12, padx=10)

root.mainloop()