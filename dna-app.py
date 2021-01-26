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
sequence = sequence[1:] # skips the first line (sequence name)
# sequence
sequence = ''.join(sequence) #Concats list into string

st.write("""
***
""")

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# print dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d
X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# Human readable text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) +' adenine (A)')
st.write('There are ' + str(X['T']) +' thymine (T)')
st.write('There are ' + str(X['G']) +' guanine (G)')
st.write('There are ' + str(X['C']) +' cytosine (C)')

# Display Dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)
