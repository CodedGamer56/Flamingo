import colorful as cf

cf.use_true_colors()

def debug(content):
    print(cf.italic_bold_yellow('!'), cf.italic_bold_yellow(content))

def error(content):
    print(cf.italic_bold_red('#'), cf.italic_bold_red(content))

def msg(content):
    print(cf.italic_white('~'), cf.italic_white(content))