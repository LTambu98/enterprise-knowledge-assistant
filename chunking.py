from pathlib import Path


def chunk_markdown(file_path):
    """Spezza un file Markdown in chunk, uno per ogni sezione '## Titolo'."""
    path = Path(file_path)
    text = path.read_text(encoding="utf-8")

    chunks = []
    current_title = None
    current_lines = []

    for line in text.splitlines():
        if line.startswith("## "):
            # chiudo la sezione precedente, se esiste
            if current_title is not None:
                chunks.append(make_chunk(path.name, current_title, current_lines))
            current_title = line[3:].strip()
            current_lines = []
        elif line.startswith("# "):
            continue  # titolo generale del documento, lo saltiamo
        else:
            current_lines.append(line)

    # chiudo l'ultima sezione
    if current_title is not None:
        chunks.append(make_chunk(path.name, current_title, current_lines))

    return chunks


def make_chunk(source, title, lines):
    body = "\n".join(lines).strip()
    return {
        "source": source,
        "section": title,
        "text": f"{title}\n{body}",
    }


if __name__ == "__main__":
    for file in Path("documenti").glob("*.md"):
        for chunk in chunk_markdown(file):
            print(f"[{chunk['source']} | {chunk['section']}]")
            print(chunk["text"])
            print("-" * 40)