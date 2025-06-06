# 🚨 IntrusiShield:  Navigating Safely Through  Cyber Tides 
**IntrusiShield** is a hybrid cybersecurity framework integrating **Convolutional Neural Networks (CNNs)** with traditional rule-based logic to deliver an intelligent **Intrusion Detection System (IDS)** and **Intrusion Prevention System (IPS)**. This project is designed to detect and prevent malicious activity in real-time using file uploads or network traffic simulations.

📄 **Published Paper**:  
**IntrusiShield: Navigating Safely Through Cyber Tides**  
Published in: *IJARCCE, Vol. 13, Issue 6, June 2024*  
[🔗 IJARCCE Paper Link](https://ijarcce.com/wp-content/uploads/2024/07/IJARCCE.2024.13674.pdf)

---

## 🧠 Features

- ✅ CNN-based classification for intrusion detection.
- 🔍 Rule-based detection for known malicious patterns.
- 📈 Real-time or batch-mode threat analysis.
- 🌐 Flask web interface for file uploads and threat feedback.
- 🧾 Dashboard-ready results for visualization and analysis.
- 📁 Structured training and testing datasets.

---

## 🛠️ Tech Stack

- Python 3.8+
- Flask (for web app)
- TensorFlow / Keras (for CNN model)
- Pandas, NumPy
- Jupyter Notebook (for model development)

---

## 📂 Project Structure

```
.
├── data/
│   ├── test/
│   ├── test_224/
│   ├── train/
│   ├── train_224/
│   ├── Car_Hacking_5_.csv
│   └── Car_Hacking_5_.xlsx
├── flask_app/
│   ├── app.py             # Flask application for web interface
│   └── chatbot.py         # Optional: Chatbot for threat interaction
├── CNN based IDS(2023-2024).ipynb   # Jupyter Notebook for CNN modeling
├── IJARCCE Paper.pdf                # Published journal paper
├── LICENSE                          # Open-source license
├── Major Project Report.pdf         # Academic major project documentation
└── README.md                        # This file
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/intrusishield.git
cd intrusishield
```

### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install package_name
```

---

## ⚙️ Run the Flask App

```bash
cd flask_app
python app.py
```

Then open your browser at:  
[http://localhost:5000](http://localhost:5000)

You can upload files and get real-time intrusion feedback from the CNN model and rule-based system.

---

## 🧪 Model Training

Use the provided Jupyter notebook to train or fine-tune the CNN model:

```bash
jupyter notebook "CNN based IDS(2023-2024).ipynb"
```

- The notebook uses the dataset files in `/data/train_224` and `/data/test_224`.
- You can modify model layers, image resizing, epochs, etc.

---

## 📊 Results & Accuracy

- CNN model trained on car hacking dataset achieved **high training accuracy (98%) and prediction accuray (86%)** in classifying between benign and malicious signals.
- Combined model with rule-checking reduces false negatives.
- Detailed evaluation and confusion matrix provided in the paper.

---

## 📜 Research Publication

> **Citation**  
Jayakar A., et al., *IntrusiShield: Navigating Safely Through Cyber Tides*,  
IJARCCE, Vol. 13, Issue 6, June 2024, pp. 445–448.  
DOI: [10.17148/IJARCCE.2024.13674](https://doi.org/10.17148/IJARCCE.2024.13674)

---

## 🧾 License

This project is licensed under the MIT License – see the `LICENSE` file for details.

