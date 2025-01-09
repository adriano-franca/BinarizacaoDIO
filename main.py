from PIL import Image

def load_image(file_path):
    # Função para carregar uma imagem (JPEG) de um arquivo e convertê-la em um array 3D de pixels
    # utilizando a biblioteca Pillow para facilitar a leitura.
    img = Image.open(file_path)
    img = img.convert('RGB')  # Garante que a imagem esteja no formato RGB
    pixels = list(img.getdata())
    width, height = img.size
    return [pixels[i * width:(i + 1) * width] for i in range(height)]

def rgb_to_grayscale(image):
    # Converte uma imagem colorida (3 canais) para níveis de cinza (1 canal).
    height, width = len(image), len(image[0])
    grayscale_image = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            r, g, b = image[i][j]
            grayscale_pixel = int(0.3 * r + 0.59 * g + 0.11 * b)  # Fórmula de luminância
            grayscale_image[i][j] = grayscale_pixel

    return grayscale_image

def binarize_image(grayscale_image, threshold=128):
    # Converte uma imagem em tons de cinza para uma imagem binarizada (preto e branco).
    height, width = len(grayscale_image), len(grayscale_image[0])
    binary_image = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            binary_image[i][j] = 255 if grayscale_image[i][j] > threshold else 0

    return binary_image

def save_image(image, file_path):
    # Função para salvar uma imagem em um arquivo (formato básico PGM para simplicidade).
    height, width = len(image), len(image[0])
    with open(file_path, 'w') as f:
        f.write(f"P2\n{width} {height}\n255\n")
        for row in image:
            f.write(" ".join(map(str, row)) + "\n")

if __name__ == "__main__":
    # Caminho para a imagem de entrada e saída
    input_path = "./assets/image.jpeg"
    grayscale_output_path = "./assets/image_grayscale.pgm"
    binary_output_path = "./assets/image_binary.pgm"

    try:
        # Carrega a imagem
        print("Carregando a imagem...")
        image = load_image(input_path)

        # Converte para níveis de cinza
        print("Convertendo para níveis de cinza...")
        grayscale_image = rgb_to_grayscale(image)
        save_image(grayscale_image, grayscale_output_path)

        # Converte para binarizada
        print("Convertendo para imagem binarizada...")
        binary_image = binarize_image(grayscale_image)
        save_image(binary_image, binary_output_path)

        print("Processo concluído. Imagens salvas.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
