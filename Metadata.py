import re
import os
import datetime
import csv

def extract_function_metadata(code_snippet):
    """
    Extract metadata from a C# function.
    """
    metadata = {}

    # Regex to capture the summary
    summary_match = re.search(r"/// <summary>\s*(.*?)\s*</summary>", code_snippet, re.DOTALL)
    metadata['Summary'] = summary_match.group(1).strip() if summary_match else None

    # Regex to capture the return type
    #return_type_match = re.search(r"public\s+(\w+)\s+\w+\s*\(", code_snippet)
    #metadata['Return Type'] = return_type_match.group(1) if return_type_match else None

    # Regex to capture the function name
    function_name_match = re.search(r"public\s+\w+\s+(\w+)\s*\(", code_snippet)
    metadata['Function Name'] = function_name_match.group(1) if function_name_match else None

    # Regex to capture attributes (decorators)
    attributes_match = re.findall(r"^\s*\[([^\]]+)\]", code_snippet, re.MULTILINE)
    metadata['Decorators'] = attributes_match

    # Regex to capture return description
    #returns_match = re.search(r"/// <returns>\s*(.*?)\s*</returns>", code_snippet, re.DOTALL)
    #metadata['Returns'] = returns_match.group(1).strip() if returns_match else None

    # Regex to capture parameters
    #parameters_match = re.search(r"public\s+\w+\s+\w+\(([^)]*)\)", code_snippet)
    #parameters = parameters_match.group(1).strip() if parameters_match else None
    #metadata['Parameters'] = parameters.split(",") if parameters else []

    return metadata

def extract_functions_with_metadata(content):
    """
    Extract functions and their metadata from a C# file.
    """

    # Regex to match a function and its metadata
    function_pattern = re.compile(
        r"""
        (///\s*<summary>.*?</summary>\s*)?      # Match the summary
        (///\s*<returns>.*?</returns>\s*)?      # Match the returns description
        ((?:\[[^\]]+\]\s*)*)                    # Match attributes/decorators
        public\s+(\w+)\s+(\w+)\s*\(([^)]*)\)    # Match return type, name, and parameters
        """,
        re.MULTILINE | re.VERBOSE | re.DOTALL
    )

    results = []
    for match in function_pattern.findall(content):
        summary = match[0].strip() if match[0] else None
        returns = match[1].strip() if match[1] else None
        decorators = [d.strip() for d in match[2].split('\n') if d.strip()]
        return_type = match[3]
        function_name = match[4]
        parameters = [param.strip() for param in match[5].split(',') if param.strip()]

        results.append({
            'Function Name': function_name,
            'Summary': summary,
            'Decorators': decorators,
            'Return Type': return_type,
            'Parameters': parameters,
            'Returns': returns
        })

    return results

def print_split_functions_to_files(functions, output_dir="output"):
    """
    print and save to csv file
    """

    headers = ["Function Name", "Summary", "Decorators"]
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for i, f in enumerate(functions, start=1):
            function_name=(f"{f['Function Name']}")
            function_summary=(f"{f['Summary']}").replace("\n", "").replace("\r", "")
            function_decorator=(f"{', '.join(f['Decorators'])}")
            function_return_type=(f"{f['Return Type']}")
            function_param=(f"{', '.join(f['Parameters'])}")
            function_returns=(f"{f['Returns']}")

            writer.writerow([function_name, function_summary, function_decorator])

            print(f"Function Name: {f['Function Name']}")
            print (f"Summary: {f['Summary']}")
            print (f"Decorators: {', '.join(f['Decorators'])}")
            print (f"Return Type: {f['Return Type']}")
            print (f"Parameters: {', '.join(f['Parameters'])}")
            print (f"Returns: {f['Returns']}")
            print("\n")

    print(f"results saved to file {filename}")

file_path = "Controller.cs"
with open(file_path, 'r') as file:
    content = file.read()

metadata = extract_functions_with_metadata(content)

print_split_functions_to_files(metadata)