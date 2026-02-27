# PDF to Excel Converter - Pakistani Banks

A complete web application that converts Pakistani bank statement PDFs into structured Excel files.

## 🏦 Supported Banks

- ✅ **Habib Bank Limited (HBL)**
- ✅ **Bank AL Habib**
- ✅ **Meezan Bank**

## ✨ Features

- **Auto Bank Detection** - Automatically detects bank from PDF content
- **OCR Fallback** - Advanced OCR for image-based/scanned PDFs
- **Smart Number Extraction** - Extracts deposit slip numbers, branch codes, alphanumeric codes
- **Clean Excel Output** - Structured columns with proper formatting
- **Modern UI** - Bootstrap 5 responsive design
- **Secure File Handling** - File validation, secure naming, auto-cleanup

## 📁 Excel Output Format

### Meezan Bank
| Date | Particulars1 | Particulars2 | Particulars3 | Particulars4 | Credit | Debit | Bank |
|------|--------------|--------------|--------------|--------------|--------|-------|------|
| 2025-12-02 | 1042 | 13D | 2 | 4171966 | 2250000 | 0 | Meezan Bank |

### HBL / Bank AL Habib
| Date | Particulars1 | Particulars2 | Particulars3 | Particulars4 | Credit | Debit | Bank |
|------|--------------|--------------|--------------|--------------|--------|-------|------|
| 2025-12-01 | Online | Deposit | 25687849 | MUHAMMAD | 158000 | 0 | Habib Bank Limited |

## 🚀 Installation

### Prerequisites

1. **Python 3.10+**
2. **Tesseract OCR** - [Download](https://github.com/UB-Mannheim/tesseract/wiki)
3. **Poppler** - [Download](https://github.com/oschwartz10612/poppler-windows/releases)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
python app.py
```

Access: **http://127.0.0.1:5000**

## 🐳 Docker Deployment

```bash
# Build image
docker build -t pdf-excel-converter .

# Run container
docker run -p 5000:5000 pdf-excel-converter
```

## ☁️ Cloud Deployment

### Render.com (Recommended - Free)

1. Push code to GitHub
2. Go to [Render.com](https://render.com)
3. Create New Web Service
4. Connect GitHub repository
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn app:app`

### Railway.app

```bash
npm install -g @railway/cli
railway login
railway up
```

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main UI page |
| POST | `/convert` | Upload and convert PDF |
| GET | `/download/<filename>` | Download converted Excel |

## 📋 Project Structure

```
project/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── templates/
│   └── index.html        # Frontend UI (Bootstrap 5)
├── static/
│   └── style.css         # Custom styles
└── uploads/              # Temporary file storage
```

## 🔒 Security Features

- ✅ File type validation (PDF only)
- ✅ Secure filename generation
- ✅ File size limit (16MB max)
- ✅ Automatic file cleanup
- ✅ Non-root user in Docker

## 🛠️ Troubleshooting

### Tesseract Not Found
```bash
# Windows - Add to PATH
setx PATH "%PATH%;C:\Program Files\Tesseract-OCR"
```

### Poppler Not Found
```bash
# Windows - Add to PATH
setx PATH "%PATH%;C:\Program Files\poppler\Library\bin"
```

### Port Already in Use
```python
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=8080)
```

## 📝 License

MIT License

## 👨‍💻 Author

**Muhammad Saad Ahmed**

GitHub: [@Muhammad-Saad-Ahmed](https://github.com/Muhammad-Saad-Ahmed)

---

**Built with ❤️ for Pakistani Banking Community**
