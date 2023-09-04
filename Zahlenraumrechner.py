import streamlit as st
import time
from PIL import Image


def eingabecheck(hexzahl):
    result = [i for i in hexzahl.upper() if i in ziffern]
    if len(result) == len(hexzahl):
        return True
    else:
        return False

ziffern = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
dezimal = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]

def hextodec(zahlstring):
    num = len(zahlstring)-1
    zahlstring = zahlstring.upper()
    #result = [int(dezimal[ziffern.index(i)])*16**num for j in ziffern for i in zahlstring if i ==j]
    list=[]

    for i in zahlstring:
        for j in ziffern:
            if i == j:
                x = int(dezimal[ziffern.index(i)])*16**num
                num -= 1
                list.append(x)
                result = sum(list)
    return result




def umrechner(hexzahl:str):
    red = hextodec(hexzahl[0:2])
    gruen = hextodec(hexzahl[2:4])
    blau = hextodec(hexzahl[4:6])
    return [red,gruen,blau]


st.title("Samaras Hexenküche🦉")

st.write("Gib einen 6stelligen Hexcode ein:")
colorcode = st.text_input("Eingabe:", max_chars=6)
col1,col2 = st.columns([3,1])
with col1:
    st.write("Gib 6 Zeichen ein!")
    st.write("Gib eine Ziffer von 0-9 oder A-F ein")
    st.write("Dreh dich  im 3-mal im Kreis!")

button = st.button("Hex hex 🧙‍♀️")
if button:
    with col2:
        if len(colorcode) == 6:
            st.write("✔")
        else:
            st.write("❌")
        if eingabecheck(colorcode)== True:
            st.write("✔")
        else:
            st.write("❌")
        time.sleep(4)
        st.write("✔")
    color = "#"+colorcode
    farbanteile = umrechner(colorcode)


    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('rot.png', f"Rot = {farbanteile[0]}")
    with col2:
        st.image('grün.png', f"Grün = {farbanteile[1]}")
    with col3:
        st.image('blau.png', f"Blau = {farbanteile[2]}")

    st.write("")

    img = Image.open("blanc_cauldron.png")
    img = img.convert("RGBA")

    d = img.getdata()

    new_image = []
    for item in d:

        # change all white (also shades of whites)
        # pixels to yellow
        if item[0] in list(range(250, 256)):
            new_image.append((farbanteile[0], farbanteile[1], farbanteile[2]))
        else:
            new_image.append(item)

    # update image data
    img.putdata(new_image)

    # save new image
    img.save("colored_cauldron.png")
    st.image("colored_cauldron.png", use_column_width=True)






