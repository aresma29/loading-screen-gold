from pathlib import Path


def main():
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    print(entry_path.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
