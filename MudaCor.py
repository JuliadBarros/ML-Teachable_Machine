import cv2
import numpy as np
from keras.models import load_model  # TensorFlow is required for Keras to work

# Carregar o modelo pré-treinado
model = load_model("Modelos_cor/keras_Model.h5", compile=False)

# Carregar os nomes das classes
class_names = [line.strip() for line in open("Modelos_cor/labels.txt", "r").readlines()]

# Criar um array para armazenar os dados da imagem
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Inicializar a câmera
cap = cv2.VideoCapture(0)


# Função para processar a imagem
def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # Ajuste para o tamanho do modelo
    image = image / 255.0  # Normalização
    return np.expand_dims(image, axis=0)


# Função para extrair o nome da classe (ignorando o número)
def get_class_name(predicted_class):
    return predicted_class.split(' ', 1)[1].strip()  # Divide a string e pega o segundo valor (nome da classe)


# Loop de captura de vídeo
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Processar a imagem
    processed_image = preprocess_image(frame)

    # Fazer a predição
    predictions = model.predict(processed_image)
    predicted_class = class_names[np.argmax(predictions)].strip()  # Remover qualquer '\n'

    # Extrair apenas o nome da classe
    class_name = get_class_name(predicted_class)

    # Definir a cor de fundo e o texto com base no gesto
    if class_name == 'Like':
        color = (0, 255, 0)  # Verde
        text = "Positivo"
    elif class_name == 'Dislike':
        color = (0, 0, 255)  # Vermelho
        text = "Negativo"
    else:
        color = (255, 255, 255)  # Branco
        text = "Neutro"

    # Mudar a cor de fundo
    background = np.full((480, 640, 3), color, dtype=np.uint8)

    # Calcular a posição do texto para centralização
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = (background.shape[1] - text_width) // 2
    text_y = (background.shape[0] + text_height) // 2

    # Adicionar o texto ao fundo
    cv2.putText(background, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

    # Exibir a cor de fundo com texto
    cv2.imshow('Cor de Fundo', background)

    # Mostrar a imagem da câmera
    cv2.imshow('Gestos', frame)

    # Saindo com 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a câmera e fechar as janelas
cap.release()
cv2.destroyAllWindows()
