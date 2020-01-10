# Set prompt eg. username@hostname :~ $
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
PS1='\[\033[0;32m\]\u\[\033[0m\]@\[\033[0;35m\]\h\[\033[0m\] :\[\033[0;33m\]\w\[\033[1;36m\]$(parse_git_branch)\[\033[0m\] \$ '

# Set LS colors
export CLICOLOR=1
export LSCOLORS=gxBxhxDxfxhxhxhxhxcxcx
