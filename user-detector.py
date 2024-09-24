# Fungsi ini menerima sebuah event dan mengembalikan tanggal dari event tersebut. Fungsinya adalah untuk digunakan sebagai kunci dalam menyortir event berdasarkan tanggal.
def get_event_date(event):
    return event.date

# Fungsi ini melakukan beberapa hal:

# Menerima daftar event dan mengurutkan event berdasarkan tanggal menggunakan events.sort(key=get_event_date).
# Membuat dictionary machines untuk melacak siapa yang sedang login pada setiap mesin.
# Melalui loop for event in events, fungsi ini memeriksa setiap event:
# Jika mesin belum ada di dictionary machines, maka dibuat entri baru untuk mesin tersebut menggunakan set(), karena set memudahkan untuk menambah dan menghapus user.
# Jika event adalah "login", maka user ditambahkan ke set pengguna mesin tersebut.
# Jika event adalah "logout", maka user dikeluarkan dari set pengguna mesin tersebut.
# Fungsi ini mengembalikan dictionary yang berisi mesin-mesin dengan daftar pengguna yang sedang login.
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


# Fungsi ini membuat laporan dari dictionary machines yang dihasilkan oleh current_users. Laporan tersebut menampilkan mesin dan daftar pengguna yang sedang login.

# Melalui for machine, users in machines.items(), fungsi ini memeriksa tiap mesin.
# Jika ada user yang login di mesin tersebut (len(users) > 0), maka daftar user diubah menjadi string yang dipisahkan koma dan ditampilkan menggunakan print.
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))



# Kelas ini digunakan untuk membuat objek event. Setiap event memiliki atribut:

# date: Tanggal event terjadi.
# type: Jenis event, bisa "login" atau "logout".
# machine: Nama mesin yang terlibat.
# user: Nama pengguna yang terlibat dalam event.
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

# Ini adalah daftar event yang melibatkan login dan logout pengguna dari beberapa mesin.
events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
