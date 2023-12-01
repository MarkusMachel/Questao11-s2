import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('ave.jpg')  # Substitua pelo caminho da sua imagem

# Definir a cor amarela
yellow_color = np.array([255, 255, 0])

# Calcular a distância euclidiana para cada pixel na imagem
distances = np.sqrt(np.sum((image - yellow_color) ** 2, axis=2))

# Definir a distância de limiar
threshold_distance = np.sqrt(np.sum((np.array([0, 0, 0]) - np.array([100, 100, 100])) ** 2))


# Criar uma máscara com base na distância de limiar
mask = distances < threshold_distance

# Calcular a média dos valores de distância dentro da região de limiar
average_distance = np.mean(distances[mask])

print(f'A média dos valores de distância dentro da região de limiar é aproximadamente: {average_distance}')
