import tkinter as tk
from tkinter import messagebox
import random


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("🍦 Important Question")
root.geometry("700x650")
root.configure(bg="#17051f")
root.resizable(False, False)


# =========================
# VARIABLES
# =========================

flavor = ""
location = ""
selected_date = ""
selected_time = ""


# =========================
# HELPER FUNCTIONS
# =========================

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def title(text, size=30):
    label = tk.Label(
        root,
        text=text,
        font=("Arial", size, "bold"),
        fg="white",
        bg="#17051f"
    )
    label.pack(pady=15)


def normal_text(text):
    label = tk.Label(
        root,
        text=text,
        font=("Arial", 15),
        fg="#dddddd",
        bg="#17051f",
        justify="center"
    )
    label.pack(pady=10)


def button(text, command, color="#ff4da6"):
    btn = tk.Button(
        root,
        text=text,
        command=command,
        font=("Arial", 14, "bold"),
        fg="white",
        bg=color,
        activebackground="#ff79c6",
        activeforeground="white",
        relief="flat",
        padx=25,
        pady=10,
        cursor="hand2"
    )
    btn.pack(pady=7)

    return btn


# =========================
# STEP 1
# =========================

def first_screen():

    clear_screen()

    tk.Label(
        root,
        text="🍦",
        font=("Arial", 75),
        bg="#17051f"
    ).pack(pady=10)

    title("I Have A Very Important Question...", 27)

    normal_text(
        "This is extremely serious.\n"
        "You have been selected for an important mission."
    )

    title("Will you buy me ice cream? ❤️", 24)

    button("YES 🍦", start_order)

    button("YES, OBVIOUSLY 😌", start_order)

    no_button = button("NO 😭", move_no_button, "#555555")

    # Store button so we can move it
    root.no_button = no_button


def move_no_button():

    # Make the NO button jump somewhere else
    x = random.randint(50, 550)
    y = random.randint(350, 550)

    root.no_button.place(x=x, y=y)

    messagebox.showinfo(
        "Nice try 😂",
        "The NO button has escaped! 😭"
    )


# =========================
# STEP 2 - FLAVOR
# =========================

def start_order():

    clear_screen()

    title("STEP 1 OF 4", 16)

    tk.Label(
        root,
        text="🍨",
        font=("Arial", 65),
        bg="#17051f"
    ).pack()

    title("Choose your flavor 🍦", 28)

    normal_text("Choose wisely... this is very important.")

    flavors = [
        "🍫 Chocolate",
        "🤍 Vanilla",
        "🍓 Strawberry",
        "🍪 Cookies & Cream",
        "🌿 Mint Chocolate",
        "😏 Surprise Me"
    ]

    for item in flavors:
        button(
            item,
            lambda value=item: choose_flavor(value)
        )


def choose_flavor(value):

    global flavor

    flavor = value

    location_screen()


# =========================
# STEP 3 - LOCATION
# =========================

def location_screen():

    clear_screen()

    title("STEP 2 OF 4", 16)

    tk.Label(
        root,
        text="📍",
        font=("Arial", 60),
        bg="#17051f"
    ).pack()

    title("Where are we getting it?", 27)

    normal_text(
        "Choose a location or type one below."
    )

    button(
        "🛍️ MART",
        lambda: choose_location("MART")
    )

    button(
        "🍦 3-LINE",
        lambda: choose_location("3-LINE")
    )

    button(
        "😌 You choose",
        lambda: choose_location("You choose")
    )

    global location_entry

    location_entry = tk.Entry(
        root,
        font=("Arial", 15),
        width=35,
        justify="center"
    )

    location_entry.pack(pady=15)

    location_entry.insert(
        0,
        "Or type a location..."
    )

    button(
        "NEXT →",
        custom_location
    )


def choose_location(value):

    global location

    location = value

    date_screen()


def custom_location():

    global location

    value = location_entry.get().strip()

    if value == "" or value == "Or type a location...":
        messagebox.showwarning(
            "Location needed",
            "You need to choose or enter a location! 📍"
        )
        return

    location = value

    date_screen()


# =========================
# STEP 4 - DATE
# =========================

def date_screen():

    clear_screen()

    title("STEP 3 OF 4", 16)

    tk.Label(
        root,
        text="📅",
        font=("Arial", 60),
        bg="#17051f"
    ).pack()

    title("Pick the date 📅", 28)

    normal_text(
        "When are we getting that ice cream?"
    )

    global date_entry

    date_entry = tk.Entry(
        root,
        font=("Arial", 18),
        width=20,
        justify="center"
    )

    date_entry.pack(pady=20)

    date_entry.insert(
        0,
        "DD/MM/YYYY"
    )

    button(
        "NEXT →",
        check_date
    )


def check_date():

    global selected_date

    value = date_entry.get().strip()

    if value == "" or value == "DD/MM/YYYY":

        messagebox.showwarning(
            "Date needed",
            "Please enter a date! 📅"
        )

        return

    selected_date = value

    time_screen()


# =========================
# STEP 5 - TIME
# =========================

def time_screen():

    clear_screen()

    title("STEP 4 OF 4", 16)

    tk.Label(
        root,
        text="⏰",
        font=("Arial", 60),
        bg="#17051f"
    ).pack()

    title("What time? ⏰", 28)

    normal_text(
        "Choose the perfect ice cream time."
    )

    global time_entry

    time_entry = tk.Entry(
        root,
        font=("Arial", 18),
        width=20,
        justify="center"
    )

    time_entry.pack(pady=20)

    time_entry.insert(
        0,
        "Example: 3:30 PM"
    )

    button(
        "CONFIRM 🍦",
        finish_order
    )


def finish_order():

    global selected_time

    value = time_entry.get().strip()

    if value == "" or value == "Example: 3:30 PM":

        messagebox.showwarning(
            "Time needed",
            "Please enter a time! ⏰"
        )

        return

    selected_time = value

    final_screen()


# =========================
# FINAL SCREEN
# =========================

def final_screen():

    clear_screen()

    tk.Label(
        root,
        text="❤️",
        font=("Arial", 90),
        bg="#17051f"
    ).pack(pady=10)

    title("Ice-Cream Date! 🍦", 32)

    normal_text(
        "Your extremely important ice cream\n"
        "appointment has officially been scheduled."
    )

    summary = tk.Frame(
        root,
        bg="#2b1038",
        padx=25,
        pady=20
    )

    summary.pack(pady=15)

    tk.Label(
        summary,
        text=f"🍦 Flavor: {flavor}",
        font=("Arial", 15, "bold"),
        fg="white",
        bg="#2b1038"
    ).pack(anchor="w", pady=4)

    tk.Label(
        summary,
        text=f"📍 Location: {location}",
        font=("Arial", 15, "bold"),
        fg="white",
        bg="#2b1038"
    ).pack(anchor="w", pady=4)

    tk.Label(
        summary,
        text=f"📅 Date: {selected_date}",
        font=("Arial", 15, "bold"),
        fg="white",
        bg="#2b1038"
    ).pack(anchor="w", pady=4)

    tk.Label(
        summary,
        text=f"⏰ Time: {selected_time}",
        font=("Arial", 15, "bold"),
        fg="white",
        bg="#2b1038"
    ).pack(anchor="w", pady=4)

    title("🍦❤️ THANK YOU ❤️🍦", 23)

    normal_text(
        "Payment accepted:\n"
        "ONE ICE CREAM 🍦😂"
    )


# =========================
# START PROGRAM
# =========================

first_screen()

root.mainloop()
