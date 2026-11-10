cat << 'EOF' > README.md
<div align="center">

# 🎙️ Python Text-to-Speech & Audio Generator

A simple, modular Python tool to transform plain text files into clean `.mp3` audio files using Google Text-to-Speech (gTTS).

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-blue?style=flat-square)](#)

</div>

---

## 📌 Problem & Motivation

Membaca teks artikel panjang, dokumen catatan, atau cerita pendek secara terus-menerus di depan layar dapat menyebabkan kelelahan mata (*screen fatigue*). Mengubah teks menjadi format audio memungkinkan konsumsi konten secara lebih fleksibel melalui format audio/audiobook mini.

Proyek ini dibuat secara independen untuk:
- Mengotomatiskan konversi teks lokal (`.txt`) menjadi berkas audio portabel (`.mp3`).
- Menyediakan antarmuka CLI (*Command Line Interface*) yang interaktif dan mudah dioperasikan.
- Mempelajari penanganan berkas teks berbasis encoding `utf-8`, manajemen alur kerja I/O di Linux, serta integrasi pustaka sintesis suara pihak ketiga (`gTTS`).

---

## ✨ Features

- **Multi-language Support:** Mendukung pelafalan dalam Bahasa Indonesia (`id`) dan Bahasa Inggris (`en`).
- **File Validation & Safety:** Memeriksa keberadaan file dan mencegah proses berjalan jika file sumber kosong.
- **Auto Directory Management:** Otomatis membuat folder tujuan (`output/`) jika belum tersedia.
- **UTF-8 Support:** Mampu membaca karakter teks dengan format encoding standar secara tepat.

---

## 🏗️ Directory Architecture

```text
text-to-speech-py/
├── data/
│   └── contoh.txt       # File teks sampel untuk pengujian
├── output/              # Tempat penyimpanan berkas audio hasil konversi (.mp3)
├── .gitignore           # File pengabaian Git (cache, virtualenv, dan output mp3)
├── main.py              # Logika utama aplikasi CLI
├── README.md            # Dokumentasi proyek
└── requirements.txt     # Daftar pustaka eksternal (gTTS)