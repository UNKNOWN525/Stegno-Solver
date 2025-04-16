# 🕵️‍♂️ Steganography Solver

A Python-based CLI tool that automates multiple steganography and metadata analysis techniques on image and binary files. It wraps tools like `steghide`, `zsteg`, `stegcracker`, `binwalk`, and `exiftool` into a single workflow.

---

## 📦 Features

- 🔍 Metadata extraction using `exiftool`
- 🧱 Archive/file carving using `binwalk`
- 🐍 Steg analysis on PNGs using `zsteg`
- 🔐 Password-based or brute-force extraction via `steghide` & `stegcracker`
- 📁 Organizes all outputs into a neat folder structure

---

## ✅ Requirements

Make sure these tools are installed:

| Tool              |
|-------------------|
| **steghide**      | 
| **zsteg**         | 
| **stegcracker**   | 
| **binwalk**       |
| **exiftool**      | 

---

## 🚀 Usage


python stego_solver.py <file> [-p PASSWORD] [-w WORDLIST]
