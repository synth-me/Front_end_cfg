import nltk
from nltk import CFG, PCFG
from nltk.parse.generate import generate 
from nltk.parse import pchart 
import re 

# here we check if the enter text fits a pcfg or cfg 
def check_type(text):

    x = re.search(r"\[", text) 

    if x :
        checked = "pcfg"
        return checked
    else:
        checked = "cfg"
        return checked

# here we transform the plain text in a grammar , depeding on the checked type
def system_grammar(text,grammar_type):
    
    if grammar_type == "pcfg":

        try:
            grammar_g = PCFG.fromstring(text)
        except:
            grammar_g = ""

        return grammar_g

    else:
        try:
            grammar_g = CFG.fromstring(text)
        except:
            grammar_g = ""

        return grammar_g

# given the already built grammar , we generate the sentences 
def system_generate(grammar,grammar_type):

    try:
        s_generated = []
        for sentence in generate(grammar,n=1):
            s_generated.append(" ".join(sentence))
    except:
        s_generated = "There's a problem with the grammar's syntax"

    return s_generated

# here the app generate the equivalent nltk's code based on the well formed syntax  
def system_code(text,grammar_type):

    if grammar_type == "pcfg":
        code = """grammar = PCFG.fromstring("{x}")
    """.format(x=text)
    else:
        code = """grammar = CFG.fromstring("{x}")
    """.format(x=text)

    return code 