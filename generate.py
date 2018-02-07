"""
Generates personalized invitations.
"""
import csv, base64
from jinja2 import Template

def run():
    """
    void main(char* argv[])
    """
    used_hashes = []
    for lang in ['en', 'lt', 'ru']:
        with open('index_%s.html' % lang) as html, \
                open('guests_%s.csv' % lang) as csv_file:
            template = Template(html.read(), autoescape=True)
            guest_reader = csv.reader(csv_file)
            for row in guest_reader:
                names = row[0]
                code = base64.b64encode(str.encode(names)).decode()[-10:-3] \
                    .replace("/", "_")
                print(code)
                while code in used_hashes:
                    code += "a"
                used_hashes.append(code)
                output_path = 'i_%s.html' % code
                with open(output_path, 'w') as output:
                    output.write(template.render(name=names))
                print(names + "," + output_path)

if __name__ == "__main__":
    run()
