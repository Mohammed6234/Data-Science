# Reading the poem.txt file
with open('poem.txt', 'r') as file:
    poem_text = file.read()

# Preprocessing the text to remove special characters and convert to lowercase
import re
poem_text = re.sub(r'[^\w\s]', '', poem_text)
poem_text = poem_text.lower()

# Splitting the text into words
words_list = poem_text.split()

# Counting occurrences of each word
word_count = {}
for word in words_list:
    word_count[word] = word_count.get(word, 0) + 1

# Finding the maximum occurrence
max_occurrence = max(word_count.values())

# Finding the words with the maximum occurrence
words_with_max_occurrence = [word for word, count in word_count.items() if count == max_occurrence]

print("Words with maximum occurrence:", words_with_max_occurrence)
print("Maximum occurrence count:", max_occurrence)


import csv

def calculate_ratios(price, earnings_per_share, book_value):
    pe_ratio = price / earnings_per_share
    pb_ratio = price / book_value
    return pe_ratio, pb_ratio

# Reading stocks.csv and calculating ratios
with open('stocks.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Company Name', 'PE Ratio', 'PB Ratio']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        price = float(row['Price'])
        earnings_per_share = float(row['Earnings Per Share'])
        book_value = float(row['Book Value'])

        pe_ratio, pb_ratio = calculate_ratios(price, earnings_per_share, book_value)

        writer.writerow({
            'Company Name': row['Company Name'],
            'PE Ratio': f'{pe_ratio:.2f}',
            'PB Ratio': f'{pb_ratio:.2f}'
        })

print("Output.csv file has been created.")
