# Fast-File-Finder
Developed a Python utility for recursively searching Windows filesystems to locate specified files and directories. Designed as a foundation for future forensic capabilities, including artifact discovery, signature matching, and automated evidence collection.

Disclaimer: This is not yet a finished product and will be expanded and debugged in the near future.

# Folder_Finder.py

## Project Overview

Folder_Finder is a Python command-line utility designed to automate the process of locating files or folders within a Windows system. Instead of manually navigating through directories, the tool recursively searches a user-specified directory and returns the full path to the requested file or folder when found.

This project was created to strengthen Python programming fundamentals while exploring filesystem traversal and command-line automation.

---

# Objective

The goal of this project was to create a lightweight utility capable of recursively searching a filesystem for a specified file or directory.

Primary objectives included:

* Automating repetitive file searches.
* Practicing Python filesystem operations.
* Improving familiarity with command-line application development.
* Building experience with reusable functions and program flow.

---

# Environment

**Language**

* Python 3

**Operating System**

* Microsoft Windows

**Libraries Used**

* `os`
* `sys`
* `time`

No third-party libraries were required.

---

# Technical Implementation

The application operates entirely from the command line.

### User Input

The user provides:

* The exact name of a file or folder
* A starting directory for the search

If no directory is specified, the program defaults to searching the Windows root directory (`C:\`).

### Filesystem Traversal

The script recursively traverses the filesystem using Python's `os.walk()` function.

During each iteration, it checks:

* Current directories
* Current files

If a matching object is discovered, the program immediately returns its absolute path.

### User Feedback

To improve usability, an animated loading indicator is displayed while the filesystem is being searched. Although simple, this demonstrates interaction with standard output and dynamic console updates.

### Search Completion

If a matching item is located, the full filesystem path is displayed.

If no matching item exists within the selected search scope, the user is notified that the search completed without finding the requested object.

---

# Skills Demonstrated

* Python programming
* Filesystem traversal
* Recursive directory searching
* Command-line application development
* Function design
* User input validation
* Program flow and control structures
* Basic automation

---

# Challenges

Searching an entire filesystem can require traversing thousands of directories. This project required understanding how recursive directory walking functions operate while keeping the implementation simple and easy to follow.

Another consideration was providing user feedback during longer searches through the implementation of a console loading animation.

---

# Potential Improvements

Future versions of the application could include:

* Partial filename matching
* Wildcard support
* Regular expression searching
* Case-insensitive searches
* File size and creation date filtering
* Multi-threaded searching for improved performance
* Search logging
* Exporting results to CSV or JSON
* Exception handling for inaccessible directories
* Progress reporting during long searches

---

# Security Relevance

While this project is not an offensive or defensive cybersecurity tool, it demonstrates several concepts applicable to security operations and system administration.

Examples include:

* Automated filesystem enumeration
* Recursive directory traversal
* Command-line scripting
* Windows filesystem familiarity
* Automation of repetitive administrative tasks

These skills form a foundation for more advanced security tooling used during incident response, digital forensics, and endpoint investigations.

---

# Lessons Learned

This project reinforced the importance of modular programming by separating the search functionality from the user interface. It also provided practical experience working with Python's filesystem libraries and demonstrated how small automation utilities can simplify repetitive administrative tasks.

Future iterations would focus on improving performance, expanding search capabilities, and adding stronger error handling to better support real-world environments.
