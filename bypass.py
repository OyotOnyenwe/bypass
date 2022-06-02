# The O-Ring Bypass, Automated
# by Oyot Onyenwe
# Version 1.0.0

import tkinter as tk
import subprocess as sp
from time import sleep

def bypass():
    
    name = "en0"
    sp.run(["networksetup", "-setairportpower", name, "off"])
    sleep(1)
    sp.run(["networksetup", "-setairportpower", name, "on"])
    sleep(1)


window = tk.Tk()
window.title("The O-Ring Bypasser")

tk.Label(text = "").grid(row = 0, column = 0)
tk.Label(text = "Click to perform the Bypass:").grid(row = 1, column = 0)
tk.Button(text = "Activate", command = bypass).grid(row = 1, column = 1)
tk.Label(text = "").grid(row = 2, column = 0)

window.mainloop()
