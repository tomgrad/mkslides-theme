import re

def preprocess(md: str) -> str:
# columns: <!-- c -->, <!-- | -->, <!-- c. -->
    md = re.sub(r"<!--\s*c\s*-->", r'\n<div class="cols" markdown="1"><div markdown="1">\n', md)
    md = re.sub(r"<!--\s*ct\s*-->", r'\n<div class="cols cols-top-align" markdown="1"><div markdown="1">\n', md)
    md = re.sub(r"<!--\s*cb\s*-->", r'\n<div class="cols cols-bottom-align" markdown="1"><div markdown="1">\n', md)
    md = re.sub(r"<!--\s*\|\s*-->", r'\n</div><div markdown="1">\n', md)
    md = re.sub(r'<!--\s*c.\s*-->', r'\n</div></div>\n', md)
    md = re.sub(r"<!--\s*c21\s*-->", r'\n<div class="cols21" markdown="1"><div markdown="1">\n', md)
    md = re.sub(r"<!--\s*c12\s*-->", r'\n<div class="cols12" markdown="1"><div markdown="1">\n', md)
    md = re.sub(r"<!--\s*c31\s*-->", r'\n<div class="cols31" markdown="1"><div markdown="1">\n', md)
    md = re.sub(r"<!--\s*c111\s*-->", r'\n<div class="cols111" markdown="1"><div markdown="1">\n', md)

# width: <!-- w100% -->, <!-- w50% -->
    md = re.sub(r"<!--\s*w([0-9]+)%\s*-->", r'<!-- .element style="width:\1%" -->', md)

# box: <!-- box -->, <!-- . -->
    md = re.sub(r"<!--\s*box\s*-->", r'\n<div class="box" markdown="1">\n', md)

# single close: </div>
    md = re.sub(r"<!--\s*\.\s*-->", r'\n</div>\n', md)

# math: <!-- e -->, <!-- e. -->
    md = re.sub(r"<!--\s*e\s*-->", r'\n<div markdown="1">\\[\\begin{aligned}', md)
    md = re.sub(r"<!--\s*e.\s*-->", r'\\end{aligned}\\]</div>', md)

# fragments: <!-- f0 -->, <!-- f1 -->
    md = re.sub(r"<!--\s*f([0-9]+)\s*-->", r'<!-- .element: class="fragment" data-fragment-index="\1" -->', md)

# fit-text: <!-- fit -->
    md = re.sub(r"<!--\s*fit\s*-->", r'<!-- .element class="r-fit-text" -->', md)

# auto-animate: <!-- anim0 -->, <!-- anim -->
    md = re.sub(r"<!--\s*anim\s*-->", r'<!-- .element data-auto-animate -->', md)
    md = re.sub(r"<!--\s*anim0\s*-->", r'<!-- .element data-auto-animate data-auto-animate-restart -->', md)

    return md

