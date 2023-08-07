import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("5000x3500")


numQuery = 1 

def home():
    print("Test")

def addQuery():
    global numQuery
    numQuery += 1
    print(numQuery)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx = 60 , fill = "both", expand = True)


for query in range(numQuery):
    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text=f"Query{ query }")
    entry1.pack(pady=12, padx=10)

add = customtkinter.CTkButton(master=frame, text="Add a query", command=addQuery)
add.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="SLD Resolution", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=home)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()