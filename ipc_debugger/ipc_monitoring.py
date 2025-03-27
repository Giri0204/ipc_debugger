import tkinter as tk from tkinter 
import ttk from threading import Thread import time   
  def __init__(self, root): 

        self.root = root        
 self.root.title("Gayatri Timer")        
 self.root.geometry("400x300")         
self.root.resizable(False, False) 
        self.root.configure(bg="#2C2F33") 
 # Dark theme        
 self.running = False      
   self.counter = 0       
  self.reminder_time = 0    
     # Timer Label        
 self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48, "bold"), fg="#FFFFFF", bg="#2C2F33") 
        self.label.grid(row=0, column=0, columnspan=3, pady=10) 
        # Buttons with styling 
        self.start_button = ttk.Button(root, text="Start", command=self.start, style="TButton")         self.start_button.grid(row=1, column=0, padx=10, pady=10)      
   self.stop_button = ttk.Button(root, text="Stop", command=self.stop, style="TButton") 
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)       
  self.reset_button = ttk.Button(root, text="Reset", command=self.reset, style="TButton") 
        self.reset_button.grid(row=1, column=2, padx=10, pady=10) 

        # Reminder Input 
        self.reminder_entry = ttk.Entry(root, font=("Helvetica", 12))         self.reminder_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew") 
        self.reminder_button = ttk.Button(root, text="Set Reminder", command=self.set_reminder, style="TButton") 
        self.reminder_button.grid(row=2, column=2, padx=10, pady=10) 
 
        # Reminder Message 
        self.reminder_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#FF5555", bg="#2C2F33") 
        self.reminder_label.grid(row=3, column=0, columnspan=3, pady=5) 

        # Apply style         self.style = ttk.Style() 
        self.style.configure("TButton", font=("Helvetica", 12), padding=5)         self.style.map("TButton", background=[("active", "#7289DA")])     def update_label(self):         while self.running:             time.sleep(1)             self.counter += 1             minutes, seconds = divmod(self.counter, 60)             hours, minutes = divmod(minutes, 60) 
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}" 
            self.label.config(text=time_str)             if self.counter == self.reminder_time:                 self.reminder_label.config(text="Reminder: " + self.reminder_entry.get())             self.root.update()     def start(self): 
        if not self.running:             self.running = True 
            self.thread = Thread(target=self.update_label, daemon=True)             self.thread.start() 
 
    def stop(self): 
        self.running = False     def reset(self):         self.running = False         self.counter = 0         self.label.config(text="00:00:00")         self.reminder_label.config(text="")     def set_reminder(self):         try: 
            reminder = int(self.reminder_entry.get())             self.reminder_time = self.counter + reminder         except ValueError:             self.reminder_label.config(text="Invalid input! Enter seconds.") 
# Run the application root = tk.Tk() stopwatch = Stopwatch(root) root.mainloop() 

 
 
