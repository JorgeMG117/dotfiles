#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
# PS1='[\u@martinez \W]\$ '
PS1="\e[0;34m \u@martinez \W \$\e[m "

### RANDOM COLOR SCRIPT ###
# colorscript random

# My commands folder
export PATH="$HOME/.local/bin:$PATH"

# Alias
alias vim='nvim'
alias mv='mv -i'
# alias rm='rm -i'

# Changing "ls" to "exa"
#alias ls='exa -al --color=always --group-directories-first' # my preferred listing
#alias la='exa -a --color=always --group-directories-first'  # all files and dirs
#alias ll='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
#alias l.='exa -a | egrep "^\."'

alias f='ranger'


alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

# Exports
export EDITOR=nvim
#export HISTCONTROL=ignoreboth

### nvim as manpager
#export MANPAGER="nvim -c 'set ft=man' -"

export PATH=$PATH:/home/jorge/.config/coc/extensions/coc-clangd-data/install/12.0.1/clangd_12.0.1/bin

# Starship shell prompt
eval "$(starship init bash)"
#[ -f "/home/jorge/.ghcup/env" ] && source "/home/jorge/.ghcup/env" # ghcup-env
. "$HOME/.cargo/env"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH=$BUN_INSTALL/bin:$PATH


# Load Angular CLI autocompletion.
# source <(ng completion script)
