# Python File Sorter

A simple Python utility that automatically organizes files into categorized folders based on their extensions.

## About

This project was created to practice Python scripting, filesystem operations, and task automation.

The application supports both manual sorting of existing files and automatic monitoring of selected directories for newly created files.

## Features

- **Manual Sorting** - Organizes existing files in a directory provided through a command-line argument
- **Automatic Sorting** - Monitors the Downloads and Desktop directories for newly created files
- **Windows Context Menu Integration** - Allows users to organize files directly from the Windows right-click menu after configuring a registry entry
- **File Categorization** - Sorts files into predefined categories based on their extensions
- **Automatic Folder Creation** - Creates destination folders when needed
- **Fallback Category** - Moves unrecognized file types into an Others folder

## File Categories

*screen*

## Technologies

- Python
- pathlib
- shutil
- watchdog

## How It Works

The application supports two independent modes:

#### Manual Mode

Scans a specified directory and organizes existing files into categorized subfolder

#### Automatic Mode

Monitors the Downloads and Desktop directories using watchdog. When a new file is detected, it is moved into the appropriate category folder.

Both modes use the same sorting function to categorize and move files.

## Status

**Functional Utility Project** - A small Python automation tool with manual and automatic file organization.

## Potential Improvements

- Configurable directories and file categories
- Improved handling of files still being downloaded
- Filename conflict handling
- Logging and error handling
