def gtfobins_helper():
    print("\n=== GTFOBins Helper ===\n")
    binary = input("Enter binary name (e.g. sudo, tar, find): ").strip()

    if not binary:
        input("No binary entered. Press Enter...")
        return

    print(f"\nGTFOBins page:")
    print(f"https://gtfobins.github.io/gtfobins/{binary}/\n")

    print("Basic checks:")
    print(f"which {binary}")
    print(f"sudo -l")
    print(f"find / -perm -4000 -name {binary} 2>/dev/null")

    input("\nPress Enter to return...")
