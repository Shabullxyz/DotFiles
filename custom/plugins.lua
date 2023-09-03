local overrides = require "custom.configs.overrides"

return {

{"neovim/nvim-lspconfig",
   config = function()
      require "plugins.configs.lspconfig"
      require "custom.configs.lspconfig"
   end,},
  { "nvim-tree/nvim-tree.lua", opts = overrides.nvimtree},
  { "nvim-treesitter/nvim-treesitter", opts = overrides.treesitter},
  { "williamboman/mason.nvim", opts = overrides.mason},
}

