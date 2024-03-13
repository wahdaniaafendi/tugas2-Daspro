# Data dictionary (username: password)
data_mahasiswa = {
    'ShunKazama': 'password1',
    'UmiMatsuzaki': 'password2',
    'Chihiro': 'password3',
    'Haku': 'password4',
    'Howl': 'password5',
    'Sophie': 'password6',
    'kiki': 'password7',
    'Tombo': 'password8',
    'Jiro': 'password9',
    'SeijiAmasawa': 'password10'
}

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print(f"Selamat datang, {username}!")
    else:
        print("Data yang dimasukkan salah. Coba lagi.")

if __name__ == "__main__":
    login()
