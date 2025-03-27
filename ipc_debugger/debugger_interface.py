from ipc_monitoring import monitor_ipc

class IPCDebugger:
    def _init_(self):
        self.is_running = False

    def start_debugging(self):
        if not self.is_running:
            print("Starting IPC Debugger...")
            self.is_running = True
            monitor_ipc()
        else:
            print("Debugger is already running.")

    def stop_debugging(self):
        if self.is_running:
            print("Stopping IPC Debugger...")
            self.is_running = False
        else:
            print("Debugger is not running.")

    def display_status(self):
        if self.is_running:
            print("IPC Debugger is running.")
        else:
            print("IPC Debugger is stopped.")

if _name_ == "_main_":
    debugger = IPCDebugger()

    while True:
        print("\nIPC Debugger Menu:")
        print("1. Start Debugging")
        print("2. Stop Debugging")
        print("3. Show Status")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            debugger.start_debugging()
        elif choice == "2":
            debugger.stop_debugging()
        elif choice == "3":
            debugger.display_status()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")