from pathlib import Path
from code_analyzer.analyzer import analyze_source

def main():
    """Read the source file and display the analysis results."""

    print("Enter path to source file: ")
    fpath = input()
    path = Path(fpath)

    # Check that the file exists.
    if not path.exists():
        print(f"Error: File not found: {fpath}")
        return

    # Read the Python source code.
    source = path.read_text(encoding="utf-8")

    # Run the static code analyzer.
    result = analyze_source(source)

    # Display the results.
    print("\n========== CODE ANALYSIS ==========")

    print("\n--- Code Metrics ---")
    print(f"Lines:         {result.metrics.lines}")
    print(f"Blank lines:   {result.metrics.blank_lines}")
    print(f"Comments:      {result.metrics.comment_lines}")
    print(f"Functions:     {result.metrics.functions}")
    print(f"Classes:       {result.metrics.classes}")
    print(f"Imports:       {result.metrics.imports}")

    print("\n--- Complexity ---")
    for function, complexity in result.complexity.items():
        print(f"{function}: {complexity}")

    print("\n--- Unused Variables ---")
    if result.unused_variables:
        for variable in result.unused_variables:
            print(f"- {variable}")
    else:
        print("None")

    print("\n--- Duplicate Code ---")
    if result.duplicates:
        for first, second in result.duplicates:
            print(f"- {first} <-> {second}")
    else:
        print("None")

    print("\n--- Naming Violations ---")
    if result.naming_violations:
        for name in result.naming_violations:
            print(f"- {name}")
    else:
        print("None")

    print("\n===================================\n")


if __name__ == "__main__":
    main()