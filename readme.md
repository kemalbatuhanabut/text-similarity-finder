# Text Similarity Finder 📝🔍

**Text Similarity Finder** is an advanced Python CLI tool to automatically **detect near-duplicate or similar text files** in a folder. Using **TF-IDF Vectorization** and **Cosine Similarity**, it compares text content and helps you clean, audit, or optimize large text collections efficiently.

Built with **powerful NLP techniques**, this tool is ideal for **plagiarism detection**, **SEO audits**, **document de-duplication**, and more.

---

## ⚡ Why Use This Tool?

- **Save hours of manual checking** — automate file similarity detection.
- Find **redundant, duplicated, or slightly modified text files**.
- Perfect for:
  - Researchers
  - Content creators
  - Writers & publishers
  - SEO professionals
  - Developers managing documentation
- Showcases **advanced Python programming with real NLP algorithms**.

---

## 🚀 Features

✅ **TF-IDF Vectorization** for intelligent text feature extraction  
✅ **Cosine Similarity** to compute meaningful document similarity  
✅ Adjustable **similarity threshold** (default `0.80`)  
✅ Supports `.txt` and `.md` files  
✅ Clean CLI interface  
✅ Works fast even with dozens or hundreds of documents

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/kemalbatuhanabut/text-similarity-finder.git
cd text-similarity-finder
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install scikit-learn numpy
```

---

## 🖥️ Usage

```bash
python find_duplicates.py [folder] --threshold [value]
```

### Arguments:

| Argument      | Description                                               | Example            |
| ------------- | --------------------------------------------------------- | ------------------ |
| `folder`      | Folder containing `.txt` or `.md` files                   | `./documents`      |
| `--threshold` | Similarity threshold (between 0.0 and 1.0, default `0.8`) | `--threshold 0.75` |

---

## 📌 Examples

* **Find files that are at least 80% similar:**

```bash
python find_duplicates.py ./texts --threshold 0.8
```

* **Find files that are at least 60% similar:**

```bash
python find_duplicates.py ./texts --threshold 0.6
```

---

## 🧠 How It Works

1. **Reads** all `.txt` and `.md` files in the folder.
2. **Vectorizes** them using **TF-IDF (Term Frequency-Inverse Document Frequency)**.
3. **Calculates pairwise Cosine Similarities** between documents.
4. **Prints pairs** of files with similarity **above the specified threshold**.

---

## 📚 Example Output:

```
Similar file pairs (above threshold):

article1.txt <--> article2.txt | Similarity: 0.924
post_about_ai.md <--> post_about_machine_learning.md | Similarity: 0.813
```

---

## 🔄 Future Roadmap

* [ ] Optional **MinHash/LSH** for ultra-large datasets
* [ ] Output similarity **matrix file** for visualization
* [ ] Ignore boilerplate text via custom stopword lists

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Fork the repo, make your changes, and open a PR.

---

## 📜 License

MIT License — Free to use, modify, distribute.

---

## 👨‍💻 Author

**Kemal Batuhan Abut**
GitHub → [@kemalbatuhanabut](https://github.com/kemalbatuhanabut)

---

✨ **Automate the boring. Focus on what matters.**
**Text Similarity Finder** helps you keep your content **clean, efficient, and optimized**.
