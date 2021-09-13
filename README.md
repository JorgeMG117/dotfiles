# Overview

This repository contains my personal configurations.
In this guide I will walk you throw all the steps I follow after a fresh Arch Linux installation.

Put this in your .bashrc or .zsh
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

git clone --bare <git-repo> $HOME/dotfiles

alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
config checkout
config config --local status.showUntrackedFiles no
