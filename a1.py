import argparse
import secrets
import string

def generate_random_string(length, chars):
    return ''.join(secrets.choice(chars) for i in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random strings.")
    parser.add_argument("--alphanumeric", action="store_true", help="Include alphanumeric characters.")
    parser.add_argument("--symbols", action="store_true", help="Include symbols.")
    parser.add_argument("--lowercase", action="store_true", help="Include lowercase letters.")
    parser.add_argument("--uppercase", action="store_true", help="Include uppercase letters.")
    parser.add_argument("--digits", action="store_true", help="Include digits.")
    parser.add_argument("--length", type=int, default=16, help="Length of the string (default: 16)")
    parser.add_argument("--iterations", type=int, default=3, help="Number of strings to generate (default: 3)")

    args = parser.parse_args()

    chars = ""
    if args.alphanumeric:
        chars += string.ascii_letters + string.digits
    if args.symbols:
        chars += string.punctuation
    if args.lowercase:
        chars += string.ascii_lowercase
    if args.uppercase:
        chars += string.ascii_uppercase
    if args.digits:
        chars += string.digits

    if not chars:
        print("Error: At least one character set must be specified.")
        exit(1)

    for _ in range(args.iterations):
        print(generate_random_string(args.length, chars))
