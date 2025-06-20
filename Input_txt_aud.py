import whisper
from pathlib import Path

def transcribir_audio_whisper(ruta_audio):
    """
    Usa OpenAI Whisper para transcribir un archivo de audio y detectar su idioma automáticamente.
    """
    # Carga del modelo (puedes usar "tiny", "base", "small", "medium", "large")
    print("Cargando modelo Whisper...")
    model = whisper.load_model("base")  # "tiny" es más rápido, "base" es más preciso

    # Verifica que el archivo exista
    ruta = Path(ruta_audio)
    if not ruta.exists():
        print(f"❌ Archivo no encontrado: {ruta}")
        return

    # Transcribe con autodetección de idioma
    print("Transcribiendo con autodetección de idioma...")
    resultado = model.transcribe(str(ruta))

    # Mostrar idioma y texto
    idioma = resultado.get("language", "desconocido")
    texto = resultado.get("text", "")

    print(f"\n🌍 Idioma detectado: {idioma.upper()}")
    print(f"\n📝 Texto transcrito:\n{texto.strip()}\n")

    return idioma, texto

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # Ruta de ejemplo
    archivo_audio = r"C:\Users\BP_motta\Documents\Grabaciones de sonido\prueba.wav"  # Cambia por tu ruta

    # Transcribir
    transcribir_audio_whisper(archivo_audio)