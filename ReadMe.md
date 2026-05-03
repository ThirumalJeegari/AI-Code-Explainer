# 🧠 AI Code Explainer Tool

An AI-powered web application that explains programming code in simple, human-friendly language. Built using **Python, Streamlit, and Groq API**.

---

## 🚀 Features

* 💻 Paste code and get instant explanation
* 🌐 Supports multiple languages (Python, Java, JavaScript, C++, etc.)
* 🧑‍🎓 Beginner Mode (simple explanation)
* 🧑‍💻 Advanced Mode (technical explanation)
* 📌 Step-by-step breakdown of code
* 🐞 Bug detection & improvement suggestions

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Groq API (LLaMA 3.3)**
* **python-dotenv**

---

## 📁 Project Structure

```
ai-code-explainer/
│── app.py
│── llm_helper.py
│── .env
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/ThirumalJeegari/AI-Content-Generator.git
cd AI-Content-Generator
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Add your API key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ **Important:** Never share your API key publicly.

---

### 4️⃣ Run the app

```
streamlit run app.py
```

---

## 🧪 Example

Paste this code:

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

👉 The app will generate:

* Simple explanation (Beginner mode)
* Technical breakdown (Advanced mode)
* Suggestions for improvement

---

## 💡 Future Improvements

* 📂 Upload code files (.py, .java, .js)
* 📄 Export explanation as PDF
* 🎨 Better UI/UX design
* 🧠 Code debugging assistant
* 🌙 Dark mode

---

## 🔒 Security Note

* Do NOT commit `.env` file to GitHub
* Add `.env` to `.gitignore`
* Regenerate API key if exposed

---

## 🙌 Use Cases

* Students learning programming
* Beginners understanding code logic
* Developers reviewing unfamiliar code

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Thirumal Jeegari**
B.Tech Student | Aspiring Java Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
