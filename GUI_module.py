import tkinter as tk 
import Core 
from Core import system_grammar, system_generate, system_code, check_type
import pycountry
import googletrans
from googletrans import Translator

# we generate the window 
window = tk.Tk()
window.configure(bg="black")

button_text_list = [
    "Save",    
    "Generate nltk code",
    "Generate sentence",
    "version 0.0.1",
    "Picture"
]

# a place to input the plain text enter 
text_cfg = tk.Text(master=window,
fg="black",
height="17",
width="20"
) 


test = """S -> VP NP[1.0]
VP -> 'teste'[1.0]
NP -> 'teste'[1.0]
"""


text_cfg.insert("1.0",test)

# another window to show the generated the sentences from the grammar 
def gen_sentences():
    
    plain_text = text_cfg.get("1.0","end")
# using the functions from Core system already written
    tc = check_type(plain_text)
    print(tc)

    g = system_grammar(plain_text,tc)
    print(g)
    s = system_generate(g,tc)

    gen_window = tk.Tk()

    sentences = tk.Text(master=gen_window)
    
    sentences.insert("1.0",s)

    sentences.grid()
    gen_window.mainloop()

    return True 

def gen_code():
# here importing the fucntions from Core as well we generate the equivalent code based on the grammar 
    plain_text = text_cfg.get("1.0","end")

    tc = check_type(plain_text)
    print(tc)

    c = system_code(plain_text,tc)

    code_window = tk.Tk()

    code = tk.Text(master=code_window
    )

    code.insert("1.0",c)

    code.grid()
    code_window.mainloop()

    return True 

# the button for saving the grammar 
btn_0 = tk.Button(master=window,
text=button_text_list[0],
bg="lightSkyBlue",
borderwidth="2px",
width="22"
)

# button for generating the code
btn_generate = tk.Button(master=window,
text=button_text_list[1],
bg="red",
borderwidth="2px",
width="22",
command=gen_code 
)

# button for generating the sentences based on the grammar 
btn_sentences = tk.Button(master=window,
text=button_text_list[2],
bg="yellow",
borderwidth="2px",
width="22",
command=gen_sentences
)


btn_picture = tk.Button(master=window,
text=button_text_list[4],
width="22",
background="pink"
)

pic_path = tk.Entry(master=window,
width="26"
)

# here a simple label with the actual version 
credits = tk.Label(master=window,
text="version 0.0.1",
font=("Times new romans",10),
width="20")

# from here we just grid all the widgets

btn_0.grid(row=2,column=0)
text_cfg.grid(row=3,column=0)
btn_picture.grid(row=4 ,column=0)
pic_path.grid(row=5,column=0)
btn_generate.grid(row=6,column=0)
btn_sentences.grid(row=7,column=0)

credits.grid(row=8,column=0)


# in order to be able to acess all widget's attributes the configuration window must be the last in the declaration 

def config_window():
     
    c_window = tk.Tk()

    color_pos = ["black","white"]
    lang_pos = []
# here we create a list with all languages that can be encoded with alpha 2 system
    for l in pycountry.languages:

        p = pycountry.languages.get(name=l.name)
        
        try:
            p.alpha_2
            lang_pos.append(p.name)
        except:
            pass 

    l = tk.Label(
        master=c_window,
        text="Language: "
    )

    color = tk.Label(
        master=c_window,
        text="Color:  "
    )

    lng_list = tk.Listbox(
        master=c_window,
        height="1",
        width="8"
    )

    color_list = tk.Listbox(
        master=c_window,
        height="1",
        width="8"
    )

# here we input the values on the list box 
    for c in color_pos:
        color_list.insert(color_pos.index(c),c) 
    for x in lang_pos:
        lng_list.insert(lang_pos.index(x),x)

    def change_color():
# here we get the color style choosed by the user 
        color = color_list.get(color_list.curselection())
        print(color)
        return True 

    def change_language():

        buttons = [btn_0,btn_generate,btn_sentences,credits,btn_picture]

        translator = Translator()

# here we get each language choosed by the user to configure the system
        language = lng_list.get(lng_list.curselection())

        f_language = pycountry.languages.get(name=language)

        v_language = f_language.alpha_2

        counter = 0
        while counter < len(button_text_list):
# then we translate each button tex using the choosen language
            n_text = (translator.translate(button_text_list[counter],dest=v_language)).text    
            buttons[counter]["text"] = n_text 

            counter+=1    

        print(v_language)
        return True 


    save_change = tk.Button(
        master=c_window,
        text="apply",
        bg="lime",
        command=change_color
    )

    save_change_1 = tk.Button(
        master=c_window,
        text="apply",
        bg="tomato",
        command=change_language
    )

    color.grid(row=0,column=0)
    color_list.grid(row=0,column=1)
    lng_list.grid(row=1,column=1)
    l.grid(row=1,column=0)
    save_change.grid(row=0,column=2)
    save_change_1.grid(row=1,column=2)

    c_window.mainloop()


    return True 
# button to open the configurations such as prefered language for the button's label 
btn_config = tk.Button(master=window,
text="Configuration",
bg="grey",
borderwidth="2px",
width="22",
command=config_window
)
btn_config.grid(row=1,column=0)

window.mainloop()
