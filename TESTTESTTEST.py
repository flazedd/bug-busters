import os
import subprocess

os.environ['PYNGUIN_DANGER_AWARE'] = 'true'
# Define the command and its arguments
command = [
    '.\\venv\\Scripts\\pynguin.exe',
    '--project-path', 'PythonPUT/codetiming',
    '--module-name', 'timers',
    '--output-path', 'PythonPUT/codetiming',
    '--assertion-generation', 'SIMPLE',
    '--algorithm', 'DYNAMOSA',
    '--maximum-search-time', '30'
]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the output and error (if any)
print("Output:")
print(result.stdout)
print("Error:")
print(result.stderr)
