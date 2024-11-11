import gradio as gr

# Function to replace the word 'World' to 'Gradio'
def replace(text):
    return text.replace('World', 'Gradio')

gr.Interface(fn=replace,
             inputs='textbox',
             outputs='textbox').launch()