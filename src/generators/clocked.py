# clocked.py
import time

def countdown_timer(seconds):
    """Yield remaining seconds each tick until 0."""
    if seconds <= 0:
        raise ValueError("Please enter a positive number of seconds.")
    
    # print(f"⏳ Timer started for {seconds} seconds...")
    while seconds > 0:
        yield seconds   # only yield, no printing
        time.sleep(1)
        seconds -= 1
    # print("⏰ Time's up!            ")


def stopwatch():
    """Runs a stopwatch until the user stops it."""
    print("⏱ Stopwatch started. Press Ctrl+C to stop.")
    start_time = time.time()
    try:
        while True:
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            millis = int((elapsed - int(elapsed)) * 100)
            print(f"{mins:02}:{secs:02}.{millis:02}", end="\r")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n✅ Stopwatch stopped.")


def run_as_script():
    """Menu when running clocked.py directly."""
    while True:
        print("\n--- Python Timer & Stopwatch ---")
        print("1. Countdown Timer")
        print("2. Stopwatch")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                seconds = int(input("Enter time in seconds: ").strip())
                print(f"⏳ Timer started for {seconds} seconds...")
                for remaining in countdown_timer(seconds):
                    # here we print because it's standalone
                    mins, secs = divmod(remaining, 60)
                    print(f"{mins:02}:{secs:02} | Remaining: {remaining}", end="\r")
                print("⏰ Time's up!            ")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "2":
            stopwatch()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# 👇 This runs only if you execute clocked.py directly
if __name__ == "__main__":
    run_as_script()
