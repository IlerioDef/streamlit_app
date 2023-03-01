# Libraries
import streamlit as st
from PIL import Image


# Confit
st.set_page_config(page_title='Lorem Ipsum', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Lorem Ipsum')

st.write(
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam elementum pulvinar etiam non quam lacus. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt. Ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt. Purus semper eget duis at. Mauris cursus mattis molestie a iaculis at erat pellentesque. Semper auctor neque vitae tempus quam. Quis hendrerit dolor magna eget est lorem. Accumsan tortor posuere ac ut consequat. Sed blandit libero volutpat sed cras. Amet nulla facilisi morbi tempus.

Purus gravida quis blandit turpis cursus in hac habitasse. Nibh sed pulvinar proin gravida. Quam pellentesque nec nam aliquam sem et tortor consequat. Mattis molestie a iaculis at. Dictum sit amet justo donec enim diam vulputate ut pharetra. Amet luctus venenatis lectus magna fringilla urna. Tellus integer feugiat scelerisque varius morbi enim nunc faucibus a. Sed velit dignissim sodales ut eu sem integer vitae. Habitasse platea dictumst vestibulum rhoncus. Integer enim neque volutpat ac. Tellus at urna condimentum mattis pellentesque id. Amet facilisis magna etiam tempor orci. Augue mauris augue neque gravida in fermentum et. Libero volutpat sed cras ornare arcu dui vivamus arcu. Eu tincidunt tortor aliquam nulla. Quam pellentesque nec nam aliquam sem et tortor consequat. Quisque sagittis purus sit amet volutpat. Orci dapibus ultrices in iaculis nunc.

Amet nulla facilisi morbi tempus iaculis. Tellus elementum sagittis vitae et leo duis ut diam. Ultrices tincidunt arcu non sodales neque sodales. Lorem sed risus ultricies tristique. At urna condimentum mattis pellentesque id nibh tortor. Quis viverra nibh cras pulvinar mattis. Ut tristique et egestas quis. Nunc sed augue lacus viverra vitae congue eu consequat ac. Mauris cursus mattis molestie a iaculis. Pulvinar etiam non quam lacus. Magna sit amet purus gravida quis blandit turpis. Eu non diam phasellus vestibulum lorem sed risus ultricies tristique. Ut etiam sit amet nisl purus in mollis. Ipsum nunc aliquet bibendum enim facilisis gravida neque. Volutpat ac tincidunt vitae semper quis lectus nulla. Enim sit amet venenatis urna. Phasellus egestas tellus rutrum tellus pellentesque eu tincidunt. Odio morbi quis commodo odio aenean. Elementum tempus egestas sed sed risus pretium quam.

Commodo quis imperdiet massa tincidunt. Vel turpis nunc eget lorem dolor sed. Amet risus nullam eget felis eget nunc lobortis mattis. Dui vivamus arcu felis bibendum ut tristique. Egestas integer eget aliquet nibh praesent tristique magna sit. Sit amet justo donec enim diam. Convallis aenean et tortor at risus viverra adipiscing. Sagittis vitae et leo duis. Mi eget mauris pharetra et ultrices neque. Sed faucibus turpis in eu mi bibendum. Magna etiam tempor orci eu lobortis elementum nibh. Sit amet consectetur adipiscing elit duis. Odio eu feugiat pretium nibh ipsum. Vel turpis nunc eget lorem dolor sed viverra. Turpis egestas integer eget aliquet nibh praesent. Pharetra sit amet aliquam id diam maecenas.

Tristique risus nec feugiat in fermentum. Non arcu risus quis varius quam quisque. Integer eget aliquet nibh praesent. Tellus at urna condimentum mattis pellentesque id. Dui faucibus in ornare quam viverra orci. Dis parturient montes nascetur ridiculus mus. Enim eu turpis egestas pretium aenean. Ipsum a arcu cursus vitae congue mauris rhoncus. Duis ultricies lacus sed turpis tincidunt id aliquet risus. Facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Elementum facilisis leo vel fringilla est ullamcorper eget. Ullamcorper sit amet risus nullam eget felis eget nunc. At volutpat diam ut venenatis tellus in. Scelerisque eleifend donec pretium vulputate. Interdum varius sit amet mattis. Phasellus faucibus scelerisque eleifend donec pretium. Neque convallis a cras semper auctor neque vitae tempus. Habitant morbi tristique senectus et netus et malesuada."""
)
st.subheader("Test subheader 1")
st.sidebar.empty()
st.sidebar.button("test button 1")




c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@]()**', icon="💡")
with c2:
    st.info('**GitHub: [@]()**', icon="💻")
with c3:
    st.info('**Data: []()**', icon="🧠")