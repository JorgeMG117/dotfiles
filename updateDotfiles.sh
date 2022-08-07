#!/bin/bash

/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME status -s | cut -d' ' -f 3 |
while read line
do
    /usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME add "$line"
done

/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME commit -m \""$1"\"

