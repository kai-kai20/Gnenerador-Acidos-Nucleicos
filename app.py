import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
def generar_icono_base(base):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
  if base == 'Adenina':
        color = 'red'
    elif base == 'Timina':
        color = 'blue'
    elif base == 'Citosina':
        color = 'green'
    elif base == 'Guanina':
        color = 'yellow'
    elif base == 'Uracilo':
        color = 'purple'
    else:
        color = 'white'
      circle = plt.Circle((0, 0), 0.8, color=color, ec="black", lw=2)
    ax.add_artist(circle)
ax.text(0, 0, base, ha='center', va='center', fontsize=12, color='white')
   ax.axis('off')
   st.pyplot(fig)
st.title('Generador de Iconos de Ácidos Nucleicos')
base_seleccionada = st.selectbox(
    'Selecciona una base nitrogenada:',
    ['Adenina', 'Timina', 'Citosina', 'Guanina', 'Uracilo']
)
generar_icono_base(base_seleccionada)
