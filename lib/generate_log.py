from datetime import datetime
import requests


def generate_log(data):
    """Write a log summary to a file with today's date."""

    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch data from a public API."""

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    return {}


if __name__ == "__main__":
    # Generate log file
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(log_data)

    # Fetch data from API
    post = fetch_data()

    if post:
        print(
            "Fetched Post Title:",
            post.get("title", "No title found")
        )