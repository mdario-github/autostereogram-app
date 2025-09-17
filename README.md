# 🎨 Autostereogram Generator

Turn any image into a **3D autostereogram** (a "Magic Eye" picture) using MiDaS depth estimation and a custom stereogram algorithm.

---

## 🚀 Features

- Upload an image (`.jpg`, `.png`, `.jpeg`)
- Generate a **depth map** using [MiDaS](https://github.com/isl-org/MiDaS) (monocular depth estimation)
- Convert the depth map into a **random-dot autostereogram**
- View the results directly in your browser
- Download the generated autostereogram as a `.png`

---

## 📦 Installation

Clone this repo:

```bash
git clone https://github.com/yourusername/autostereogram-app.git
cd autostereogram-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run locally

Start the Streamlit app:

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deployment

You can deploy this app for free on:

* [Streamlit Cloud](https://streamlit.io/cloud)
* [HuggingFace Spaces](https://huggingface.co/spaces)

Both support Python out of the box.
Just connect your GitHub repo and deploy 🚀

---

## 📂 Project structure

```
autostereogram-app/
│── app.py                 # Streamlit app entry point
│── requirements.txt       # Dependencies
│── src/
│    ├── depthmap.py       # MiDaS-based depth map generation
│    ├── stereogram.py     # Autostereogram generator
│── assets/examples/       # Example images
│── README.md              # Documentation
```

---

## 🧠 How it works

1. **Depth map estimation**:
   MiDaS predicts relative depth from a single 2D image.
   White = closer, Black = farther.

2. **Autostereogram generation**:
   Each pixel is shifted horizontally based on depth.
   Your brain fuses the repeated patterns to reveal a hidden 3D shape.

---

## 📜 License

MIT License – Free to use, modify, and share.
