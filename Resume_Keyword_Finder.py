# Define the keywords to look for
keywords = ['Python', 'Java', 'JavaScript', 'SQL', 'HTML', 'CSS']

# Get the resume text from a file or user input
resume = input("Enter the text of your resume: ")

# Convert the resume text to lowercase for case-insensitive matching
resume = resume.lower()

# Initialize a dictionary to store the keyword counts
counts = {keyword: 0 for keyword in keywords}

# Count the number of times each keyword appears in the resume
for keyword in keywords:
    counts[keyword] = resume.count(keyword.lower())

# Print the results
print("Resume analysis:")
for keyword, count in counts.items():
    print(keyword + ':', count)