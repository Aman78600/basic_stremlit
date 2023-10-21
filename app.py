import streamlit as st
st.title("-> hello world, today is butifull.")
st.header('header -> it is header tag')
st.subheader('subheader -> it is subheader.')
st.text('text -> it is text.')

st.markdown("# hi")
st.markdown("## hi")
st.markdown("### hi")
st.markdown("### hi")
st.markdown("#### hi")
st.markdown("##### hi")

st.success('it is success')
st.info("info function")
st.warning('warning!')
st.error('error!')

expration = ZeroDivisionError('division not possible with 0')


st.exception(expration)
st.exception(ZeroDivisionError('division is not possible'))
st.help(ZeroDivisionError)

st.code('x=10\n'
        'for i in range(1,x+1):\n'
        '   print(i)')


st.checkbox('Male')

if (st.checkbox('Female')):
    st.write('you are Female.')


radioButton = st.radio('select :', {'male', 'female', 'other'})
if (radioButton == 'male'):
    st.write('you are male.')
elif (radioButton == 'female'):
    st.write('you are female.')
else:
    st.write('you are other')


st.subheader('select box')
st.selectbox('Data science :', {'data analysis', 'web scraping', 'machine learning',
             'deep learning', 'NLP', 'computer vision', 'image processing'})


multiselectBox=st.multiselect('Data science :', {'data analysis', 'web scraping', 'machine learning',
             'deep learning', 'NLP', 'computer vision', 'image processing'})

st.write('you selected : ',len(multiselectBox),'coutses')







st.subheader('Button')
if st.button("click me."):
    st.write('you click button.')

rang=st.slider('select your rang :',0,10,step=1)
st.write('your rang is ',rang)

username=st.text_input('username')
password=st.text_input('password',type='password')
# if name:
#         st.write('hi',name)

st.subheader('text area')
textArea=st.text_area('write code')
st.write(textArea)

st.subheader('input number')
st.number_input('enter your age',18,100)

st.subheader('input data')
st.date_input('enter your birthdate')

