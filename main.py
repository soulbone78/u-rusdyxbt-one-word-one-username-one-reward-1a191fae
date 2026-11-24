import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write("soulbone")


if __name__ == "__main__":
    main()
