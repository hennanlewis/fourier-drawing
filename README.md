# 🎨 Fourier Drawing

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-FFT-orange.svg)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Animation-green.svg)](https://matplotlib.org)

Reconstrução procedural de imagens SVG usando séries de Fourier e epiciclos.

O projeto:
- carrega um SVG
- converte o caminho em pontos
- calcula a Transformada de Fourier
- reconstrói o desenho usando vetores rotativos
- renderiza ou exporta a animação em vídeo

---

# ✨ Funcionalidades

- 🎨 Reconstrução procedural de SVGs
- 🌀 Sistema de epiciclos baseado em Fourier
- 🎥 Exportação MP4 com FFmpeg
- 📐 Resolução automática baseada na proporção
- 🖥️ Preview em tempo real com Matplotlib
- ⚡ Pipeline modular para animação e exportação
- 📦 Arquitetura desacoplada entre matemática, renderização e export

---

# 🏗️ Estrutura do Projeto

```bash
📁 fourier-drawing/
├── 📁 assets/                 # SVGs de entrada
│
├── 📁 core/
│   ├── 📁 animation/          # Runtime e renderização
│   │   ├── 📄 animator.py
│   │   ├── 📄 artists.py
│   │   ├── 📄 canvas.py
│   │   ├── 📄 config.py
│   │   └── 📄 trace.py
│   │
│   ├── 📁 math/               # Fourier e epiciclos
│   │   ├── 📄 epicycles.py
│   │   ├── 📄 fourier.py
│   │   └── 📄 models.py
│   │
│   └── 📁 svg/                # Carregamento e otimização SVG
│       ├── 📄 loader.py
│       └── 📄 optimizer.py
│
├── 📁 output/
│
├── 📄 .gitignore
├── 📄 .python-version
├── 📄 README.md
├── 📄 main.py
├── 📄 pyproject.toml
└── 📄 uv.lock
```

# ⚙️ Como Funciona

O SVG é convertido em uma sequência de pontos complexos.

A Transformada de Fourier é aplicada:

```math
X_k = \sum_{n=0}^{N-1} x_n e^{-i2\pi kn/N}
```

Cada coeficiente gera:

- frequência
- amplitude
- fase

Os vetores rotativos (epiciclos) são então utilizados para reconstruir o desenho ao longo do tempo.

---

#🛠️ Instalação
Pré-requisitos

- Python 3.13+
- uv
- FFmpeg

## Clone o projeto
```bash
git clone https://github.com/hennanlewis/fourier-drawing
cd fourier-drawing
```

## Instale as dependências
```bash
uv sync
```

---

🚀 Executando

Defina o SVG em main.py:

```python
INPUT_SVG = "assets/batman.svg"
```

Execute:

```bash
uv run main.py
```
---

# 📹 Exportando MP4

```python
animator.export_mp4(
    "output/video/render.mp4"
)
```

---

# ⚡ Configuração

Exemplo:

```python
NUM_SAMPLES = 2000
NUM_HARMONICS = 200
```

### NUM_SAMPLES
Quantidade de pontos amostrados do SVG.

- mais pontos → maior fidelidade
- mais processamento

---

### NUM_HARMONICS
Quantidade de componentes de Fourier utilizados.

- mais harmônicos → reconstrução mais precisa
- menos harmônicos → efeito mais simplificado

---

# 🧠 Tecnologias

- NumPy
- Matplotlib
- FFmpeg
- Python Dataclasses

---

# 🎯 Objetivos do Projeto

- estudo de séries de Fourier
- computação gráfica procedural
- renderização matemática
- animação baseada em vetores
- arquitetura modular em Python

---

# 📌 Roadmap

- [x] Reconstrução SVG via Fourier
- [x] Runtime encapsulado
- [x] Exportação MP4
- [x] Resolução dinâmica
- [ ] Exportação GIF
- [ ] Presets de renderização
- [ ] Multi-path SVG
- [ ] GPU rendering backend

---

# 🤝 Contribuindo

Contribuições são bem-vindas!

Sinta-se à vontade para:
- reportar bugs
- sugerir funcionalidades
- abrir pull requests
- melhorar performance e renderização
