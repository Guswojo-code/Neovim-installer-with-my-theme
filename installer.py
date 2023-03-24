import os
os.system("sudo pacman -S nvim")
os.system("cd ~/.config")
os.system("git clone https://github.com/jdhao/nvim-config")
os.system("mv nvim-config nvim")
os.system("nvim +PackerSync")
os.system("cd ~/.config/nvim/core/")
os.system("rm colorschemes.lua")
os.system("wget https://raw.githubusercontent.com/Guswojo-code/Neovim-installer-with-my-theme/main/colorschemes.lua")
