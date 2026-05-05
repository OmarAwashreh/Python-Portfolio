# The Live DJ Queue Manager

is_running = True
playlist = []

while is_running:
    print("\n--- DJ Queue Menu ---")
    print("1) Welcome")
    print("2) Standard Add")
    print("3) VIP Insert")
    print("4) Play Next")
    print("5) Remove Specific Song")
    print("6) Replace Song at Index")
    print("7) Display Queue")
    print("8) Clear All")
    print("9) Exit")
    
    try:
        choice = int(input("\nEnter your choice (1-9): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        print("Welcome to the DJ Booth!")

    elif choice == 2:
        insert_song = input("Enter the song name: ").lower()
        if insert_song in playlist:
            print(f"WARNING: '{insert_song.title()}' is already in the queue. No duplicates allowed.")
        else:
            playlist.append(insert_song)
            print(f"Added '{insert_song.title()}' to the queue.")

    elif choice == 3:
        insert_song = input("Enter the VIP song name: ").lower()
        if insert_song in playlist:
            print(f"WARNING: '{insert_song.title()}' is already in the queue. No duplicates allowed.")
        else:
            # VIP goes straight to the front (index 0)
            playlist.insert(0, insert_song)
            print(f"VIP INSERT: '{insert_song.title()}' is now next!")

    elif choice == 4:
        # Prevent the empty pop crash
        if len(playlist) == 0:
            print("The queue is currently empty. Please add a song first.")
        else:
            current_song = playlist.pop(0)
            print(f"🎧 NOW PLAYING: {current_song.title()} 🎧")

    elif choice == 5:
        remove_song = input("Enter the song name to remove: ").lower()
        try:
            playlist.remove(remove_song)
            print(f"Removed '{remove_song.title()}' from the queue.")
        except ValueError:
            print(f"Error: '{remove_song.title()}' is not in the queue.")

    elif choice == 6:
        new_song = input("Enter the NEW song name: ").lower()
        
        # Check for duplicates before replacing
        if new_song in playlist:
            print(f"WARNING: '{new_song.title()}' is already in the queue.")
            continue
            
        try:
            # Note: Display shows 1-based indexing, but Python uses 0-based indexing under the hood.
            # To make it user friendly, we could ask for the display number and subtract 1.
            # But for this test, we are keeping it strictly to Python indexes as you wrote it.
            index = int(input("Enter the Python index number to replace: "))
            
            if 0 <= index < len(playlist):
                old_song = playlist[index]
                playlist[index] = new_song
                print(f"Replaced '{old_song.title()}' with '{new_song.title()}'.")
            else:
                print("Error: Index is out of range.")
        except ValueError:
            print("Invalid input. Index must be a number.")

    elif choice == 7:
        print("\n--- Current Queue ---")
        if len(playlist) == 0:
            print("The queue is empty.")
        else:
            # Counter moved outside the loop!
            count = 1
            for song in playlist:
                print(f"{count}. {song.title()}")
                count += 1

    elif choice == 8:
        playlist.clear()
        print("Queue has been wiped clean!")
        
    elif choice == 9:
        print("Shutting down the DJ Booth. Goodnight!")
        is_running = False
    
    else:
        print("Wrong Input. Please choose a number between 1 and 9.")
