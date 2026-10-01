from core.system_info import get_system_info


def main():
    print("Sentinel Ledger 2.3")
    print("System initialized.")
    print()

    system_info = get_system_info()

    print("System Information")
    print("------------------")

    for key, value in system_info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
