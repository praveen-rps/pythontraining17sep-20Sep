import sys
import os

# 1. Get the Python version
print("Python version:", sys.version)

# 2. Get the Python executable path
print("Python executable path:", sys.executable)

# 3. Get the platform
print("Platform:", sys.platform)

# 4. Get the maximum size of an integer
print("Max size of an integer:", sys.maxsize)

# 5. Get the system’s byte order (little-endian or big-endian)
print("System byte order:", sys.byteorder)

# 6. Get the arguments passed to the script (including the script name itself)
print("Command-line arguments:", sys.argv)

# 7. Set the default encoding (used for string operations)
print("Default encoding:", sys.getdefaultencoding())

# 8. Get the system-specific line separator
print("Line separator:", repr(sys.platform))

# 9. Get the recursion limit (maximum depth of the Python interpreter stack)
print("Recursion limit:", sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print("New recursion limit set to:", sys.getrecursionlimit())

# 11. Get the current stdin, stdout, stderr streams
print("Standard input (stdin) is:", sys.stdin)
print("Standard output (stdout) is:", sys.stdout)
print("Standard error (stderr) is:", sys.stderr)

print("File system encoding:", sys.getfilesystemencoding())

# 12. Get the modules loaded by the Python interpreter
print("Modules loaded:", sys.modules.keys())

# 13. Check if a path exists in the sys.path (for module search)
print("Is '/usr/lib' in sys.path?", '/usr/lib' in sys.path)

# 14. Get the path to the site-packages directory
print("Site-packages path:", sys.prefix)

# 15. Get the current system-specific file system encoding
print("File system encoding:", sys.getfilesystemencoding())