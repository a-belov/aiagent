import os
import subprocess


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs the Python file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file we need to run",
                },
                "args": {
                    "type": "array",
                    "description": "Optional parameters of the Python file",
                },
            },
        },
    },
}


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(args)

        proc = subprocess.run(command, capture_output=True, timeout=30, text=True)

        output = str()

        if proc.returncode:
            output += f"Process exited with code {proc.returncode}"
        
        if (proc.stderr or proc.stdout):
            output += f"STDOUT: {proc.stdout}\nSTDERR: {proc.stderr}\n"
        else:
            output += " No output produced"

        return output

    except BaseException as e:
        return f"Error: executing Python file: {e}"