import streamlit as st

st.title('title ->Hello Geeks')
st.header('header ->Hello Geeks')
st.subheader('subheader ->Hello Geeks')
st.text('text ->Hello Geeks')

st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')

st.success('Success')
st.info('Data is submitted')
st.warning('Warning!!')
st.error('Error!!')

st.exception(ZeroDivisionError('Division not possible with 0'))
st.help(ZeroDivisionError)

st.write('range(1,10)')
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x = 10\n'
        'for i in range(x):\n'
            '\tprint(i)')

st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write("You are an adult")


radioButton  = st.radio('Select: ',('Male','Female','Other'))
if(radioButton == 'Male'):
    st.write('You are a male')
elif(radioButton == 'Female'):
    st.write('You are a Female')
elif(radioButton == 'Other'):
    st.write('You are a Other')

st.subheader('Select Box')
selectbox = st.selectbox('Data Science:',['Data Analysis', 'Web Scrapping'])

st.write('you have selected :',selectbox)

st.subheader('Multi -select Box')
selectbox = st.multiselect('Data Science:',['Data Analysis', 'Web Scrapping','AI'])
st.write('you have selected :',len(selectbox))

st.subheader('Button')
if(st.button('Click Me!!')):
    st.write('Thanks')


st.subheader('Slider')
vol = st.slider('Select the level',0,10,step = 1)
st.write('Vol is',vol)

st.subheader('text input')
username = st.text_input('Enter your name:')
password = st.text_input('Enter your password:',type = 'password')
if(username):
    st.write('hi',username)

st.subheader('Text Are')
st.text_area('Write something interesting in 500 words')

st.subheader('Input Number')
st.number_input('select your Age',18,60)

st.subheader('Input Date')
st.date_input('Date Please!!')

st.subheader('Input Time')
st.time_input('Date Please!!')
