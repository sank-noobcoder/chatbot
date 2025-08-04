# chatbot
# 🧠 CSV-Based Chatbot using Flask

This project is a simple AI-powered chatbot built with **Python**, **Flask**, and a **CSV file** as the data source. It provides intelligent responses based on the data loaded from the CSV and can be easily deployed on a local server.

---

## 🚀 Features

- Uses **CSV file** as a knowledge base
- Built with lightweight **Flask** framework
- Simple and clean **frontend** UI
- Easy to deploy and extend
- Customizable response logic

---

## 📁 Project Structure

├── app.py # Flask backend application
├── chatbot.py # Chatbot logic (reads and responds from CSV)
├── data/
│ └── knowledge.csv # CSV file with questions and answers
├── templates/
│ └── index.html # Frontend interface
├── static/
│ └── style.css # (Optional) Styling for frontend

---

## 📄 CSV File Format

Make sure your `knowledge.csv` inside the `data/` folder looks like this:

csv
question,answer
"Hello", "Hi there! How can I help you?"
"What's your name?", "I am your AI assistant."
"How are you?", "I'm doing well, thank you!"
