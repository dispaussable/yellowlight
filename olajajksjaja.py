import gradio as gr

def responder(mensaje):
    return "Hola, estoy aquí para escucharte. ¿Cómo te sientes hoy?"

gr.Interface(fn=responder, inputs="text", outputs="text").launch()
