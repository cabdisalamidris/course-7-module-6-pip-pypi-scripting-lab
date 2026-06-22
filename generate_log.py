from lib.generate_log import fetch_data, generate_log


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
    ]

    generate_log(log_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
