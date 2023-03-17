#!/bin/bash
pacman -S neovim
echo "Downloaded base vim"
mkdir "~/.config/"
echo "Made the config file!"
mkdir "~/.config/nvim"
echo "Made the neovim config"
cd "~/.config/nvim/"
git clone "~/.config/nvim"
echo "Downloaded the Neovim config!"
echo "Done!"
