from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path


ROOT_DIR = Path(__file__).parent
FILE1 = ROOT_DIR / 'operadores.png'
OUTPUT = ROOT_DIR / 'melhoradas/operadores_melhorada.png'


def enhance_image(FILE1, OUTPUT):
    # Abrir a imagem
    img = Image.open(FILE1)
    
    # Verificar se a imagem já está em 1080x1080
    if img.size == (1080, 1080):
        img = img.resize((4160, 4160), Image.LANCZOS)
    
    # Aplicar nitidez
    sharpness = ImageEnhance.Sharpness(img)
    img = sharpness.enhance(2.0)  # Aumenta a nitidez
    
    # Ajustar o contraste
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.3)  # Aumenta o contraste
    
    # Ajustar o brilho
    brightness = ImageEnhance.Brightness(img)
    img = brightness.enhance(1.1)  # Aumenta levemente o brilho
    
    # Ajustar a cor
    color = ImageEnhance.Color(img)
    img = color.enhance(1.2)  # Aumenta a saturação
    
    # Reduzir ruído aplicando um leve desfoque e depois aumentando a nitidez
    img = img.filter(ImageFilter.SMOOTH)
    img = img.filter(ImageFilter.SHARPEN)
    
    # Salvar a imagem melhorada
    img.save(OUTPUT, quality=100)
    print(f"Imagem salva em {OUTPUT}")

# Exemplo de uso
enhance_image(FILE1, OUTPUT)