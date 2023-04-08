# library
import streamlit as st

# write
st.title('Software Perkalian')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan bulat')

# Input bilangan pertama
number1= st.number_input('Masukan bilangan pertama')
st.write(f'Bilangan pertama {number1}')

# Input bilangan kedua
number2= st.number_input('Masukan bilangan kedua')
st.write(f'Bilangan kedua {number2}')

# hasil
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan pencet tombol hitung!')
