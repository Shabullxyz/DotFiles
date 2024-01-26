local M = {}

M.treesitter = {
  ensure_installed = {
    "vim",
    "html",
    "css",
    "javascript",
    "json",
    "markdown",
    "python",
    "bash",
    "lua",
    "tsx",
    "typescript",
    "toml",
    "rust",
    "php",
  },
}

M.nvimtree = {


  view = {
    adaptive_size = false,
    side = "right",
    width = 30,
    preserve_window_proportions = true,
  },
  filters = {
    dotfiles = true,
    custom = { "node_modules" },
  },

  git = {
    enable = true,
  },

  renderer = {
    highlight_git = true,
    icons = {
      show = {
        git = true,
      },
    },
  },
}

M.mason = {
  ensure_installed = {
    -- lua stuff
    "lua-language-server",
    "stylua",

    -- web dev
    "css-lsp",
    "html-lsp",
    "typescript-language-server",

    -- "emmet-ls",
    "json-lsp",
    "tailwindcss-language-server",

    -- shell
    "shfmt",
    "shellcheck",
    "bash-language-server",
    --python
    "black",
    "djlint",
    "jedi-language-server",
    "mypy",
    "pyright",


 },
}
--
return M
