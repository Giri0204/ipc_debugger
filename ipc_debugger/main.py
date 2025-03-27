from debugger_interface import IPCDebugger
from data_visualization import visualize_ipc

def main():
    debugger = IPCDebugger()

    while True:
        print("\nIPC Debugger Menu:")
        print("1. Start Debugging")
        print("2. Stop Debugging")
        print("3. Show Status")
        print("4. Visualize IPC Flow")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            debugger.start_debugging()
        elif choice == "2":
            debugger.stop_debugging()
        elif choice == "3":
            debugger.display_status()
        elif choice == "4":
            visualize_ipc()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()