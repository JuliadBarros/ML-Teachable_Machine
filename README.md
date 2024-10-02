# Integrando Modelo de IA 🤖 em um código Python.
<div align="justify">
Para o treinamento do modelo, foi utilizado o site [Teachable Machine](https://teachablemachine.withgoogle.com/), lá foram criadas três classes: as de "Like" e "Dislike", sendo essas representadas por gestos com a mão, e uma classe padrão chamada "Background", que é ativada quando nenhum gesto é detectado.

O objetivo do código é identificar cada gesto usando o modelo de IA treinado e retornar uma ação correspondente a cada classe. Cada ação é responsável por modificar a aparência da tela, sendo elas:
- Para "Like" o fundo verde com um texto escrito "Positivo";
- Para "Dislike" o fundo vermelho com o texto escrito "Negativo";
- Quando não detectar nenhum gesto, o padrão é o "Background" que deixa o fundo branco com o texto escrito "Neutro".
</div>

## 🛠 Bibliotecas utilizadas:
- OpenCV.
- Tensorflow.
- NumPy.

## :pencil2: Autores 
- [@JuliadBarros](https://github.com/JuliadBarros)
  
