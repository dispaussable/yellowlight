import gradio as gr

def responder(mensaje):
    return "HOLAAAAA SI FUNCIONA!!!!! :p"

gr.Interface(fn=responder, inputs="text", outputs="text").launch()

