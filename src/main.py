import pandas
import streamlit as st
import time


st.title("Streamlit Tests")
st.write("more examples available in the app gallery:  https://streamlit.io/gallery")


st.subheader("Here's our first attempt at using data to create a table:")

st.code(
    """
df = pandas.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
""",
    language="python",
)
df = pandas.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
# here we use 'magic',
# any time that Streamlit sees a variable or a literal value on its own line,
# it automatically writes that to your app using st.write()
df


st.subheader("Show progress")

st.code(
    """
import time

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.05)
""",
    language="python",
)


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.05)

"...and now we're done!"
