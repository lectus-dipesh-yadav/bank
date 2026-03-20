import tkinter as tk
from tkinter import messagebox
import json
import os


file_name = "bank_data.json"

# ---------- Load Data ----------
def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return {}

# ---------- Save Data ----------
def save_data():
    with open(file_name, "w") as f:
        json.dump(accounts, f)

accounts = load_data()

# ---------- Create Account ----------
def create_account():
    acc = acc_entry.get()
    name = name_entry.get()

    if acc == "" or name == "":
        messagebox.showwarning("Warning","Please fill all fields")
        return

    if acc in accounts:
        messagebox.showerror("Error","Account already exists")
    else:
        accounts[acc] = {"name":name,"balance":0}
        save_data()
        messagebox.showinfo("Success","Account Created Successfully")

# ---------- Deposit ----------
def deposit_money():
    acc = acc_entry.get()

    if acc not in accounts:
        messagebox.showerror("Error","Account not found")
        return

    try:
        amt = int(amount_entry.get())
        accounts[acc]["balance"] += amt
        save_data()
        messagebox.showinfo("Success","Money Deposited")
    except:
        messagebox.showerror("Error","Enter valid amount")

# ---------- Withdraw ----------
def withdraw_money():
    acc = acc_entry.get()

    if acc not in accounts:
        messagebox.showerror("Error","Account not found")
        return

    try:
        amt = int(amount_entry.get())

        if accounts[acc]["balance"] >= amt:
            accounts[acc]["balance"] -= amt
            save_data()
            messagebox.showinfo("Success","Money Withdrawn")
        else:
            messagebox.showerror("Error","Insufficient Balance")
    except:
        messagebox.showerror("Error","Enter valid amount")

# ---------- Check Balance ----------
def check_balance():
    acc = acc_entry.get()

    if acc in accounts:
        bal = accounts[acc]["balance"]
        messagebox.showinfo("Balance",f"Current Balance: {bal}")
    else:
        messagebox.showerror("Error","Account not found")

# ---------- Show All Accounts ----------
def show_accounts():
    display.delete(1.0, tk.END)

    for acc,data in accounts.items():
        display.insert(tk.END,f"Account No: {acc}\n")
        display.insert(tk.END,f"Name: {data['name']}\n")
        display.insert(tk.END,f"Balance: {data['balance']}\n")
        display.insert(tk.END,"---------------------------\n")

# ---------- GUI ----------
root = tk.Tk()
root.title("Basic Banking System")
root.geometry("520x550")
root.config(bg="#FFFFFF")   # White background

# Header
title = tk.Label(
    root,
    text="Basic Banking System",
    font=("elephant",25,"bold"),
    bg="#1E3A8A",     # Dark Blue
    fg="white",
    pady=10
)
title.pack(fill="x")

# Main Frame
frame = tk.Frame(root,bg="#F1F5F9",padx=20,pady=20)  # Light Gray
frame.pack(pady=20)

tk.Label(frame,text="Account Number",bg="#F1F5F9",font=("Arial",12,)).grid(row=0,column=0,pady=8)

acc_entry = tk.Entry(frame,width=25)
acc_entry.grid(row=0,column=1,pady=8)

tk.Label(frame,text="Account Holder Name",bg="#F1F5F9",font=("Arial",12,)).grid(row=1,column=0,pady=8)
name_entry = tk.Entry(frame,width=25)
name_entry.grid(row=1,column=1,pady=8)

tk.Label(frame,text="Amount",bg="#F1F5F9",font=("Arial",13,)).grid(row=2,column=0,pady=8)
amount_entry = tk.Entry(frame,width=28)
amount_entry.grid(row=2,column=1,pady=8)

# Buttons Frame
btn_frame = tk.Frame(root,bg="#FFFFFF")
btn_frame.pack(pady=10)

btn_style = {
    "width":18,
    "bg":"#1E3A8A",   # Blue Buttons
    "fg":"white",
    "activebackground":"#163172"
}

tk.Button(btn_frame,text="Create Account",command=create_account,**btn_style).grid(row=0,column=0,padx=5,pady=5)
tk.Button(btn_frame,text="Deposit Money",command=deposit_money,**btn_style).grid(row=0,column=1,padx=5,pady=5)
tk.Button(btn_frame,text="Withdraw Money",command=withdraw_money,**btn_style).grid(row=1,column=0,padx=5,pady=5)
tk.Button(btn_frame,text="Check Balance",command=check_balance,**btn_style).grid(row=1,column=1,padx=5,pady=5)

tk.Button(
    root,
    text="Show All Accounts",
    command=show_accounts,
    width=38,
    bg="#1E3A8A",
    fg="white"
).pack(pady=10)

# Display Area
display = tk.Text(root,height=12,width=55,bg="#F1F5F9")
display.pack(pady=10)

root.mainloop()