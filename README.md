# NSForest CLI

A command-line bioinformatics tool scaffolded using [template-python](https://github.com/NIH-NLM/template-python).

---

## 🛠 Features

- Python 3.11
- Typer-powered CLI
- Conda + Docker compatible
- CI with GitHub Actions
- Auto-generated Sphinx docs

---

## 🚀 Getting Started

Install via Conda or use Docker:

```bash
conda env create -f environment.yml
conda activate nsforest
# OR
docker build -t nsforest .
docker run -it nsforest
```

---

## 💡 CLI Usage

```bash
nsforest --help
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 📄 License

MIT License © NIH/NLM

