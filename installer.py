import os
os.system("sudo pacman -S nvim")
os.system("cd ~/.config")
os.system("git clone https://github.com/jdhao/nvim-config")
os.system("mv nvim-config nvim")
os.system("nvim +PackerSync")
