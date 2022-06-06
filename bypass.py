# The O-Ring Bypass, Automated
# by Oyot Onyenwe
# v1.1.1

import tkinter as tk
import subprocess as sp
from time import sleep

# Figure out which hardware port Wi-Fi runs on
def name_get():
    devlist = str(sp.run(["networksetup", "-listallhardwareports"], stdout = sp.PIPE))
    i1 = devlist.find("Wi-Fi") + 15
    cutlist = devlist[i1:]
    i2 = cutlist.find("Ethernet") - 2
    name = cutlist[:i2]
    return name

# Disable the port, then reenable
def bypass():
    name = name_get()
    sp.run(["networksetup", "-setairportpower", name, "off"])
    sleep(1)
    sp.run(["networksetup", "-setairportpower", name, "on"])
    sleep(1)

# Tkinter GUI Code
window = tk.Tk()
window.title("O-Ring Bypasser v1.1.1")

tk.Label(text = "").grid(row = 0, column = 0)
tk.Label(text = "Click to perform the Bypass:").grid(row = 1, column = 0)
tk.Button(text = "Activate", command = bypass).grid(row = 1, column = 1)
tk.Label(text = "").grid(row = 2, column = 0)

window.mainloop()
