"""
Long Python Script: Toolkit Demonstration

This script includes:
- Text utilities
- Math utilities
- Web scraping
- File handling
- Data analysis with pandas
- Visualization with matplotlib
- List sorting and searching
- Simple encryption utilities
- Class-based utilities

Author: OpenAI Demo
"""

import math
import random
import string
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import hashlib

# ---------------------- TEXT UTILITIES ----------------------
" +
        "
".join([f"def generate_random_string_{i}(length=10): return ''.join(random.choices(string.ascii_letters + string.digits, k=length))" for i in range(150)]) +
        "

# ---------------------- MATH UTILITIES ----------------------
" +
        "
".join([f"def fibonacci_{i}(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a" for i in range(150)]) +
        "

# ---------------------- WEB SCRAPING ----------------------
def scrape_hackernews_titles():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [a.text for a in soup.find_all('a') if a.text.strip()]
    return titles[:30]

# ---------------------- FILE HANDLING ----------------------
" +
        "
".join([f"def save_text_file_{i}(filename, content):
    with open(filename, 'w') as f:
        f.write(content)" for i in range(100)]) +
        "

# ---------------------- DATA ANALYSIS ----------------------
def create_sample_dataframe():
    data = {
        'Category': ['A', 'B', 'C', 'D'] * 25,
        'Value': [random.randint(10, 100) for _ in range(100)]
    }
    df = pd.DataFrame(data)
    return df

def plot_dataframe(df):
    summary = df.groupby('Category').sum()
    summary.plot(kind='bar')
    plt.title("Category-wise Sum")
    plt.tight_layout()
    plt.savefig("plot.png")

# ---------------------- STRING ANALYSIS ----------------------
def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

def count_consonants(s):
    return sum(1 for c in s.lower() if c.isalpha() and c not in 'aeiou')

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    return s == s[::-1]

# ---------------------- DATE UTILITIES ----------------------
" +
        "
".join([f"def get_current_datetime_{i}():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')" for i in range(50)]) +
        "

# ---------------------- LIST UTILITIES ----------------------
" +
        "
".join([f"def flatten_nested_list_{i}(nested):
    return [item for sublist in nested for item in sublist]" for i in range(50)]) +
        "

# ---------------------- ENCRYPTION UTILS ----------------------
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# ---------------------- SORTING & SEARCH ----------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ---------------------- DEMO CLASS ----------------------
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}! Welcome to PyTitan."

# ---------------------- MAIN FUNCTION ----------------------
def main():
    print("Fetching Hacker News Titles:")
    titles = scrape_hackernews_titles()
    for title in titles:
        print("-", title)

    print("\nGenerating DataFrame and Plotting...")
    df = create_sample_dataframe()
    plot_dataframe(df)
    print("Plot saved as plot.png")

    print("\nGenerating Random Strings:")
    for i in range(5):
        print(f"String {i}:", generate_random_string_0(12))

    print("\nCalculating Fibonacci:")
    for i in range(5):
        print(f"Fibonacci({i+5}) =", fibonacci_0(i+5))

    print("\nString Analysis Examples:")
    sample = "Level"
    print(f"Is '{sample}' a palindrome?", is_palindrome(sample))
    print(f"Reversed: {reverse_string(sample)}")
    print(f"Vowels: {count_vowels(sample)}")
    print(f"Consonants: {count_consonants(sample)}")

    print("\nDate Example:")
    print("Current datetime:", get_current_datetime_0())

    print("\nList Flatten Example:")
    print(flatten_nested_list_0([[1, 2], [3, 4], [5]]))

    print("\nEncryption Example:")
    print("SHA256 of 'hello':", sha256_hash('hello'))
    print("MD5 of 'hello':", md5_hash('hello'))

    print("\nSorting and Searching:")
    data = [5, 3, 8, 6, 2]
    sorted_data = bubble_sort(data)
    print("Sorted:", sorted_data)
    print("Search for 6 in sorted list:", binary_search(sorted_data, 6))

    print("\nGreeter Class Demo:")
    g = Greeter("Developer")
    print(g.greet())

if __name__ == "__main__":
    main()
