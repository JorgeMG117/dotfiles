#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
# PS1='[\u@martinez \W]\$ '
PS1="\e[0;34m \u@martinez \W \$\e[m "

### RANDOM COLOR SCRIPT ###
#/opt/shell-color-scripts/colorscript.sh random

# My commands folder
export PATH="$HOME/.local/bin:$PATH"

# Alias
alias mv='mv -i'
# alias rm='rm -i'

# Changing "ls" to "exa"
#alias ls='exa -al --color=always --group-directories-first' # my preferred listing
#alias la='exa -a --color=always --group-directories-first'  # all files and dirs
#alias ll='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
#alias l.='exa -a | egrep "^\."'


alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

# Exports
export EDITOR=nvim
#export HISTCONTROL=ignoreboth

### nvim as manpager
export MANPAGER="nvim -c 'set ft=man' -"

export PATH=$PATH:/home/jorge/.config/coc/extensions/coc-clangd-data/install/11.0.0/clangd_11.0.0/bin

# Flutter
export PATH="$PATH:/home/jorge/development/flutter/bin"

# Starship shell prompt
eval "$(starship init bash)"