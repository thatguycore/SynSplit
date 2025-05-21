import os
import sys

def syn_split():
    # Look for files containing "Synergism"
    matching_files = [f for f in os.listdir('.') if os.path.isfile(f) and "Synergism" in f]

    if not matching_files:
        print("❌ Error: No save file found in the directory containing the word 'Synergism'.")
        input("\nPress Enter to close...")
        sys.exit(1)

    elif len(matching_files) == 1:
        input_path = matching_files[0]
        print(f"✅ Found save file: {input_path}")

    else:
        print("⚠️ Multiple save files found:")
        for i, file in enumerate(matching_files, start=1):
            print(f"  {i}. {file}")
        
        try:
            choice = int(input("Enter the number of the file to use: "))
            if not (1 <= choice <= len(matching_files)):
                raise ValueError
            input_path = matching_files[choice - 1]
        except ValueError:
            print("❌ Invalid selection. Exiting.")
            input("\nPress Enter to close...")
            sys.exit(1)

    # Process the selected file
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read()

    total_length = len(data)
    chunk_size = total_length // 3

    chunks = [
        data[:chunk_size],
        data[chunk_size:2 * chunk_size],
        data[2 * chunk_size:]
    ]

    for i, chunk in enumerate(chunks, start=1):
        with open(f'box_{i}.txt', 'w', encoding='utf-8') as out:
            out.write(chunk)

    print("\n✅ Data successfully split into box_1.txt, box_2.txt, and box_3.txt")
    input("\nPress Enter to close...")

# Usage
syn_split()
