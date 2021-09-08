let mapleader = " "

noremap <leader>w :w<cr>
noremap <leader>q :q!<cr>

noremap <leader>h <C-w>h
noremap <leader>j <C-w>j
noremap <leader>k <C-w>k
noremap <leader>l <C-w>l

"map <leader>h :wincmd h<cr>
"map <leader>j :wincmd j<cr>
"map <leader>k :wincmd k<cr>
"map <leader>l :wincmd l<cr>

"map - <C-W>-
"map + <C-W>+

" Find files using Telescope command-line sugar.
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

" nnoremap <leader>t :NERDTreeFocus<CR>
" map <leader>t :10sp|:term
map <Leader>t :10sp term://bash<CR>i
tnoremap jj <C-\><C-n>
"nnoremap Ctrl+o Ctrl+\ Ctrl+N 

""TEX
autocmd FileType tex inoremap ,be \begin{}<Enter><Enter>\end{}<Esc>ki

:imap jj <Esc>
