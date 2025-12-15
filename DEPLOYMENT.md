# Deployment Guide 🚀

## Option 1: Streamlit Cloud (Easiest)
Streamlit Cloud is free for public repositories and handles everything for you.

1.  Push your code to GitHub.
2.  Go to [share.streamlit.io](https://share.streamlit.io/).
3.  Click **"New app"**.
4.  Select your repository, branch, and main file path:
    *   **Repository**: `your-username/math-adaptive-prototype`
    *   **Branch**: `main`
    *   **Main file path**: `src/main.py`
5.  Click **"Deploy!"**.

## Option 2: Docker (Flexible)
You can containerize this application to run it anywhere (AWS, Azure, Google Cloud, or locally).

### 1. Build the Image
Run this command in the project root:
```bash
docker build -t math-adventure .
```

### 2. Run the Container
```bash
docker run -p 8501:8501 math-adventure
```
Your app will be available at `http://localhost:8501`.

## Option 3: Manual / VPS
If you have a server with Python installed:

1.  Install dependencies: `pip install -r requirements.txt`
2.  Run as a background process:
    ```bash
    nohup streamlit run src/main.py --server.port 80 &
    ```
