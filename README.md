# PXE ANUVAD

**Offline Multilingual Document Translation System**

PXE ANUVAD is an offline document translation system developed during the **DRDO PXE Internship Project**. It translates PDF documents and images into multiple Indian languages while preserving the original document layout as much as possible.

---

## Features

- Offline document translation
- Automatic source language detection
- Support for multiple Indian languages
- OCR support for scanned PDFs and images
- Layout-preserving PDF generation
- Drag & Drop document upload
- Professional Flask-based web interface
- Download translated PDF
- Works completely offline after model installation

---

## Supported Input Formats

- PDF
- PNG
- JPG
- JPEG

---

## Supported Languages

- English
- Hindi
- Odia
- Bengali
- Assamese
- Bodo
- Dogri
- Gujarati
- Kannada
- Kashmiri
- Konkani
- Maithili
- Malayalam
- Manipuri
- Marathi
- Nepali
- Punjabi
- Sanskrit
- Santali
- Sindhi
- Tamil
- Telugu
- Urdu

---

## Technologies Used

### Backend
- Python
- Flask

### OCR
- EasyOCR

### Translation
- Meta NLLB-200

### PDF Processing
- PyMuPDF

### Image Processing
- OpenCV
- Pillow

### Frontend
- HTML
- CSS
- JavaScript

---

# Project Structure

```
PXE-ANUVAD/
│
├── backend/
│   ├── app.py
│   ├── translator.py
│   ├── pipeline.py
│   ├── pdf_reader.py
│   ├── ocr.py
│   ├── layout_writer.py
│   ├── layout_cleaner.py
│   ├── layout_preserving_pdf.py
│   ├── language_detector.py
│   ├── file_handler.py
│   ├── text_preprocessor.py
│   └── config.py
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
│
├── fonts/
│
├── models/
│
├── input/
│
├── output/
│
├── requirements.txt
│
└── README.md
```

---

# Installation

## Step 1

Clone or download the project.

```
git clone <repository_url>
```

or download the ZIP file.

---

## Step 2

Create a virtual environment (Recommended)

Windows

```
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3

Install dependencies

```
pip install -r requirements.txt
```

---

## Step 4

Download the translation model.

Place the downloaded model inside:

```
models/
```

---

## Step 5

Place the font

```
fonts/
```

Example:

```
NotoSansDevanagari-Regular.ttf
```

---

## Step 6

Run the application

```
python backend/app.py
```

---

## Step 7

Open your browser

```
http://127.0.0.1:5000
```

---

# Usage

1. Open PXE ANUVAD.

2. Drag & Drop or browse a document.

3. Select the target language.

4. Click **Translate Document**.

5. Wait for translation.

6. Download the translated PDF.

---

# Requirements

Python 3.10 or above

Install all required packages using:

```
pip install -r requirements.txt
```

---

# Notes

- Internet is required only for downloading the translation model for the first time.
- After the model has been downloaded, the application works completely offline.
- Large PDF files may require additional processing time.

---

# Screenshots

Add screenshots here.

Example:

- Home Page
- Upload Page
- Translation Progress
- Result Page
- Download Page

---

# Future Improvements

- Real-time translation progress
- Better table preservation
- Improved OCR accuracy
- Additional language support
- Batch document translation
- Export to DOCX

---

# Developed By

Team PXE ANUVAD

---
