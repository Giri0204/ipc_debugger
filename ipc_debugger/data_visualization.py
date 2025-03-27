def visualize_ipc():
    print("\nIPC Visualization:")
    print("Message flow between Sender and Receiver:")
    for i in range(1, 6):
        print(f"Sender -> Message {i}")
        print(f"Receiver <- Message {i}")