import os
import subprocess
import argparse
import shlex

def ensure_output_dir(file):
    base_name = os.path.basename(file)
    name_no_ext = os.path.splitext(base_name)[0]
    output_dir = os.path.join("outputs", name_no_ext)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def run_command(command, output_file):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        with open(output_file, "w") as f:
            if result.stdout:
                f.write(result.stdout)
            if result.stderr:
                f.write("\n[ERROR] " + result.stderr)
        print(f"[+] Output saved to {output_file}")
    except Exception as e:
        with open(output_file, "w") as f:
            f.write(f"[ERROR] {e}")
        print(f"[ERROR] Failed to run command: {command}")

def steghide_extract(file, password, out_dir):
    print("[+] Trying Steghide...")
    output_file = os.path.join(out_dir, "steghide.txt")
    run_command(f"steghide extract -sf {shlex.quote(file)} -p {shlex.quote(password)} -f", output_file)

def zsteg_scan(file, out_dir):
    print("[+] Running Zsteg on PNG file...")
    output_file = os.path.join(out_dir, "zsteg.txt")
    run_command(f"zsteg {shlex.quote(file)}", output_file)

def stegcracker_bruteforce(file, wordlist, out_dir):
    print("[+] Running StegCracker...")
    output_file = os.path.join(out_dir, "stegcracker.txt")
    run_command(f"stegcracker {shlex.quote(file)} {shlex.quote(wordlist)}", output_file)

def binwalk_extract(file, out_dir):
    print("[+] Running Binwalk to extract hidden files...")
    output_file = os.path.join(out_dir, "binwalk.txt")
    run_command(f"binwalk --extract --verbose {shlex.quote(file)}", output_file)

def exiftool_metadata(file, out_dir):
    print("[+] Extracting Metadata with ExifTool...")
    output_file = os.path.join(out_dir, "exiftool.txt")
    run_command(f"exiftool {shlex.quote(file)}", output_file)

def main():
    parser = argparse.ArgumentParser(description="Steganography Solver")
    parser.add_argument("file", help="Path to the file")
    parser.add_argument("-p", "--password", default="", help="Password for steghide (if known)")
    parser.add_argument("-w", "--wordlist", help="Wordlist for stegcracker (optional)")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("[ERROR] File not found!")
        return

    output_dir = ensure_output_dir(args.file)

    if args.file.lower().endswith(".png"):
        zsteg_scan(args.file, output_dir)

    steghide_extract(args.file, args.password, output_dir)

    if args.wordlist:
        stegcracker_bruteforce(args.file, args.wordlist, output_dir)

    binwalk_extract(args.file, output_dir)

    exiftool_metadata(args.file, output_dir)

if __name__ == "__main__":
    main()

