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

Way to manage the dotfiles inspired in
[https://www.atlassian.com/git/tutorials/dotfiles](https://www.atlassian.com/git/tutorials/dotfiles)

# Login and window manager

```bash
sudo pacman -S xorg lightdm lightdm-gtk-greeter qtile
```

```bash
sudo systemctl enable lightdm
```

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

# Fonts

# Audio

```bash
sudo pacman -S pulseaudio pavucontrol
```

```bash
sudo pacman -S brightnessctl
```

# Monitors

```bash
sudo pacman -S arandr
```

# File Manager

```bash
sudo pacman -S thunar ranger
```
