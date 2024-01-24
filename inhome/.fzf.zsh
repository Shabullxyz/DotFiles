# Setup fzf
# ---------
if [[ ! "$PATH" == */home/shabull/.fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}/home/shabull/.fzf/bin"
fi

# Auto-completion
# ---------------
source "/home/shabull/.fzf/shell/completion.zsh"

# Key bindings
# ------------
source "/home/shabull/.fzf/shell/key-bindings.zsh"
