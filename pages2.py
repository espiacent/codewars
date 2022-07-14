import pyperclip


def inhalt(start, end):
    out = ["", "[zurück zur Übersicht](ha_übersicht.md)", "", "## Inhalt"]
    for i in range(start, end + 1):
        s_1 = "### {}".format(i)
        out.append(s_1)
        out.append("*")
        out.append(">")
        continue
    out.append("---")
    out.append("[zurück zur Übersicht](ha_übersicht.md)")
    joined = "\n".join(out)
    pyperclip.copy(joined)


inhalt(53, 67)
