
import os

def read_file_safely():
    """Prompt user for a filename, read it, and display stats and preview."""
    
    while True:
        try:
            # Ask user for filename
            fname = input("\nEnter a file name (or type 'exit' to quit): ").strip()
            
            # Exit condition
            if fname.lower() == "exit":
                print("👍 Exiting program. Have a great day!")
                break
            
            if not fname:
                print("⚠️  You must type something!")
                continue
            
            # If file not found
            if not os.path.isfile(fname):
                print(f"❌ File '{fname}' not found.")
                
                # Show available files in current folder
                available = [f for f in os.listdir('.') if os.path.isfile(f)]
                if available:
                    print("📌 Available files in this folder:")
                    for f in available[:5]:  # show only first 5
                        print("   -", f)
                continue
            
            # Open and read file
            with open(fname, "r", encoding="utf-8") as f:
                text = f.read()
            
            # Show stats
            print(f"\n✅ File '{fname}' opened successfully!")
            print(f"   Characters: {len(text)}")
            print(f"   Words: {len(text.split())}")
            print(f"   Lines: {len(text.splitlines())}")
            
            # Display preview
            print("\n📖 Preview of content:")
            for i, line in enumerate(text.splitlines()[:3], 1):
                print(f"   {i}. {line}")
            if len(text.splitlines()) > 3:
                print("   ... (content truncated) ...")
            
        except PermissionError:
            print(f"🚫 No permission to read '{fname}'.")
        except UnicodeDecodeError:
            print(f"⚠️  File '{fname}' might not be a text file.")
        except KeyboardInterrupt:
            print("\n⏹️  Program stopped by user.")
            break
        except Exception as e:
            print(f"❓ Unexpected error: {e}")

def make_sample_files():
    """Create some sample files automatically"""
    samples = {
        "hello.txt": "Hello there!\nThis is a demo file.",
        "data.txt": "Python makes file handling easy.\nLine 2.\nLine 3.",
        "emptyfile.txt": "",
        "list.txt": "\n".join([f"Item {i}" for i in range(1, 6)])
    }
    for name, content in samples.items():
        with open(name, "w") as f:
            f.write(content)
    print("📂 Sample files created:", ", ".join(samples.keys()))

if __name__ == "__main__":
    print("==== File Handling & Error Management ====")
    make_sample_files()
    read_file_safely()
