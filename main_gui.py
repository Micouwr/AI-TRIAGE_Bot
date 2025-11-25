# main_gui.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
from bot_engine.router import classify_ticket
import threading

class TicketClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Ticket Classifier")
        self.root.geometry("600x450")

        # --- UI Elements ---
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Input Area
        input_label = tk.Label(self.main_frame, text="Enter Ticket Text:", font=("Arial", 12))
        input_label.pack(anchor="w")

        self.input_text = scrolledtext.ScrolledText(self.main_frame, height=10, width=70, wrap=tk.WORD)
        self.input_text.pack(pady=5, fill=tk.BOTH, expand=True)

        # Button
        self.classify_button = tk.Button(self.main_frame, text="Classify Ticket", command=self.start_classification_thread, font=("Arial", 12, "bold"))
        self.classify_button.pack(pady=10)

        # Results Area
        results_frame = tk.LabelFrame(self.main_frame, text="Classification Results", padx=10, pady=10)
        results_frame.pack(fill=tk.X, expand=True)

        self.result_text = tk.StringVar(value="Result: N/A")
        result_label = tk.Label(results_frame, textvariable=self.result_text, font=("Arial", 11))
        result_label.pack(anchor="w")

        self.confidence_text = tk.StringVar(value="Confidence: N/A")
        confidence_label = tk.Label(results_frame, textvariable=self.confidence_text, font=("Arial", 11))
        confidence_label.pack(anchor="w")

        self.pii_text = tk.StringVar(value="Contains PII: N/A")
        pii_label = tk.Label(results_frame, textvariable=self.pii_text, font=("Arial", 11))
        pii_label.pack(anchor="w")

        # Status Bar
        self.status_text = tk.StringVar(value="Ready")
        status_bar = tk.Label(root, textvariable=self.status_text, bd=1, relief=tk.SUNKEN, anchor="w")
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def start_classification_thread(self):
        """Starts the classification in a separate thread to keep the GUI responsive."""
        ticket_text = self.input_text.get("1.0", tk.END).strip()
        if not ticket_text:
            messagebox.showwarning("Input Error", "Ticket text cannot be empty.")
            return

        self.classify_button.config(state=tk.DISABLED)
        self.status_text.set("Classifying, please wait...")

        # Run classification in a thread to prevent freezing the GUI
        thread = threading.Thread(target=self.run_classification, args=(ticket_text,))
        thread.start()

    def run_classification(self, ticket_text):
        """Calls the backend classifier and updates the GUI with the results."""
        try:
            result = classify_ticket(ticket_text)
            self.root.after(0, self.update_ui_with_results, result)
        except Exception as e:
            self.root.after(0, self.show_error, str(e))
        finally:
            self.root.after(0, self.reset_ui_state)

    def update_ui_with_results(self, result):
        """Updates the result labels in the GUI."""
        self.result_text.set(f"Result: {result.get('ticket_type', 'Error')}")
        self.confidence_text.set(f"Confidence: {result.get('confidence_score', 'Error') * 100:.2f}%")
        pii_status = "Yes" if result.get('contains_pii') else "No"
        self.pii_text.set(f"Contains PII: {pii_status}")
        self.status_text.set("Classification complete.")

    def show_error(self, error_message):
        """Shows an error message in the status bar and a popup."""
        self.status_text.set(f"Error: {error_message}")
        messagebox.showerror("Error", f"An unexpected error occurred: {error_message}")

    def reset_ui_state(self):
        """Resets the button to an active state."""
        self.classify_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketClassifierApp(root)
    root.mainloop()
