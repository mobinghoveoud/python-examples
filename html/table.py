import re
import webbrowser


# bold & italic
def format(text):
    match = re.search("\*(.*)\*", text)
    if match:
        return f"<b>{match.group(1)}</b>"

    match = re.search("_(.*)_", text)
    if re.search("_.*_", text):
        return f"<u>{match.group(1)}</u>"

    return text


with open('sample.html', 'r') as f:
    sampleHtml = f.read()

text = ""
with open('sample.csv', 'r') as f:
    line = f.readline().rstrip().split(',')

    text += "<tr>\n"
    for title in line:
        text += f"    <th>{format(title)}</th>\n"
    text += "</tr>\n"

    for line in f:
        text += f"<tr>\n"
        for t in line.rstrip().split(','):
            text += f"    <td>{format(t)}</td>\n"
        text += "</tr>\n"

with open('final.html', 'w') as f:
    f.write(sampleHtml.replace('@@tr@@', text))

webbrowser.open_new_tab('final.html')
