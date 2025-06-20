# 🛠️ Development Environment Setup

## 📖 Mục lục

1. [Anaconda Installation (Khuyến nghị)](#1-anaconda-installation)
2. [Python Official Installation](#2-python-official-installation)
3. [VS Code Setup](#3-vs-code-setup)
4. [Jupyter Notebook](#4-jupyter-notebook)
5. [Git Installation](#5-git-installation)
6. [Environment Verification](#6-environment-verification)

---

## 1. Anaconda Installation (Khuyến nghị)

### 🐍 Tại sao chọn Anaconda?

- **All-in-one package**: Python + essential libraries + package manager
- **Conda environment**: Quản lý môi trường dễ dàng
- **Pre-installed libraries**: NumPy, Pandas, Matplotlib, Jupyter, v.v.
- **Cross-platform**: Hoạt động trên Windows, Mac, Linux
- **Beginner-friendly**: GUI interface với Anaconda Navigator

### 📥 Download và Install

#### Windows:

1. Truy cập [anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
2. Download **Python 3.11** version for Windows
3. Chạy installer (.exe file)
4. **Important settings**:
   - ✅ Add Anaconda to PATH environment variable
   - ✅ Register Anaconda as default Python
   - ✅ Install for all users (nếu có admin rights)

#### macOS:

1. Download **Python 3.11** version for macOS
2. Chạy installer (.pkg file)
3. Follow installation wizard
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

### ✅ Verify Installation

```bash
# Check Python version
python --version
# Should output: Python 3.11.x

# Check conda
conda --version
# Should output: conda x.x.x

# Check available packages
conda list
```

---

## 2. Python Official Installation

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

**Features include**:

- IntelliSense (code completion)
- Debugging support
- Code formatting
- Jupyter integration

#### Useful Additional Extensions

```
# Code formatting
Name: Prettier - Code formatter
ID: esbenp.prettier-vscode

# Git integration
Name: GitLens
ID: eamodio.gitlens

# Bracket colorization
Name: Bracket Pair Colorizer 2
ID: coenraads.bracket-pair-colorizer-2

# File icons
Name: Material Icon Theme
ID: pkief.material-icon-theme
```

### ⚙️ VS Code Configuration

#### Python Interpreter Setup:

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
# Method 1: From terminal
jupyter notebook

# Method 2: From Anaconda Navigator
# Open Anaconda Navigator → Launch Jupyter Notebook

# Method 3: JupyterLab (modern interface)
jupyter lab
```

### 🔧 Jupyter Configuration

#### Create config file:

```bash
jupyter notebook --generate-config
```

#### Useful extensions:

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
# Method 1: Homebrew (recommended)
brew install git

# Method 2: Xcode Command Line Tools
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

**Expected Output:**

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
