st={10,2,30}
st1={1,2,3}
st2={9,2,3}
st3=st&st1&st2
print(st3)

st3=st.intersection(st1).intersection(st2)
print(st3)