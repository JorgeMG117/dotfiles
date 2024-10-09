-- Disable netrw at the very start of your init.lua (recommended when using nvim-tree)
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

-- Optionally enable 24-bit color in the terminal
vim.opt.termguicolors = true

vim.keymap.set('n', '<leader>e', ":NvimTreeToggle<CR>", { noremap = true, silent = true, desc = 'Toggle NvimTree' })


-- Define the function to handle key mappings for nvim-tree
local function my_on_attach(bufnr)
  local api = require "nvim-tree.api"

  local function opts(desc)
    return { desc = "nvim-tree: " .. desc, buffer = bufnr, noremap = true, silent = true, nowait = true }
  end

  -- Default nvim-tree mappings
  api.config.mappings.default_on_attach(bufnr)

  -- Custom key mappings
  vim.keymap.set('n', '<C-t>', api.tree.change_root_to_parent, opts('Up'))
  vim.keymap.set('n', '?', api.tree.toggle_help, opts('Help'))
end

-- Set up nvim-tree with options and the custom on_attach function
require("nvim-tree").setup({
  sort = {
    sorter = "case_sensitive",
  },
  view = {
    width = 30,
  },
  renderer = {
    group_empty = true,
  },
  filters = {
    dotfiles = true,
  },
  on_attach = my_on_attach, -- Attach custom key mappings
})

