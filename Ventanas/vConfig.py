# Esta función se ocupará de realizar cálculos para
# colocarse de manera centrada en la pantalla.
from tkinter import ttk


def CentraPantalla(master, ancho, alto):
    anchuraPantalla = master.winfo_screenwidth()
    alturaPantalla = master.winfo_screenheight()

    posx = int((anchuraPantalla / 2) - (ancho / 2))
    posy = int((alturaPantalla / 2) - (alto / 2))

    posicion = str(ancho) + 'x' + str(alto) + '+' + str(posx) + '+' + str(posy)
    return posicion
    

def PreparaEstilos():
    fuente = 'Source Serif Pro ExtraLight'
    st = ttk.Style()
    st.theme_use('clam')

    st.map('Custom.TButton',
        background=[('active', '#EEEEEE')],
        foreground=[('active', '#000000')])

    st.configure(
        'Custom.TButton',
        borderwidth=3,
        background='#FFFFFF',
        bordercolor='#00455F',
        lightcolor='#00455F',
        darkcolor='#00455F',
        foreground='#000000',
        font=(fuente, 11)
    )

    st.configure(
        'Custom.TLabel',
        background='#FFFFFF',
        foreground='#00455F',
        font=(fuente, 20,'bold')
    )

    st.configure(
        'Title.TLabel',
        background='#00455F',
        foreground='#FFFFFF',
        font=(fuente, 30,'bold')
    )

    st.configure(
        'TimesTitle.TLabel',
        background='#FFFFFF',
        foreground='#00455F',
        font=(fuente, 20,'bold')
    )

    st.configure(
        'Times.TLabel',
        background='#FFFFFF',
        foreground='#00455F',
        font=(fuente, 15,'bold')
    )

    st.configure(
        'Cbox.TLabel',
        background='#FFFFFF',
        font=(fuente, 10)
    )