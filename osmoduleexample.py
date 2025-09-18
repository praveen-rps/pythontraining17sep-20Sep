import os

# 1. Current working directory
print("Current working directory:", os.getcwd())

# 2. Change the current working directory
os.chdir("..")  # Move one level up
print("Changed working directory:", os.getcwd())

# 3. List directory contents
print("Directory contents:", os.listdir("."))

# 4. Make a new directory
new_dir = "test_dir"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Created new directory: {new_dir}")

# 5. Rename the directory
new_dir_rename = "renamed_test_dir"
os.rename(new_dir, new_dir_rename)
print(f"Renamed directory to: {new_dir_rename}")

# 6. Remove a directory (will fail if directory is not empty)
try:
    os.rmdir(new_dir_rename)
    print(f"Removed directory: {new_dir_rename}")
except OSError as e:
    print(f"Error removing directory: {e}")

# 7. Check if a path exists
path_to_check = "some_file.txt"
print(f"Does '{path_to_check}' exist?", os.path.exists(path_to_check))

# 8. Create a file (open with write mode, will create the file if it doesn't exist)
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# 9. Check if a path is a file or directory
print(f"Is 'example.txt' a file?", os.path.isfile("example.txt"))
print(f"Is 'example.txt' a directory?", os.path.isdir("example.txt"))

# 10. Get file status
file_stat = os.stat("example.txt")
print(f"File stats for 'example.txt':")
print(f"  Size: {file_stat.st_size} bytes")
print(f"  Last modified: {file_stat.st_mtime}")

# 11. Get the process ID
print("Current process ID:", os.getpid())

# 12. Get the parent process ID
print("Parent process ID:", os.getppid())

# 13. System information (Unix-based systems)
try:
    print("System info:", os.uname())
except AttributeError:
    print("`os.uname()` is not available on this platform.")

# 14. Create a symbolic link
os.symlink("example.txt", "example_symlink.txt")
print("Created symbolic link 'example_symlink.txt' to 'example.txt'")

# 15. Remove a file
os.remove("example.txt")
print("Removed file 'example.txt'")

# 16. Create and remove a temporary file
temp_file = os.tmpfile()
print("Temporary file created:", temp_file)
# Note: This file is automatically deleted when closed.

# 17. Get environment variables
print("Home directory from environment:", os.environ.get("HOME"))

# 18. Set environment variable (works only for the current process)
os.environ["MY_VAR"] = "Some Value"
print("MY_VAR:", os.environ["MY_VAR"])

# 19. Check if a path is absolute
abs_path_check = "/usr/bin/python"
print(f"Is '{abs_path_check}' an absolute path?", os.path.isabs(abs_path_check))

# 20. Join paths
joined_path = os.path.join("usr", "bin", "python")
print("Joined path:", joined_path)

# 21. Split a path into head and tail
head, tail = os.path.split(joined_path)
print(f"Head: {head}, Tail: {tail}")

# 22. Get the basename of a file
basename = os.path.basename(joined_path)
print(f"Basename of '{joined_path}':", basename)

# 23. Get the dirname of a file
dirname = os.path.dirname(joined_path)
print(f"Dirname of '{joined_path}':", dirname)

# 24. Normalize a path
normalized_path = os.path.normpath("/usr//bin/../python")
print(f"Normalized path: {normalized_path}")

# 25. Check if a path is a symlink
print(f"Is 'example_symlink.txt' a symlink?", os.path.islink("example_symlink.txt"))

# 26. Get the current user
try:
    print("Current user:", os.getlogin())
except OSError:
    print("Unable to get the current user (possibly not available on this platform).")

# 27. Create a FIFO (named pipe)
fifo_name = "example_fifo"
if not os.path.exists(fifo_name):
    os.mkfifo(fifo_name)
    print(f"Created FIFO: {fifo_name}")

# 28. Get the number of CPUs
print("Number of CPUs:", os.cpu_count())

# 29. Get the system load average (Unix-based)
try:
    print("System load average:", os.getloadavg())
except AttributeError:
    print("`os.getloadavg()` is not available on this platform.")

# 30. Temporary file with `tempfile`
import tempfile
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    print(f"Created temporary file: {temp_file.name}")

# Clean up - remove created files
os.remove(fifo_name)
os.remove("example_symlink.txt")
os.remove(temp_file.name)
