import subprocess


def get_running_processes():
    result = subprocess.run(
        ["ps", "-eo", "pid,comm"],
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout


if __name__ == "__main__":
    print(get_running_processes())
