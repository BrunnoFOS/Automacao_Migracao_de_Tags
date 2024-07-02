import pyautogui
import time
import random

cores = [
        "FF5733", "33FF57", "5733FF", "FF33A1", "33FFA1", "A133FF",
        "C70039", "900C3F", "FFC300", "DAF7A6", "581845", "FF0000",
        "00FF00", "0000FF", "FFFF00", "00FFFF", "FF00FF", "800000",
        "008000", "000080", "808000", "800080", "008080", "C0C0C0",
        "808080", "FFA07A", "20B2AA", "87CEFA", "778899", "B0C4DE",
        "FFFFE0", "00FA9A", "F0E68C", "E6E6FA", "FFB6C1", "ADD8E6",
        "F08080", "E0FFFF", "FAFAD2", "D3D3D3", "90EE90", "DA70D6",
        "D8BFD8", "FFD700", "DCDCDC", "DDA0DD", "FF4500", "DAA520",
        "EEE8AA", "98FB98", "AFEEEE", "DB7093", "FFEFD5", "FFDAB9",
        "CD853F", "FFC0CB", "B0E0E6", "FF6347", "4682B4", "9ACD32",
        "483D8B", "2F4F4F", "00CED1", "9400D3", "FF1493", "00BFFF",
        "696969", "1E90FF", "B22222"
    ]

num_repeticoes = 40
for cliques in range(num_repeticoes):
        time.sleep(3)
        pyautogui.click(x=124, y=160)
        time.sleep(1)
        pyautogui.tripleClick(x=185, y=872)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)
        pyautogui.click(x=1835, y=267)
        time.sleep(1)
        pyautogui.click(x=901, y=534)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.doubleClick(x=917, y=599)
        pyautogui.press('delete')
        time.sleep(1)
        cor_aleatoria = random.choice(cores)
        pyautogui.write(cor_aleatoria)
        time.sleep(1)
        pyautogui.click(x=1103, y=702)
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)
        pyautogui.scroll(66)