from pathlib import Path

from tkinter import Tk, Canvas, Text, Button, PhotoImage

import main

SCRIPT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = SCRIPT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x700")
window.configure(bg="#FFFFFF")
window.title("Shield RSA - Criptografia de mensagens :)")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

dots = PhotoImage(
    file=relative_to_assets("image_11.png"))
obj_dots = canvas.create_image(
    49.0,
    22.0,
    image=dots
)

logo = PhotoImage(
    file=relative_to_assets("image_12.png"))
obj_logo = canvas.create_image(
    930.0,
    26.0,
    image=logo
)

bg_step_one = PhotoImage(
    file=relative_to_assets("image_9.png"))
obj_bg_step_one = canvas.create_image(
    210.0,
    230.0,
    image=bg_step_one
)

icon_step_one = PhotoImage(
    file=relative_to_assets("image_10.png"))
obj_icon_step_one = canvas.create_image(
    84.0,
    90.0,
    image=icon_step_one
)

canvas.create_text(
    116.0,
    74.0,
    anchor="nw",
    text="TEXTO ORIGINAL",
    fill="#025464",
    font=("Righteous", 20 * -1)
)

input_step_one = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 16 * -1)
)
input_step_one.place(
    x=60.0,
    y=131.0,
    width=300.0,
    height=193.0
)

input_step_one.insert("1.0", "Insira uma mensagem para\nser criptografada...")
input_step_one.bind(
    "<Button-1>", lambda event: main.reset_input(input_step_one))

button_encript = PhotoImage(
    file=relative_to_assets("button_2.png"))
obj_button_encript = Button(
    image=button_encript,
    bg="#FFF",
    activebackground='#FFF',
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
obj_button_encript.place(
    x=242.0,
    y=342.0,
    width=136.0,
    height=54.0
)

obj_button_encript.bind(
    "<Button-1>", lambda event: main.encript(input_step_one, input_step_two, input_step_three, input_public_key, input_private_key))

bg_step_two = PhotoImage(
    file=relative_to_assets("image_7.png"))
obj_bg_step_two = canvas.create_image(
    210.0,
    551.0,
    image=bg_step_two
)

icon_step_two = PhotoImage(
    file=relative_to_assets("image_8.png"))
obg_icon_step_two = canvas.create_image(
    84.0,
    463.0,
    image=icon_step_two
)

canvas.create_text(
    116.0,
    448.0,
    anchor="nw",
    text="TEXTO CRIPTOGRAFADO",
    fill="#025464",
    font=("Righteous", 20 * -1)
)

input_step_two = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 16 * -1)
)
input_step_two.place(
    x=60.0,
    y=506.0,
    width=300.0,
    height=164.0
)

input_step_two.insert("1.0", "Nenhum texto criptografado!")
input_step_two.config(state="disabled")

bg_public_key = PhotoImage(
    file=relative_to_assets("image_5.png"))
obg_bg_public_key = canvas.create_image(
    692.0,
    128.0,
    image=bg_public_key
)

icon_public_key = PhotoImage(
    file=relative_to_assets("image_6.png"))
obj_icon_public_key = canvas.create_image(
    948.0,
    79.0,
    image=icon_public_key
)

canvas.create_text(
    805.0,
    65.0,
    anchor="nw",
    text="KEY PÚBLICA",
    fill="#025464",
    font=("Righteous", 20 * -1)
)

input_public_key = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 16 * -1)
)
input_public_key.place(
    x=437.0,
    y=100.0,
    width=511.0,
    height=84.0
)

input_public_key.insert("1.0", "Nenhuma chave pública gerada!")
input_public_key.config(state="disabled")

bg_private_key = PhotoImage(
    file=relative_to_assets("image_3.png"))
obj_bg_private_key = canvas.create_image(
    692.0,
    311.0,
    image=bg_private_key
)

canvas.create_text(
    802.0,
    227.0,
    anchor="nw",
    text="KEY PRIVADA",
    fill="#025464",
    font=("Righteous", 20 * -1)
)

icon_private_key = PhotoImage(
    file=relative_to_assets("image_4.png"))
obj_icon_private_key = canvas.create_image(
    947.0,
    240.0,
    image=icon_private_key
)

input_private_key = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 16 * -1)
)
input_private_key.place(
    x=437.0,
    y=260.0,
    width=511.0,
    height=126.0
)

input_private_key.insert("1.0", "Nenhuma chave privada gerada!")
input_private_key.config(state="disabled")

bg_step_three = PhotoImage(
    file=relative_to_assets("image_1.png"))
obg_bg_step_three = canvas.create_image(
    695.0,
    550.0,
    image=bg_step_three
)

icon_step_three = PhotoImage(
    file=relative_to_assets("image_2.png"))
obj_icon_step_three = canvas.create_image(
    464.0,
    461.0,
    image=icon_step_three
)

canvas.create_text(
    497.0,
    448.0,
    anchor="nw",
    text="TEXTO DESCRIPTOGRAFADO",
    fill="#025464",
    font=("Righteous", 20 * -1)
)

input_step_three = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 16 * -1)
)
input_step_three.place(
    x=438.0,
    y=494.0,
    width=511.0,
    height=166.0
)

input_step_three.insert("1.0", "Nenhuma mensagem criptografada foi gerada!")
input_step_three.config(state="disabled")

button_descript = PhotoImage(
    file=relative_to_assets("button_1.png"))

obj_button_descript = Button(
    image=button_descript,
    bg="#FFF",
    activebackground='#FFF',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)

obj_button_descript.place(
    x=830.0,
    y=621.0,
    width=136.0,
    height=52.0
)

obj_button_descript.bind(
    "<Button-1>", lambda event: main.descript(input_step_one, input_step_three))

canvas.create_text(
    337.0,
    734.0,
    anchor="nw",
    text="Ciências da Computação 2023/ 2º Período",
    fill="#3D3D3D",
    font=("Poppins Regular", 15 * -1)
)

window.resizable(False, False)
window.mainloop()
