import pyautogui
import time
import sys
import argparse
from PIL import Image

# Image paths
RETRY_BUTTON_IMG = r"images\retrybutton.png"
ALLOW_IN_WORKSPACE_IMG = r"images\allowinworkspace.png"

# Time interval to check for the button (in seconds)
CHECK_INTERVAL_SECONDS = 5

def get_allowed_checks(selection):
    if selection == "1":
        return [RETRY_BUTTON_IMG]
    elif selection == "2":
        return [ALLOW_IN_WORKSPACE_IMG]
    else:
        return [RETRY_BUTTON_IMG, ALLOW_IN_WORKSPACE_IMG]

def auto_retry_bot(check_selection):
    targets = get_allowed_checks(check_selection)
    target_names = {RETRY_BUTTON_IMG: "Retry Button", ALLOW_IN_WORKSPACE_IMG: "Allow in Workspace"}
    labels = " and ".join(target_names[t] for t in targets)

    print(f"Bot started. Searching for {labels} every {CHECK_INTERVAL_SECONDS} seconds...")
    print("Press Ctrl+C in the terminal to stop the bot.\n")

    while True:
        try:
            print(f"[{time.strftime('%H:%M:%S')}] Checking screen...")
            any_found = False
            for img_path in targets:
                location = pyautogui.locateCenterOnScreen(img_path, confidence=0.6)
                if location is not None:
                    print(f"[{time.strftime('%H:%M:%S')}] {target_names[img_path]} found at {location}!")
                    
                    # Save current cursor position
                    original_pos = pyautogui.position()
                    print(f"Saved cursor position: {original_pos}")
                    
                    # Click directly (OCR verification removed)
                    print(f"[{time.strftime('%H:%M:%S')}] {target_names[img_path]} found. Clicking...")
                    pyautogui.click(int(location.x), int(location.y))
                    time.sleep(2)
                    any_found = True
                    
                    # Return cursor to original position
                    pyautogui.moveTo(original_pos)
                    print(f"Cursor returned to: {original_pos}")
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] {target_names[img_path]} not found this cycle.")

            if not any_found:
                print(f"[{time.strftime('%H:%M:%S')}] No target images found this cycle.")

        except pyautogui.ImageNotFoundException:
            print(f"[{time.strftime('%H:%M:%S')}] No target image found this cycle.")
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] An unexpected error occurred: {e}")

        for i in range(CHECK_INTERVAL_SECONDS, 0, -1):
            print(f"Waiting to check again in {i} seconds...", end='\r', flush=True)
            time.sleep(1)
        print(" " * 50, end='\r', flush=True)

def main():
    parser = argparse.ArgumentParser(description="Auto-retry bot with multiple image support")
    parser.add_argument(
        "--check",
        choices=["1", "2", "all"],
        default="all",
        help="Which image(s) to check: 1=Retry Button, 2=Allow in Workspace, all=both (default)"
    )
    args = parser.parse_args()
    auto_retry_bot(args.check)

if __name__ == "__main__":
    main()