# educause-meeting-mapper
Generating a Python script to visualize Educause annual meeting locations on a US map with Cartopy.

## Overview

The **Educause Meeting Mapper** script plots the locations of Educause annual meetings held from 1999 to 2024 on a detailed US map. It includes:

- Geographical visualization of meeting locations.
- Sequential arrows showing the order of venues.
- Annotations of meeting years and locations.
- Customizable output options for filenames and formats (PDF/PNG/JPG).

This project uses `Cartopy` for mapping and provides a flexible CLI interface for user-friendly interaction.

---

## Features

- **Visualize Educause Meetings:** Displays meeting locations with annotations and arrows connecting venues in sequence.
- **Custom Output:** Choose output file names and formats (`pdf`, `png`, or `jpg`).
- **Overwrite Protection:** The script prompts for confirmation before overwriting existing files.
- **Command-Line Interface:** Use `argparse` for ease of use and flexibility.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gptdialogues/educause-meeting-mapper.git
   cd educause-meeting-mapper
   ```

2. Install the required Python packages:
   ```bash
   pip install matplotlib cartopy
   ```

---

## Usage

### Command Line Arguments

Run the script with the following options:

| Argument       | Description                                    | Default                       |
|----------------|------------------------------------------------|-------------------------------|
| `--output` `-o`| Specify the output filename without extension. | `educause_meetings_map`       |
| `--format` `-f`| Choose the output format (`pdf`, `png`, `jpg`).| `pdf`                         |

### Example Prompts

#### Basic Usage
To generate a PDF map with the default filename:
```bash
python educause_meetings_map.py
```

#### Specify Output Filename and Format
To generate a PNG map with a custom filename:
```bash
python educause_meetings_map.py --output my_map --format png
```

#### Prevent Overwriting
If a file with the same name exists, the script will prompt:
```
File "educause_meetings_map.pdf" exists. Overwrite? (y/n):
```
- Type `y` to overwrite.
- Type `n` to cancel.

## License

This project is licensed under the MIT License.
