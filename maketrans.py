intab='aeiou'
outab='12345'
trans=str.maketrans(intab,outab)
st='my name is ansh saxena'
out=st.translate(trans)
print(out)
