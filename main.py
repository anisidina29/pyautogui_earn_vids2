import subprocess
import time
import random
import requests
import os

# Delay import pyautogui sau khi GUI đã sẵn sàng
time.sleep(2)
import pyautogui
pyautogui.FAILSAFE = False
import pygetwindow as gw

KEEP_KEYWORDS = ["watch", "chatgpt", "record"]

def get_chrome_windows():
    return [w for w in gw.getWindowsWithTitle('Chrome') if w.visible and w.title.strip() != ""]

# 1. Mở Chrome với link và kích thước cố định
old_url = "https://raw.githubusercontent.com/anisidina29/anisidina29-selenium_earnvids_docker/refs/heads/main/earnvids.txt"
response_old = requests.get(old_url)
response_old.raise_for_status()
links = response_old.text.strip().splitlines()

# Chọn 1 link ngẫu nhiên
url = random.choice(links)
print(f"Da chon link: {url}")
print("Dang mo Chrome...")
subprocess.Popen(["start", "chrome", "--new-window", url, "--window-size=1280,720"], shell=True)

# 2. Chờ trình duyệt mở và tab chính load
time.sleep(6)

# 3. Click nút Play hoặc giữa màn hình
for i in range(11):
    print(f"\nLap lan {i+1}/10")
    try:
        location = False
        if location:
            center = pyautogui.center(location)
            pyautogui.moveTo(center.x, center.y, duration=0.3)
            pyautogui.click()
            print("Da click nut Play!")
        else:
            raise Exception("Khong tim thay anh")
    except Exception as e:
        print("Khong tim thay play.png, se click giua man hinh.")

        screen_width, screen_height = pyautogui.size()
        rand_x = screen_width // 2 + random.randint(-50, 50)
        rand_y = screen_height // 2 + random.randint(-50, 50)

        pyautogui.moveTo(rand_x, rand_y, duration=random.uniform(0.2, 0.6))
        pyautogui.click()

    # Xử lý tab
    tabs = get_chrome_windows()
    print(f"tabs: {tabs}")
    for w in tabs:
        title = w.title.lower()
        if any(k in title for k in KEEP_KEYWORDS):
            print(f"Giu tab: {w.title}")
        else:
            print(f"Dong tab: {w.title}")
            w.activate()
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(0.5)

    time.sleep(3)

print("\nBat dau mo phong nguoi dung trong 250 giay...")
start_time = time.time()
duration = 250

while time.time() - start_time < duration:
    screen_width, screen_height = pyautogui.size()
    rand_x = random.randint(100, screen_width - 100)
    rand_y = random.randint(100, screen_height - 100)

    pyautogui.moveTo(rand_x, rand_y, duration=random.uniform(0.2, 0.5))
    time.sleep(random.uniform(2, 4))

print("Da hoan tat mo phong. Dang chup man hinh...")

timestamp = int(time.time())
os.makedirs("output", exist_ok=True)
screenshot_path = f"output/screenshot_{timestamp}.png"
pyautogui.screenshot(screenshot_path)
print(f"Da luu anh: {screenshot_path}")

# Đóng tất cả tab còn lại
print("Dang dong tat ca tab Chrome...")
tabs = get_chrome_windows()
for w in tabs:
    print(f"Dong tab: {w.title}")
    w.activate()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.5)

print("Hoan tat tat ca.")
