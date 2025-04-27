import google.generativeai as genai
import subprocess
import re
import os
import dotenv 
# Load environment variables from a .env file if it exists
dotenv.load_dotenv()

# Configure the Gemini API key
# It's recommended to set this as an environment variable or in a .env file
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    print("Please ensure you have a .env file in the same directory with GOOGLE_API_KEY='YOUR_API_KEY'")
    print("or set the environment variable directly.")
    exit(1)

def generate_script_with_gemini(user_input):
    """
    Generates a shell script using the Gemini API based on user input.

    Args:
        user_input (str): The task description provided by the user.

    Returns:
        str: The generated shell script content, or None if generation fails.
    """
    # Define the model
    model = genai.GenerativeModel('gemini-1.5-flash-latest') # Or 'you can try any latest and old accrding to result'

    prompt = f"Write a valid .sh script (only the file content, no extra explanation) that performs the following task:\nTask: '{user_input}'\nMake sure the script is correct and executable directly. Provide only the script content within a markdown code block."

    try:
        # Generate content using the model
        response = model.generate_content(prompt)

        # Extract the text content from the response
        content = response.text

        # Use regex to extract the script content from the markdown code block
        # This handles cases where the model might include the ```sh ``` wrapper
        match = re.search(r"```(?:sh)?\s*(.*?)```", content, re.DOTALL)
        if match:
            script_content = match.group(1).strip()
        else:
            # If no markdown block is found, assume the whole content is the script
            script_content = content.strip()

        return script_content

    except Exception as e:
        print(f"An error occurred during Gemini API call: {e}")
        return None


def save_and_run_script(script_content):
    """
    Saves the script content to a file, makes it executable, and runs it.

    Args:
        script_content (str): The content of the shell script.
    """
    if not script_content:
        print("No script content to save and run.")
        return

    script_filename = "generated_script.sh" # Use a more descriptive name

    try:
        # Save the script content to a file
        with open(script_filename, "w") as f:
            f.write(script_content)
        print(f"Script saved as {script_filename}")

        # Make the script executable
        subprocess.run(["chmod", "+x", script_filename], check=True)
        print(f"Made {script_filename} executable.")

        # Run the script and capture stdout and stderr
        term_output_filename = "term_out.txt"
        with open(term_output_filename, "w") as out_file:
            print(f"Running {script_filename} and capturing output to {term_output_filename}...")
            # Use run with capture_output=True and text=True for easier handling
            # Or keep the file writing approach
            subprocess.run([f"./{script_filename}"], stdout=out_file, stderr=subprocess.STDOUT, check=True)
        print(f"Script finished. Output captured in {term_output_filename}")

    except FileNotFoundError:
        print(f"Error: Could not find the script file {script_filename}.")
    except PermissionError:
        print(f"Error: Permission denied to execute {script_filename}. Make sure you have execute permissions.")
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
        # Optionally read and print the output file content on error
        try:
            with open(term_output_filename, "r") as out_file:
                print("\n--- Script Output (on error) ---")
                print(out_file.read())
                print("-------------------------------")
        except FileNotFoundError:
             pass # Ignore if output file wasn't created
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Main Execution ---
if __name__ == "__main__":
    user_input = input("Enter Your Task for the shell script: ")

    # Generate the script using Gemini
    generated_script = generate_script_with_gemini(user_input)

    if generated_script:
        print("\n--- Generated Script ---")
        print(generated_script)
        print("------------------------\n")

        # Save and run the generated script
        save_and_run_script(generated_script)
    else:
        print("Failed to generate script.")
