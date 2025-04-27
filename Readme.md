TeA-Terminal_Assistant (Terminal Automation)
============================================

This project provides a tool to generate, save, and execute shell scripts based on user input using the **Google Gemini API**. The user provides a description of the task, and the program generates a corresponding shell script, saves it, makes it executable, and runs it. If any errors occur during execution, the output is captured and can be reviewed for debugging.

Features
--------

*   Generate shell scripts based on user-defined tasks.
    
*   Make the generated script executable.
    
*   Run the script and capture the output (including errors).
    
*   Error handling and debugging support.
    

Prerequisites
-------------

Before using this tool, make sure you have the following installed on your system:

*   Python 3.6 or later.
    
*   Google Gemini API credentials.
    
*   Required Python libraries (listed below).
    

### Python Libraries

This project requires the following Python libraries:

*   google-generativeai – for interacting with the Gemini API.
    
*   python-dotenv – for loading environment variables from a .env file.
    
*   subprocess – for running shell commands.
    

You can install the required libraries using the following:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install google-generativeai python-dotenv   `

Setup
-----

To set up the project and install all the required dependencies, follow the steps below.

### Automated Setup with setup.sh

To automate the setup process, you can use the provided setup.sh script. This will install dependencies, check for Python 3.6+, and prompt you to create a .env file.

1.  git clone https://github.com/your-username/shell-script-generator.gitcd shell-script-generator
    
2.  chmod +x setup.sh
    
3.  ./setup.sh
    

The script will perform the following tasks:

*   Check if Python 3.6+ is installed, and install it if necessary.
    
*   Install the required Python libraries (google-generativeai and python-dotenv).
    
*   Check for the presence of a .env file, and prompt you to create it if it's missing.
    

### Create a .env file:

The .env file should contain your Google API key in the following format:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   GOOGLE_API_KEY=your-google-api-key   `

Replace your-google-api-key with your actual Google API key.

### Install dependencies manually (if needed):

If you prefer to install dependencies manually, you can run the following commands:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install google-generativeai python-dotenv   `

Usage
-----

1.  After setting up the .env file, you can run the script as follows:python generate\_script.pyThe program will prompt you to enter a task description for which the shell script needs to be generated.
    
2.  When prompted, enter a description of the task you want to automate with the shell script. For example:Enter Your Task for the shell script: Create a backup of all .txt files in the directoryThe program will:
    
    *   Generate a shell script using the Google Gemini API.
        
    *   Save the script as generated\_script.sh.
        
    *   Make it executable.
        
    *   Run it, and capture the output in term\_out.txt.
        
3.  After execution, you can check the captured output in the term\_out.txt file for debugging or verification of script execution.
    

Example
-------

**User Input:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Enter Your Task for the shell script: Backup all files with a .txt extension in the current directory   `

**Generated Script Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   #!/bin/bash  # This script backs up all .txt files in the current directory to a backup folder  backup_dir="backup"  mkdir -p "$backup_dir"  # Find and copy all .txt files to the backup directory  find . -type f -name "*.txt" -exec cp {} "$backup_dir" \;  echo "Backup completed successfully."   `

**Output in term\_out.txt:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Backup completed successfully.   `

Contributing
------------

We welcome contributions! If you have any suggestions or improvements, please feel free to fork this repository and submit a pull request.

### Steps to Contribute:

1.  Fork the repository.
    
2.  Create a new branch for your changes.
    
3.  Make your changes.
    
4.  Run tests and ensure the code works as expected.
    
5.  Submit a pull request.
    

Author
------

krakhilesh_28
