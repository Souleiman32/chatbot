import openai
import os
import tkinter as tk
from tkinter import ttk

# Remplacez par votre clé API
api_key = "" #mettez votre clé API GPT3

openai.api_key = api_key

conversation_history = []

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

def on_submit():
    global conversation_history
    user_input = user_entry.get()
    if user_input.lower() == "quit":
        root.quit()
    conversation_history.append(f"Un utilisateur demande : {user_input}")
    user_entry.delete(0, tk.END)
    
    prompt = "\n".join(conversation_history) + "\nComment répondre :"
    response = generate_response(prompt)
    
    conversation_history.append(f"Chatbot répond : {response}")
    response_label.config(text=f"Chatbot : {response}")

    

root = tk.Tk()
root.title("Chatbot")

frame1 = ttk.Frame(root, padding="10 10 10 10")
frame1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

chat_text = tk.Text(frame1, wrap=tk.WORD, width=50, height=20)
chat_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=chat_text.yview)
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
chat_text["yscrollcommand"] = scrollbar.set

frame2 = ttk.Frame(root, padding="10 0 10 10")
frame2.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

user_entry = ttk.Entry(frame2, width=40)
user_entry.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

submit_button = ttk.Button(frame2, text="Envoyer", command=on_submit)
submit_button.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

user_entry.focus()

root.mainloop()
