import requests
import time

BASE_URL = "https://e56c-116-109-223-76.ngrok-free.app"
TIMEZONE_OFFSET = 7

def run_job():
    url = f"{BASE_URL}/core/run-eligible-tenants"

    params = {
        "moduleKey": "bus-schedule-autogenerators",
        "jobName": "auto_schedule",
        "timezoneOffset": TIMEZONE_OFFSET
    }

    for i in range(3):
        try:
            res = requests.post(url, params=params, timeout=20)

            print(f"Status: {res.status_code}")
            print(res.text)

            res.raise_for_status()
            return True

        except Exception as e:
            print(f"Retry {i+1}: {e}")
            time.sleep(2)

    return False


def main():
    print("=== RUN ELIGIBLE TENANTS ===")

    success = run_job()

    if success:
        print("✅ DONE")
    else:
        print("❌ FAILED")


if __name__ == "__main__":
    main()
