from PIL import Image
import pytesseract

def transcrever_imagem(imagem):
    try:
        imagem_aberta = Image.open(imagem)
        texto = pytesseract.image_to_string(imagem_aberta)
        print("Texto extraído:")
        print(texto)
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

transcrever_imagem('caminho/para/sua/imagem.jpg')
