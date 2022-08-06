#!/bin/bash

repo='https://github.com/JorgeMG117/dotfiles.git'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

git clone --bare $repo $HOME/dotfiles

mkdir -p .config-backup && \
config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | \
xargs -I{} mv {} .config-backup/{}

config checkout

config config --local status.showUntrackedFiles no

#echo "alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'" >> $HOME/.bashrc
