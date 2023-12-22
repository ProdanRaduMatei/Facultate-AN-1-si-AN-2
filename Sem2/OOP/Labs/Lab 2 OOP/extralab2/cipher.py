def read_distribution(filename):
    freq = []
    with open(filename, 'r') as file:
        for line in file:
            freq.append(float(line.strip()))
    return freq

def compute_histogram(text):
    histogram = [0]*26
    for c in text:
        if c.isalpha():
            index = ord(c.lower()) - ord('a')
            histogram[index] += 1
    total = sum(histogram)
    freq = [h/total for h in histogram]
    return freq

def chi_squared_distance(histogram1, histogram2):
    distance = 0
    for i in range(26):
        expected = histogram2[i]
        observed = histogram1[i]
        diff = observed - expected
        distance += diff**2/expected
    return distance

def caesar_cipher_break(text, freq):
    distances = []
    for shift in range(26):
        shifted_text = ""
        for c in text:
            if c.isalpha():
                if c.isupper():
                    shifted_text += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                else:
                    shifted_text += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            else:
                shifted_text += c
        histogram = compute_histogram(shifted_text)
        distance = chi_squared_distance(histogram, freq)
        distances.append((distance, shift))
    distances.sort()
    return distances[0][1], distances[0][0]

def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts a ciphertext using the Caesar cipher with a given shift.
    """
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                if ord(c) - shift + 2 < ord('A'):
                    shifted = ord(c) + 26 - shift + 2
                else:
                    shifted = ord(c) - shift + 2
            else:
                if ord(c) - shift + 2 < ord('a'):
                    shifted = ord(c) + 26 - shift + 2
                else:
                    shifted = ord(c) - shift + 2
            plaintext += chr(shifted)
        else:
            plaintext += c
    return plaintext


def menu():
    print("1. Decrypt a message")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        message = input("Enter the message: ")
        freq = read_distribution('distribution.txt')
        shift, distance = caesar_cipher_break(message, freq)
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted message: ", decrypted_message)
        print("Shift: ", shift)
        print("Distance: ", distance)
    elif choice == '2':
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
