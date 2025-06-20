# 🛠️ Thiết lập môi trường phát triển

## 📖 Mục lục

1. [Cài đặt Anaconda (Khuyến nghị)](#1-cài-đặt-anaconda-khuyến-nghị)
2. [Cài đặt Python chính thức](#2-cài-đặt-python-chính-thức)
3. [Thiết lập VS Code](#3-thiết-lập-vs-code)
4. [Jupyter Notebook](#4-jupyter-notebook)
5. [Cài đặt Git](#5-cài-đặt-git)
6. [Kiểm tra môi trường](#6-kiểm-tra-môi-trường)

---

## 1. Cài đặt Anaconda (Khuyến nghị)

### 🐍 Tại sao chọn Anaconda?

- **Gói tất cả trong một**: Python + thư viện thiết yếu + trình quản lý gói
- **Môi trường Conda**: Quản lý môi trường dễ dàng
- **Thư viện được cài sẵn**: NumPy, Pandas, Matplotlib, Jupyter, v.v.
- **Đa nền tảng**: Hoạt động trên Windows, Mac, Linux
- **Thân thiện với người mới**: Giao diện GUI với Anaconda Navigator

### 📥 Download và Install

#### Windows:

1. Truy cập [anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
2. Download **Python 3.11** phiên bản cho Windows
3. Chạy installer (file .exe)
4. **Cài đặt quan trọng**:
   - ✅ Thêm Anaconda vào biến môi trường PATH
   - ✅ Đăng ký Anaconda làm Python mặc định
   - ✅ Cài đặt cho tất cả người dùng (nếu có quyền admin)

#### macOS:

1. Download **Python 3.11** phiên bản cho macOS
2. Chạy installer (file .pkg)
3. Làm theo hướng dẫn cài đặt
4. Restart terminal sau khi cài đặt

#### Linux (Ubuntu/Debian):

```bash
# Download installer
wget https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh

# Make executable
chmod +x Anaconda3-2023.03-Linux-x86_64.sh

# Run installer
./Anaconda3-2023.03-Linux-x86_64.sh

# Follow prompts, add to PATH when asked
# Restart terminal
source ~/.bashrc
```

### ✅ Xác minh cài đặt

```bash
# Kiểm tra phiên bản Python
python --version
# Kết quả: Python 3.11.x

# Kiểm tra conda
conda --version
# Kết quả: conda x.x.x

# Kiểm tra các gói có sẵn
conda list
```

---

## 2. Cài đặt Python chính thức

### 📥 Download từ Python.org

Nếu bạn muốn lightweight installation:

1. Truy cập [python.org/downloads](https://www.python.org/downloads/)
2. Download **Python 3.11+** cho OS của bạn
3. Run installer với options:
   - ✅ Add Python to PATH
   - ✅ pip installation
   - ✅ py launcher (Windows)

### 📦 Install Essential Packages

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install essential data science packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Install development tools
pip install black flake8 pytest
```

### 🐍 Virtual Environment Setup

```bash
# Create virtual environment
python -m venv python_course_env

# Activate environment
# Windows:
python_course_env\Scripts\activate
# Mac/Linux:
source python_course_env/bin/activate

# Install packages in virtual environment
pip install -r requirements.txt
```

---

## 3. VS Code Setup

### 📥 Download và Install

1. Truy cập [code.visualstudio.com](https://code.visualstudio.com/)
2. Download for your OS
3. Install với default settings

### 🔧 Essential Extensions

#### Python Extension Pack

```
Tên: Python
Publisher: Microsoft
ID: ms-python.python
```

**Tính năng bao gồm**:

- IntelliSense (tự động hoàn thành code)
- Hỗ trợ debugging
- Định dạng code
- Tích hợp Jupyter

#### Các Extension bổ sung hữu ích

```
# Định dạng code
Name: Prettier - Code formatter
ID: esbenp.prettier-vscode

# Tích hợp Git
Name: GitLens
ID: eamodio.gitlens

# Tô màu ngoặc
Name: Bracket Pair Colorizer 2
ID: coenraads.bracket-pair-colorizer-2

# Icon file
Name: Material Icon Theme
ID: pkief.material-icon-theme
```

### ⚙️ Cấu hình VS Code

#### Thiết lập Python Interpreter:

1. Open Command Palette (`Ctrl+Shift+P`)
2. Type \"Python: Select Interpreter\"
3. Choose your Python installation:
   - Anaconda: `~/anaconda3/bin/python`
   - Official: Your Python installation path

#### Settings.json Configuration:

```json
{
    \"python.defaultInterpreterPath\": \"/path/to/python\",
    \"python.formatting.provider\": \"black\",
    \"python.linting.enabled\": true,
    \"python.linting.pylintEnabled\": true,
    \"editor.formatOnSave\": true,
    \"editor.codeActionsOnSave\": {
        \"source.organizeImports\": true
    }
}
```

---

## 4. Jupyter Notebook

### 🚀 Launch Jupyter

```bash
# Phương pháp 1: Từ terminal
jupyter notebook

# Phương pháp 2: Từ Anaconda Navigator
# Mở Anaconda Navigator → Khởi chạy Jupyter Notebook

# Phương pháp 3: JupyterLab (giao diện hiện đại)
jupyter lab
```

### 🔧 Cấu hình Jupyter

#### Tạo file config:

```bash
jupyter notebook --generate-config
```

#### Các extension hữu ích:

```bash
# Install nbextensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Enable useful extensions
jupyter nbextension enable varInspector/main
jupyter nbextension enable toc2/main
jupyter nbextension enable code_folding/main
```

### 📝 First Jupyter Test

```python
# Create new notebook and test
print(\"Hello, Jupyter!\")

# Check Python version
import sys
print(f\"Python version: {sys.version}\")

# Test data science libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(\"All libraries loaded successfully!\")
```

---

## 5. Git Installation

### 📥 Install Git

#### Windows:

1. Download from [git-scm.com](https://git-scm.com/)
2. Run installer with default settings
3. Choose \"Git from command line and 3rd party software\"

#### macOS:

```bash
# Phương pháp 1: Homebrew (khuyến nghị)
brew install git

# Phương pháp 2: Xcode Command Line Tools
xcode-select --install
```

#### Linux:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install git

# CentOS/RHEL
sudo yum install git
```

### ⚙️ Git Configuration

```bash
# Set your identity
git config --global user.name \"Your Name\"
git config --global user.email \"your.email@example.com\"

# Set default editor
git config --global core.editor \"code --wait\"

# Verify configuration
git config --list
```

---

## 6. Environment Verification

### 🧪 Complete System Test

Tạo file `environment_test.py`:

```python
#!/usr/bin/env python3
\"\"\"
Environment Test Script
Kiểm tra tất cả components đã cài đặt đúng chưa
\"\"\"

import sys
import subprocess

def check_python():
    \"\"\"Check Python version\"\"\"
    print(f\"✅ Python version: {sys.version}\")
    return sys.version_info >= (3, 8)

def check_package(package_name):
    \"\"\"Check if package is installed\"\"\"
    try:
        __import__(package_name)
        print(f\"✅ {package_name} installed\")
        return True
    except ImportError:
        print(f\"❌ {package_name} NOT installed\")
        return False

def check_command(command):
    \"\"\"Check if command is available\"\"\"
    try:
        result = subprocess.run([command, '--version'],
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f\"✅ {command} available: {result.stdout.strip().split()[0]}\")
            return True
    except FileNotFoundError:
        print(f\"❌ {command} NOT available\")
        return False

def main():
    print(\"=== PYTHON ENVIRONMENT TEST ===\")

    # Check Python
    python_ok = check_python()

    # Check essential packages
    packages = ['numpy', 'pandas', 'matplotlib', 'jupyter']
    packages_ok = all(check_package(pkg) for pkg in packages)

    # Check external tools
    commands = ['git', 'conda']  # conda might not be available with pip install
    commands_ok = any(check_command(cmd) for cmd in commands)

    print(\"\\n=== SUMMARY ===\")
    if python_ok and packages_ok:
        print(\"🎉 Environment setup is COMPLETE!\")
        print(\"You're ready to start the Python course!\")
    else:
        print(\"⚠️  Environment setup is INCOMPLETE\")
        print(\"Please check the failed items above\")

if __name__ == \"__main__\":
    main()
```

### 🏃 Run Test

```bash
python environment_test.py
```

**Kết quả mong đợi:**

```
=== PYTHON ENVIRONMENT TEST ===
✅ Python version: 3.11.x
✅ numpy installed
✅ pandas installed
✅ matplotlib installed
✅ jupyter installed
✅ git available: git version 2.x.x
✅ conda available: conda 23.x.x

=== SUMMARY ===
🎉 Environment setup is COMPLETE!
You're ready to start the Python course!
```

---

## 🆘 Troubleshooting Common Issues

### Issue 1: Python không được nhận diện

```bash
# Windows: Check PATH environment variable
echo $PATH

# Add Python to PATH manually
# Control Panel → System → Advanced → Environment Variables
```

### Issue 2: pip không hoạt động

```bash
# Reinstall pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### Issue 3: Jupyter không khởi động

```bash
# Check if installed
pip show jupyter

# Reinstall if needed
pip uninstall jupyter
pip install jupyter
```

### Issue 4: VS Code không tìm thấy Python

1. Open Command Palette (`Ctrl+Shift+P`)
2. \"Python: Select Interpreter\"
3. Manually browse to Python executable

---

## 📋 Post-Installation Checklist

- [ ] Python 3.8+ installed and accessible from command line
- [ ] pip working and up to date
- [ ] Essential packages installed (numpy, pandas, matplotlib, jupyter)
- [ ] VS Code installed with Python extension
- [ ] Jupyter Notebook launches successfully
- [ ] Git installed and configured
- [ ] Environment test script passes
- [ ] Create first \"Hello World\" program successfully

---

**Next**: Continue to `03_first_python_program.md`
