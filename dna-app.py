import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page title

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA
""")

# Input text box

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence
sequence = sequence[1:] # skips the first line (sequence name)
sequence = ''.join(sequence) #Concats list into string

st.write("""
***
""")

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')
