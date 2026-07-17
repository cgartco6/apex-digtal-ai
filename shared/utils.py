import os

def save_output(studio: str, content: str, filename: str = "output.md"):
    os.makedirs(f"deliverables/{studio}", exist_ok=True)
    with open(f"deliverables/{studio}/{filename}", "w", encoding="utf-8") as f:
        f.write(str(content))
    print(f"Saved: deliverables/{studio}/{filename}")
