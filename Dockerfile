# Base image đã cài Chrome rồi
FROM mcr.microsoft.com/windows/servercore:ltsc2022


# Dùng PowerShell làm shell mặc định
SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop';"]

COPY chrome_installer.exe C:\\chrome_installer.exe

# Cài Chrome im lặng
RUN Start-Process -Wait -FilePath 'C:\\chrome_installer.exe' -ArgumentList '/silent', '/install'; \
    Remove-Item 'C:\\chrome_installer.exe'

# Tải Python installer (bản chính thức từ python.org)
# Cài Python
ENV PYTHON_VERSION=3.11.5
ENV PYTHON_DIR="C:\\Python311"

RUN Invoke-WebRequest -Uri "https://www.python.org/ftp/python/$env:PYTHON_VERSION/python-$env:PYTHON_VERSION-amd64.exe" -OutFile "python-installer.exe"; \
    Start-Process -Wait -FilePath "python-installer.exe" -ArgumentList '/quiet', "InstallAllUsers=1", "PrependPath=1", "TargetDir=$env:PYTHON_DIR"; \
    Remove-Item "python-installer.exe"; \
    & "$env:PYTHON_DIR\\python.exe" --version

# Cài pip packages
RUN & "$env:PYTHON_DIR\\python.exe" -m pip install --upgrade pip; \
    & "$env:PYTHON_DIR\\python.exe" -m pip install pyautogui requests opencv-python pygetwindow pillow


# === TẠO THƯ MỤC APP VÀ CHÉP FILE MAIN.PY ===
WORKDIR C:/app
COPY main.py .

# === CHẠY CHƯƠNG TRÌNH ===
CMD ["python", "main.py"]
