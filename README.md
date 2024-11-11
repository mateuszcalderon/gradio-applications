### What is Gradio?
Gradio is a open-source Python library that allows you to quickly create and share interactive user interfaces for machine learning models, data science workflows, or any Python function.

### Getting Started
To start you Gradio projects first you need a Python 3.10 or higher.
<br/> Gradio documentation recommends installing the library using ` pip ` in your terminal or command prompt. Just run ` pip install gradio ` on it and you will be able to code!

1. [Hello World](https://github.com/mateuszcalderon/gradio-applications/blob/main/hello_gradio.py)
<br/> My first 'Hello World' using gradio! Or should we say 'Hello Gradio'?
<br/> On this first project we designed a function called ` replace ` to simply replace the input word 'World' to 'Gradio'.
```python
def replace(text):
    return text.replace('World', 'Gradio')
```

It also includes the interface object and its components. Here both input and output were defined as ` textbox `.
<br/> The ` .launch() ` method runs a web application that lets us interact with the function we have wrapped in the Gradio interface object.
```python
gr.Interface(fn=replace,
             inputs='textbox',
             outputs='textbox').launch()
```

Running locally at: http://127.0.0.1:7860.
