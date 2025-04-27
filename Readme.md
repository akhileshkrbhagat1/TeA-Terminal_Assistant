# Shell Script Generator Using Gemini API

This project provides a tool to generate, save, and execute shell scripts based on user input using the **Google Gemini API**. The user provides a description of the task, and the program generates a corresponding shell script, saves it, makes it executable, and runs it. If any errors occur during execution, the output is captured and can be reviewed for debugging.

## Features

- Generate shell scripts based on user-defined tasks.
- Make the generated script executable.
- Run the script and capture the output (including errors).
- Error handling and debugging support.

## Prerequisites

Before using this tool, make sure you have the following installed on your system:

- Python 3.6 or later.
- Google Gemini API credentials.
- Required Python libraries (listed below).

### Python Libraries

This project requires the following Python libraries:

- `google-generativeai` – for interacting with the Gemini API.
- `python-dotenv` – for loading environment variables from a `.env` file.
- `subprocess` – for running shell commands.

You can install the required libraries using the following:

```bash
pip install google-generativeai python-dotenv

Setup

    Clone the repository:

git clone https://github.com/your-username/shell-script-generator.git
cd shell-script-generator

Create a .env file in the project root:

The .env file should contain your Google API key in the following format:

GOOGLE_API_KEY=your-google-api-key

Replace your-google-api-key with the actual API key from Google Gemini.

Install dependencies:

Ensure you have Python 3.6+ installed and then install the required libraries:

    pip install -r requirements.txt

Usage

    Run the Python script:

    After setting up the .env file, you can run the script as follows:

python generate_script.py

The program will prompt you to enter a task description for which the shell script needs to be generated.

Provide the task description:

When prompted, enter a description of the task you want to automate with the shell script. For example:

    Enter Your Task for the shell script: Create a backup of all .txt files in the directory

    The program will:

        Generate a shell script using the Google Gemini API.

        Save the script as generated_script.sh.

        Make it executable.

        Run it, and capture the output in term_out.txt.

    Check the output:

    After execution, you can check the captured output in the term_out.txt file for debugging or verification of script execution.

Example
User Input:

Enter Your Task for the shell script: Backup all files with a .txt extension in the current directory

Generated Script Example:

#!/bin/bash
# This script backs up all .txt files in the current directory to a backup folder

backup_dir="backup"
mkdir -p "$backup_dir"

# Find and copy all .txt files to the backup directory
find . -type f -name "*.txt" -exec cp {} "$backup_dir" \;

echo "Backup completed successfully."

Output in term_out.txt:

Backup completed successfully.

Contributing

We welcome contributions! If you have any suggestions or improvements, please feel free to fork this repository and submit a pull request.
Steps to Contribute:

    Fork the repository.

    Create a new branch for your changes.

    Make your changes.

    Run tests and ensure the code works as expected.

    Submit a pull request.

License

This project is licensed under the MIT License – see the LICENSE file for details.
Author

    Akhilesh