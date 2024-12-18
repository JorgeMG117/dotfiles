# Overview

This repository contains my personal configurations.
In this guide I will walk you throw the steps I follow after an Arch Linux installation.

# Installation

```bash
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
repo='https://github.com/JorgeMG117/dotfiles.git'

git clone --bare $repo $HOME/dotfiles

config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | \
xargs -I{} rm {}

config checkout

config config --local status.showUntrackedFiles no
```

To update the dotfiles, execute the following commands for the files to upload

```bash
config status
config add README.md
config commit -m "Update README"
config push origin master #Change origin to your own repository
```


Way to manage the dotfiles inspired in
[https://www.atlassian.com/git/tutorials/dotfiles](https://www.atlassian.com/git/tutorials/dotfiles)

# Login and window manager

```bash
sudo pacman -S xorg lightdm lightdm-gtk-greeter qtile
```

```bash
sudo apt install i3
```

```bash
sudo systemctl enable lightdm
```

Change the theme of *lightdm* to make it look cooler

```bash
pacman -S --needed lightdm-webkit2-greeter lightdm-webkit-theme-litarvan
```

Edit /etc/lightdm/lightdm.conf and set greeter-session=lightdm-webkit2-greeter

Edit /etc/lightdm/lightdm-webkit2-greeter.conf and set theme or webkit-theme to litarvan

# Terminal emulator

```bash
sudo pacman -S alacritty
```

# Program launcher

```bash
sudo pacman -S rofi
```

# Wallpaper

```bash
sudo pacman -S feh
```

To change the background, modify the following code in the qtile configuration

```python
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.run(["feh", "--bg-scale", home + "/wallpapers/0178.jpg"])
```

# Fonts

Nerd Fonts can be downloaded from the following website.

[Nerd Fonts download website](https://www.nerdfonts.com/font-downloads)

With the downloaded zip, execute the following commands.


```bash
sudo cp [font-name.zip] /usr/share/fonts/

cd /usr/share/fonts/

sudo unzip [font-name.zip]

fc-cache -fv
```

# Audio

```bash
sudo pacman -S pulseaudio pavucontrol
```

```bash
sudo pacman -S brightnessctl
```


# Clipboard 

```bash
sudo pacman -S xclip xsel
```

# Monitors

```bash
sudo pacman -S arandr
```

# File Manager

```bash
sudo pacman -S thunar ranger
```

# Other Software
```bash
sudo pacman -S exa # Replacement for ls
sudo pacman -S ripgrep
sudo pacman -S picom # Transparency
sudo pacman -S gcc go
```


# Neovim

If you want to install [Neovim](https://github.com/neovim/neovim/blob/master/BUILD.md) from source.

I am currently using [lazy.nvim](https://github.com/folke/lazy.nvim) as package manager.

To setup Copilot check [copilot](https://github.com/github/copilot.vim)

 

# Tmux

```bash
sudo pacman -S tmux

git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```




