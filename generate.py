"""
Generates personalized invitations
"""
from jinja2 import Template

def run():
    """
    void main(char* argv[])
    """
    with open('index.html') as html, open('guests.csv') as csv:
        template_en = Template(html.read())



if __name__ == "__main__":
    run()
