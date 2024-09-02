import tkinter as tk 

def on_enter(e):
    e.widget['background'] = '#bdb7b7'

def on_leave(e):
    e.widget['background'] = '#ffffff'

def tombol_klik(simbol):
    saat_ini = tampilan.get() 
    
    if saat_ini == "Error":
        tampilan.set("")
    elif simbol == "=":
        try:
            hasil = eval(saat_ini)
            tampilan.set(hasil)
        except ZeroDivisionError:
            tampilan.set("Error")
        except SyntaxError:
            tampilan.set("Error")
    elif simbol == "AC":
        tampilan.set("")
    elif simbol == "DEL":
        saat_ini = saat_ini[:-1]
        tampilan.set(saat_ini)
    else:
        tampilan.set(saat_ini + simbol)

root = tk.Tk() 
root.title("Kalkulator")  
root.geometry("300x400") 

tampilan = tk.StringVar()

masukan = tk.Entry(root, textvariable=tampilan, font=("sans-serif", 20), bd=10, insertwidth=4, width=14, justify="right")  
masukan.grid(row=0, column=0, columnspan=4)


tombol = [
    ('AC', 'DEL', '%', '/'),
    ('7', '8', '9', '*'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('00', '0', '.', '=')
]

lebar_tombol = 5


for i, baris in enumerate(tombol):
    for j, tombol_teks in enumerate(baris):
        tombol_baru = tk.Button(root, text=tombol_teks, font='sans-serif', padx=5, pady=5, command=lambda simbol=tombol_teks: tombol_klik(simbol), relief="raised", bd=5)
        tombol_baru.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        tombol_baru.config(width=lebar_tombol)
        tombol_baru.bind("<Enter>", on_enter)
        tombol_baru.bind("<Leave>", on_leave)
        
        root.grid_columnconfigure(j, weight=1)
        root.grid_rowconfigure(i, weight=1)

    

root.resizable(False, False)        

root.mainloop()
