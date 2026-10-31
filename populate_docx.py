import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc_path = 'E:/PROJEK_AI/Tugas Minggu 10-1/Laporan.docx'
screenshots_dir = 'E:/PROJEK_AI/Tugas Minggu 10-1/Hasil_Scranshot'

doc = docx.Document(doc_path)
table = doc.tables[0]

def set_cell_text(cell, text, bold=False, font_size=10, color=None):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(font_size)
    run.bold = bold
    if color:
        run.font.color.rgb = color
    return p

# 1. Update Identity Table
set_cell_text(table.rows[1].cells[2], "Workshop Pengembangan Website", font_size=9.5)
set_cell_text(table.rows[2].cells[2], "Nugroho Setyo Wibowo, ST. MT", font_size=9.5)
set_cell_text(table.rows[3].cells[2], "Event Broadcast & Reverb", font_size=9.5)
set_cell_text(table.rows[7].cells[2], "Minggu 10 / Pertemuan 1", font_size=9.5)
set_cell_text(table.rows[10].cells[2], "https://github.com/trivaldoaminullah/laravel-reverb-broadcast", font_size=9.5)

# Helper for adding an entry with caption & image
def add_figure(cell, title_text, desc_text, img_filename, max_width_in=5.8):
    p_title = cell.add_paragraph()
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(2)
    run_title = p_title.add_run(title_text)
    run_title.bold = True
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(10)
    run_title.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    if desc_text:
        p_desc = cell.add_paragraph()
        p_desc.paragraph_format.space_before = Pt(0)
        p_desc.paragraph_format.space_after = Pt(4)
        run_desc = p_desc.add_run(desc_text)
        run_desc.font.name = 'Calibri'
        run_desc.font.size = Pt(9.5)

    img_path = os.path.join(screenshots_dir, img_filename)
    if os.path.exists(img_path):
        p_img = cell.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(2)
        p_img.paragraph_format.space_after = Pt(8)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(max_width_in))

# 2. Section H: Kode Program
cell_h = table.rows[9].cells[0]
cell_h.text = "" # Clear placeholder

kode_program_items = [
    ("Instalasi Laravel Reverb",
     "Menjalankan perintah composer require laravel/reverb pada terminal untuk mengunduh dan memasang paket WebSocket Laravel Reverb beserta seluruh pustaka pendukungnya.",
     "terminal_composer_reverb.png"),

    ("Publish Konfigurasi Reverb",
     "Mengeksekusi perintah php artisan vendor:publish --provider=\"Laravel\\Reverb\\ReverbServiceProvider\" untuk menerbitkan berkas konfigurasi config/reverb.php ke dalam aplikasi.",
     "terminal_vendor_publish.png"),

    ("Konfigurasi Server Reverb (config/reverb.php)",
     "Mengatur konfigurasi host 127.0.0.1, port 8080, skema HTTP, serta parameter aplikasi Reverb pada berkas config/reverb.php.",
     "vscode_config_reverb.png"),

    ("Konfigurasi Variabel Lingkungan (.env)",
     "Menambahkan parameter konfigurasi Reverb pada berkas .env meliputi REVERB_APP_ID, REVERB_APP_KEY, REVERB_APP_SECRET, host, port 8080, dan BROADCAST_CONNECTION=reverb.",
     "vscode_env.png"),

    ("Pembuatan Event Class OrderPlaced",
     "Mengeksekusi perintah php artisan make:event OrderPlaced melalui terminal untuk men-generate berkas event broadcast transaksi.",
     "terminal_make_event.png"),

    ("Implementasi Event OrderPlaced (app/Events/OrderPlaced.php)",
     "Mengimplementasikan interface ShouldBroadcast, mendefinisikan private channel user.{id}, nama siaran order.placed, dan payload data transaksi.",
     "vscode_order_placed_event.png"),

    ("Instalasi Pustaka Frontend & Build Aset",
     "Menjalankan perintah npm install --save-dev laravel-echo pusher-js serta npm run build untuk mengompilasi pustaka client WebSocket.",
     "terminal_npm_echo.png"),

    ("Konfigurasi Laravel Echo (resources/js/bootstrap.js)",
     "Menginisialisasi Laravel Echo dengan broadcaster Reverb pada host 127.0.0.1 dan port 8080 agar client siap mendengarkan broadcast.",
     "vscode_bootstrap_echo.png"),

    ("Menjalankan Server WebSocket Reverb",
     "Mengeksekusi perintah php artisan reverb:start pada terminal untuk mengaktifkan daemon server WebSocket Reverb pada port 8080.",
     "terminal_reverb_start.png"),

    ("Menjalankan Server Aplikasi Laravel",
     "Mengeksekusi perintah php artisan serve pada terminal untuk menjalankan web server HTTP Laravel pada port 8000.",
     "terminal_serve.png"),

    ("Menjalankan Queue Worker Antrean",
     "Mengeksekusi perintah php artisan queue:work pada terminal untuk memproses antrean pengiriman event broadcast secara asinkron.",
     "terminal_queue_work.png"),

    ("Controller Pemesanan (app/Http/Controllers/OrderController.php)",
     "Membangun controller pemesanan dengan method store() yang memicu event OrderPlaced ke antrean Reverb saat transaksi berlangsung.",
     "vscode_order_controller.png"),

    ("Routing Aplikasi & Saluran Broadcast (routes/web.php)",
     "Mendefinisikan routing autentikasi, dashboard, broadcast routes, serta endpoint POST /order untuk pemicu event transaksi.",
     "vscode_routes_web.png"),

    ("Integrasi Listener pada View (resources/views/dashboard.blade.php)",
     "Memasang listener Echo.private() pada dashboard untuk menangkap event order.placed dan tombol aksi pengujian notifikasi.",
     "vscode_dashboard_blade.png"),
]

for title, desc, img in kode_program_items:
    add_figure(cell_h, title, desc, img)

# 3. Section I: Tangkapan Layar
cell_i = table.rows[12].cells[0]
cell_i.text = "" # Clear placeholder

tangkapan_layar_items = [
    ("Pengujian Server Reverb Port 8080 (Acara 33)",
     "Mengakses http://127.0.0.1:8080 pada peramban web dan menampilkan respons Not found. yang menandakan server WebSocket Reverb aktif dan berjalan normal.",
     "web_reverb_8080_not_found.png"),

    ("Halaman Welcome Laravel",
     "Tampilan halaman awal Laravel pada http://127.0.0.1:8000 yang menyediakan navigasi autentikasi Log in dan Register.",
     "web_welcome_laravel.png"),

    ("Halaman Registrasi Pengguna (/register)",
     "Tampilan form registrasi akun pengguna baru pada aplikasi.",
     "web_register.png"),

    ("Halaman Verifikasi Email (/verify-email)",
     "Tampilan antarmuka pemberitahuan verifikasi email pengguna.",
     "web_verify_email.png"),

    ("Halaman Login Pengguna (/login)",
     "Tampilan antarmuka login pengguna dengan input alamat email dan password.",
     "web_login.png"),

    ("Halaman Dashboard Utama (/dashboard)",
     "Tampilan dashboard utama setelah login, memperlihatkan status koneksi WebSocket terhubung dan informasi private channel user.",
     "web_dashboard.png"),

    ("Pengujian Notifikasi Real-Time (Acara 34)",
     "Hasil pengujian saat tombol Tes Notifikasi ditekan: event OrderPlaced berhasil dipancarkan dan Laravel Echo langsung menangkap event secara real-time dengan memunculkan alert box 'Order #4821 telah ditempatkan! Total: Rp 50000', update log console, dan banner informasi.",
     "web_dashboard_alert_notification.png"),
]

for title, desc, img in tangkapan_layar_items:
    add_figure(cell_i, title, desc, img)

# 4. Section J: Penjelasan
cell_j = table.rows[14].cells[0]
cell_j.text = ""

def add_heading(cell, text):
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    run.bold = True
    run.font.name = 'Calibri'
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

def add_bullet(cell, num_str, title_bold, text):
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.first_line_indent = Inches(-0.2)
    run_num = p.add_run(f"{num_str} ")
    run_num.bold = True
    run_num.font.name = 'Calibri'
    run_num.font.size = Pt(9.5)
    run_title = p.add_run(f"{title_bold}: ")
    run_title.bold = True
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(9.5)
    run_text = p.add_run(text)
    run_text.font.name = 'Calibri'
    run_text.font.size = Pt(9.5)

add_heading(cell_j, "Penjelasan Praktikum Acara 33: Instalasi dan Konfigurasi Laravel Reverb")
add_bullet(cell_j, "1.", "Instalasi Paket Laravel Reverb", "Melakukan instalasi library resmi Laravel Reverb menggunakan perintah composer require laravel/reverb untuk menyediakan server WebSocket mandiri dengan performa tinggi.")
add_bullet(cell_j, "2.", "Publikasi dan Konfigurasi Berkas Reverb", "Mempublikasikan berkas konfigurasi config/reverb.php melalui perintah vendor:publish, lalu mengonfigurasi host 127.0.0.1, port 8080, skema HTTP, serta opsi TLS.")
add_bullet(cell_j, "3.", "Pengaturan Variabel Lingkungan (.env)", "Menambahkan variabel lingkungan REVERB_APP_ID, REVERB_APP_KEY, REVERB_APP_SECRET, REVERB_HOST, REVERB_PORT, serta mengatur BROADCAST_CONNECTION=reverb.")
add_bullet(cell_j, "4.", "Pembuatan Event Transaksi OrderPlaced", "Men-generate event class menggunakan perintah php artisan make:event OrderPlaced pada direktori app/Events.")
add_bullet(cell_j, "5.", "Implementasi ShouldBroadcast", "Mengimplementasikan interface ShouldBroadcast pada event OrderPlaced, mengatur saluran siaran privat user.{id}, nama siaran order.placed, dan payload data transaksi.")
add_bullet(cell_j, "6.", "Konfigurasi Laravel Echo dan Pengujian Server", "Memasang pustaka laravel-echo dan pusher-js pada frontend, mengonfigurasi instance Echo di bootstrap.js, serta menjalankan server Reverb (php artisan reverb:start) yang divalidasi melalui akses port 8080.")

add_heading(cell_j, "Penjelasan Praktikum Acara 34: Integrasi Listener Laravel Echo dan Pengujian")
add_bullet(cell_j, "1.", "Integrasi Listener pada View", "Menambahkan script listener Laravel Echo pada tampilan view dashboard.blade.php untuk menangani aliran siaran data event secara asinkron.")
add_bullet(cell_j, "2.", "Penerapan Private Channel per Pengguna", "Mengonfigurasi listener window.Echo.private('user.{id}') agar notifikasi transaksi hanya disiarkan dan diterima secara privat oleh pengguna pemilik transaksi.")
add_bullet(cell_j, "3.", "Autentikasi dan Otorisasi Saluran", "Mendefinisikan aturan otorisasi saluran pada routes/channels.php dan bootstrap/app.php untuk memastikan user yang melakukan subscribe memiliki ID yang valid dan cocok.")
add_bullet(cell_j, "4.", "Pembuatan Controller dan Route Pemicu", "Membuat OrderController dengan method store() yang memancarkan event OrderPlaced, serta mendaftarkan rute POST /order yang dipanggil melalui tombol antarmuka.")
add_bullet(cell_j, "5.", "Visualisasi Notifikasi Pop-Up", "Menampilkan respons pesan notifikasi instan berupa alert dialog pop-up browser, pembaruan kotak log riwayat event, dan banner interaktif saat data siaran tiba di peramban.")
add_bullet(cell_j, "6.", "Pengujian Simultan Komponen Real-Time", "Menguji integrasi menyeluruh yang menghubungkan server Reverb (port 8080), aplikasi Laravel (port 8000), queue worker pemroses antrean, dan peramban web client secara waktu nyata.")

# 5. Section K: Kesimpulan
cell_k = table.rows[16].cells[0]
cell_k.text = ""

add_heading(cell_k, "Kesimpulan Praktikum")
add_bullet(cell_k, "•", "Kesimpulan Acara 33", "Mahasiswa berhasil memahami konsep komunikasi dua arah secara real-time berbasis protokol WebSocket pada Laravel menggunakan Laravel Reverb. Instalasi library laravel/reverb, penerbitan dan penyesuaian berkas konfigurasi config/reverb.php dan .env, perancangan event class OrderPlaced yang mengimplementasikan kontrak ShouldBroadcast, serta inisialisasi Laravel Echo di sisi frontend berhasil diimplementasikan dan diverifikasi berjalan dengan baik pada port 8080.")
add_bullet(cell_k, "•", "Kesimpulan Acara 34", "Mahasiswa berhasil mengintegrasikan komunikasi real-time antara Laravel Reverb di sisi server dan Laravel Echo di sisi client. Penggunaan private channel per user menjamin aspek keamanan transmisi data transaksi. Mekanisme pemicu event melalui rute dan controller terbukti mampu memicu siaran event secara instan, diproses oleh queue worker, dan langsung ditangkap oleh listener frontend dengan memunculkan notifikasi pop-up alert browser dan pencatatan log interaktif tanpa memerlukan reload halaman web.")

doc.save(doc_path)
print("Laporan.docx updated and saved successfully.")
