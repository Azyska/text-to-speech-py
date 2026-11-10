import os
import sys
from gtts import gTTS

def konversi_teks_ke_audio(path_teks, nama_file_audio, bahasa="id", lambat=False):
    # 1. Validasi keberadaan file sumber
    if not os.path.exists(path_teks):
        print(f"[ERROR] File teks tidak ditemukan di: {path_teks}")
        return False

    # 2. Baca isi file teks
    try:
        with open(path_teks, "r", encoding="utf-8") as file:
            konten = file.read().strip()
    except Exception as e:
        print(f"[ERROR] Gagal membaca file: {e}")
        return False

    if not konten:
        print("[PERINGATAN] File teks kosong, tidak ada audio yang dibuat.")
        return False

    # 3. Pastikan folder output tersedia
    folder_output = "output"
    os.makedirs(folder_output, exist_ok=True)
    path_output = os.path.join(folder_output, f"{nama_file_audio}.mp3")

    # 4. Proses konversi Text-to-Speech via gTTS
    print("\nSedang mengonversi teks ke audio...")
    try:
        tts = gTTS(text=konten, lang=bahasa, slow=lambat)
        tts.save(path_output)
        print(f"[SUKSES] Audio berhasil disimpan!")
        print(f"Lokasi file: {path_output}")
        return True
    except Exception as e:
        print(f"[ERROR] Gagal mengonversi ke suara: {e}")
        return False

def main():
    print("=" * 45)
    print("      PYTHON TEXT-TO-SPEECH GENERATOR      ")
    print("=" * 45)

    # Input file sumber
    file_default = "data/contoh.txt"
    path_input = input(f"Masukkan path file teks (default: {file_default}): ").strip()
    if not path_input:
        path_input = file_default

    # Input nama file output
    nama_output = input("Masukkan nama file audio (tanpa .mp3): ").strip()
    if not nama_output:
        nama_output = "hasil_audio"

    # Pilihan bahasa
    print("\nPilihan bahasa:")
    print("1. Bahasa Indonesia (id)")
    print("2. Bahasa Inggris (en)")
    pilihan_bahasa = input("Pilih bahasa (1/2, default 1): ").strip()
    kode_bahasa = "en" if pilihan_bahasa == "2" else "id"

    # Jalankan fungsi
    konversi_teks_ke_audio(path_input, nama_output, bahasa=kode_bahasa)

if __name__ == "__main__":
    main()