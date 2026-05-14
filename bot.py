import pyautogui
import time

# Image path
RETRY_BUTTON_IMG = r"images\retrybutton.png"

# Time interval to check for the button (in seconds)
CHECK_INTERVAL_SECONDS = 5

def auto_retry_bot():
    print(f"Bot started. Searching for the retry button every {CHECK_INTERVAL_SECONDS} seconds...")
    print("Press Ctrl+C in the terminal to stop the bot.\n")

    while True:
        try:
            print(f"[{time.strftime('%H:%M:%S')}] Checking screen for retry button...")
            retry_location = pyautogui.locateCenterOnScreen(RETRY_BUTTON_IMG, confidence=0.7)

            if retry_location is not None:
                print(f"[{time.strftime('%H:%M:%S')}] Retry button found at {retry_location}! Clicking...")
                pyautogui.click(retry_location)
                time.sleep(2)
            else:
                print(f"[{time.strftime('%H:%M:%S')}] No retry button found this cycle.")

        except pyautogui.ImageNotFoundException:
            print(f"[{time.strftime('%H:%M:%S')}] No target image found this cycle.")
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] An unexpected error occurred: {e}")

        for i in range(CHECK_INTERVAL_SECONDS, 0, -1):
            print(f"Waiting to check again in {i} seconds...", end='\r', flush=True)
            time.sleep(1)
        print(" " * 50, end='\r', flush=True)

if __name__ == "__main__":
    auto_retry_bot()