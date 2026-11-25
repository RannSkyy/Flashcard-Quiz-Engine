import random
import os

# ==========================
# DATA
# ==========================

quiz = [
    {
        "question": "Apa ibu kota Indonesia?",
        "options": ["A. Bandung", "B. Jakarta", "C. Surabaya", "D. Medan"],
        "answer": "B"
    },
    {
        "question": "2 + 8 = ?",
        "options": ["A. 8", "B. 9", "C. 10", "D. 12"],
        "answer": "C"
    },
    {
        "question": "Planet terbesar di tata surya?",
        "options": ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturnus"],
        "answer": "B"
    },
    {
        "question": "Bahasa pemrograman Python dibuat oleh?",
        "options": [
            "A. Guido van Rossum",
            "B. Bill Gates",
            "C. Elon Musk",
            "D. Steve Jobs"
        ],
        "answer": "A"
    },
    {
        "question": "HTML digunakan untuk?",
        "options": [
            "A. Mengolah gambar",
            "B. Membuat struktur website",
            "C. Membuat database",
            "D. Antivirus"
        ],
        "answer": "B"
    }
]

flashcards = [
    ("CPU", "Otak utama komputer."),
    ("RAM", "Penyimpanan sementara."),
    ("SSD", "Media penyimpanan yang cepat."),
    ("Python", "Bahasa pemrograman yang mudah dipelajari."),
    ("HTML", "Bahasa markup untuk website."),
    ("CSS", "Mengatur tampilan website."),
    ("Loop", "Perulangan dalam program."),
    ("Variable", "Tempat menyimpan data.")
]

# ==========================
# HIGHSCORE
# ==========================

FILE = "highscore.txt"

def get_highscore():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return int(f.read())
    return 0

def save_highscore(score):
    with open(FILE, "w") as f:
        f.write(str(score))

# ==========================
# QUIZ
# ==========================

def play_quiz():
    soal = quiz.copy()
    random.shuffle(soal)

    score = 0

    print("\n===== MODE KUIS =====")

    for nomor, q in enumerate(soal, start=1):
        print(f"\nSoal {nomor}")
        print(q["question"])

        for pilihan in q["options"]:
            print(pilihan)

        jawaban = input("Jawaban (A/B/C/D): ").upper()

        if jawaban == q["answer"]:
            print("Benar!")
            score += 20
        else:
            print(f"Salah! Jawaban benar: {q['answer']}")

    print("\n===================")
    print("Skor :", score)

    high = get_highscore()

    if score > high:
        print("🎉 Highscore Baru!")
        save_highscore(score)
    else:
        print("Highscore :", high)

# ==========================
# FLASHCARD
# ==========================

def flashcard():
    cards = flashcards.copy()
    random.shuffle(cards)

    benar = 0

    print("\n===== FLASHCARD =====")

    for depan, belakang in cards:
        print("\n----------------")
        print("Pertanyaan :")
        print(depan)

        input("\nTekan ENTER untuk melihat jawaban...")

        print("Jawaban :", belakang)

        tahu = input("Apakah kamu sudah hafal? (y/n): ").lower()

        if tahu == "y":
            benar += 1

    print("\nProgress Belajar")
    print(f"{benar}/{len(cards)} kartu telah dikuasai.")

# ==========================
# MENU
# ==========================

while True:
    print("\n==============================")
    print(" MESIN KUIS & KARTU FLASH")
    print("==============================")
    print("1. Mulai Kuis")
    print("2. Belajar Flashcard")
    print("3. Lihat Highscore")
    print("4. Keluar")

    pilih = input("Pilih menu : ")

    if pilih == "1":
        play_quiz()

    elif pilih == "2":
        flashcard()

    elif pilih == "3":
        print("\nHighscore :", get_highscore())

    elif pilih == "4":
        print("\nTerima kasih telah belajar!")
        break

    else:
        print("Menu tidak tersedia.")
