"""
Long Python Script: Toolkit Demonstration

This script includes:
- Text utilities
- Math utilities
- Web scraping
- File handling
- Data analysis with pandas
- Visualization with matplotlib

Author: OpenAI Demo
"""

import math
import random
import string
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------- TEXT UTILITIES ----------------------
def generate_random_string_0(length=10): return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def generate_random_string_1(length=10): return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def generate_random_string_2(length=10): return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# ... repeated up to:
def generate_random_string_149(length=10): return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ---------------------- MATH UTILITIES ----------------------
def fibonacci_0(n): a, b = 0, 1; [a := b, b := a + b for _ in range(n)]; return a
def fibonacci_1(n): a, b = 0, 1; [a := b, b := a + b for _ in range(n)]; return a
def fibonacci_2(n): a, b = 0, 1; [a := b, b := a + b for _ in range(n)]; return a
# ... repeated up to:
def fibonacci_149(n): a, b = 0, 1; [a := b, b := a + b for _ in range(n)]; return a

# ---------------------- WEB SCRAPING ----------------------
def scrape_hackernews_titles():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [a.text for a in soup.find_all('a') if a.text.strip()]
    return titles[:30]

# ---------------------- FILE HANDLING ----------------------
def save_text_file_0(filename, content): with open(filename, 'w') as f: f.write(content)
def save_text_file_1(filename, content): with open(filename, 'w') as f: f.write(content)
# ... repeated up to:
def save_text_file_99(filename, content): with open(filename, 'w') as f: f.write(content)

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

if __name__ == "__main__":
    main()
