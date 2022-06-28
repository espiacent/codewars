import pyperclip
def testing(times):
    i = 1
    out = []
    while i <= times:
        s_1 = "### {}".format(i)
        out.append(s_1)
        i += 1
        continue
    joined = "\n".join(out)
    pyperclip.copy(joined)

testing(25)
