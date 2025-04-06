import tkinter as tk
from tkinter import messagebox

# Sabit kullanıcı PIN ve başlangıç bakiyesi
USER_PIN = "1234"
balance = [1000.0]  # Liste olarak tutuldu çünkü referansla değiştirilebilir

# Renk teması
bg_color = "#f0f4f8"
primary_color = "#3498db"
secondary_color = "#2c3e50"
font_name = "Segoe UI"

def show_atm_screen():
    def update_balance():
        balance_label.config(text=f"Bakiye: {balance[0]:.2f} TL")

    def deposit_money():
        try:
            amount = float(entry.get())
            if amount > 0:
                balance[0] += amount
                update_balance()
                entry.delete(0, tk.END)
                messagebox.showinfo("Başarılı", f"{amount} TL yatırıldı.")
            else:
                messagebox.showwarning("Hatalı Giriş", "Pozitif bir miktar girin.")
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir miktar girin.")

    def withdraw_money():
        try:
            amount = float(entry.get())
            if amount > 0 and amount <= balance[0]:
                balance[0] -= amount
                update_balance()
                entry.delete(0, tk.END)
                messagebox.showinfo("Başarılı", f"{amount} TL çekildi.")
            elif amount > balance[0]:
                messagebox.showwarning("Yetersiz Bakiye", "Bu kadar paranız yok.")
            else:
                messagebox.showwarning("Hatalı Giriş", "Pozitif bir miktar girin.")
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir miktar girin.")

    def logout():
        atm_window.destroy()
        show_login_screen()

    login_window.destroy()
    atm_window = tk.Tk()
    atm_window.title("🌟 ATM Uygulaması")
    atm_window.geometry("400x400")
    atm_window.configure(bg=bg_color)

    tk.Label(atm_window, text="ATM Paneli", font=(font_name, 20, "bold"), fg=primary_color, bg=bg_color).pack(pady=10)

    balance_label = tk.Label(atm_window, text=f"Bakiye: {balance[0]:.2f} TL", font=(font_name, 14), bg=bg_color)
    balance_label.pack(pady=5)

    entry = tk.Entry(atm_window, font=(font_name, 12), justify='center')
    entry.pack(pady=10, ipady=5, ipadx=10)

    tk.Button(atm_window, text="💰 Para Yatır", font=(font_name, 12), bg=primary_color, fg="white",
              relief="flat", command=deposit_money).pack(pady=5, ipadx=10, ipady=5)

    tk.Button(atm_window, text="🏧 Para Çek", font=(font_name, 12), bg="#e67e22", fg="white",
              relief="flat", command=withdraw_money).pack(pady=5, ipadx=10, ipady=5)

    tk.Button(atm_window, text="🚪 Çıkış Yap", font=(font_name, 12), bg="#e74c3c", fg="white",
              relief="flat", command=logout).pack(pady=20, ipadx=10, ipady=5)

    atm_window.mainloop()

def show_login_screen():
    def check_pin():
        pin = pin_entry.get()
        if pin == USER_PIN:
            show_atm_screen()
        else:
            messagebox.showerror("Hatalı PIN", "Girdiğiniz PIN yanlış!")

    global login_window
    login_window = tk.Tk()
    login_window.title("🔐 Giriş Yap")
    login_window.geometry("400x250")
    login_window.configure(bg=bg_color)

    tk.Label(login_window, text="ATM Giriş Ekranı", font=(font_name, 18, "bold"), fg=secondary_color, bg=bg_color).pack(pady=20)

    pin_entry = tk.Entry(login_window, show="*", font=(font_name, 14), justify='center')
    pin_entry.pack(pady=10, ipady=5, ipadx=10)

    tk.Button(login_window, text="Giriş", font=(font_name, 12), bg=primary_color, fg="white",
              relief="flat", command=check_pin).pack(pady=15, ipadx=15, ipady=5)

    login_window.mainloop()

show_login_screen()
