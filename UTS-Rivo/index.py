import hashlib
import os

USER_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                username, hashed = line.strip().split(":")
                users[username] = hashed
    return users

def save_user(username, hashed_password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{hashed_password}\n")

def register():
    print("\n=== REGISTER ===")
    username = input("Buat username: ").strip()
    password = input("Buat password: ").strip()

    users = load_users()

    if username in users:
        print("❌ Username sudah digunakan. Silakan pilih yang lain.")
        return

    hashed = hash_password(password)
    save_user(username, hashed)
    print("✅ Pendaftaran berhasil!")

def login():
    print("\n=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    users = load_users()
    hashed = hash_password(password)

    if username in users and users[username] == hashed:
        print(f"✅ Login berhasil. Selamat datang, {username}!")
    else:
        print("❌ Login gagal. Username atau password salah.")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        choice = input("Pilih (1/2/3): ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid.")

# Jalankan program
main()
