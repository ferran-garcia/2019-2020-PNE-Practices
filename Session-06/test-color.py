import termcolor

termcolor.cprint("Testing colors", 'green')
print_red_on_cyan = lambda x: termcolor.cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')
text = termcolor.colored('Hello, World!', 'red', attrs=['underline', 'blink'])
print(text)