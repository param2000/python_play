import re

text = """
/// <summary>
/// This is a multi-line
/// summary for a function.
/// </summary>
"""

pattern = r"<summary>(.*?)</summary>"
matches = re.findall(pattern, text, re.DOTALL)

# Flatten results by removing leading/trailing whitespace and newlines
summaries = [match.strip() for match in matches]

print(summaries)