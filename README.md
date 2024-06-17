# markdown-to-json

![issues](https://img.shields.io/github/issues/Justin-Byrne/markdown-to-json)
![license](https://img.shields.io/github/license/Justin-Byrne/markdown-to-json)
<img src=https://img.shields.io/badge/Python-3.11.2-blue />
<img src=https://img.shields.io/badge/Version-0.0.0-green />
<img src=https://img.shields.io/github/languages/code-size/Justin-Byrne/markdown-to-json />

Markdown to JSON converter for jsdoc-to-markdown output

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Structure](#structure)

## Requirements

| Program | Function | Optional | Download |
| :---: | :--- | :---: | :---: |
| npm | Node package manager. | :x: | [:floppy_disk:](https://www.npmjs.com/) |
| jsdoc2md | JSDoc annotation to markdown | :x: | [:floppy_disk:](https://github.com/jsdoc2md/jsdoc-to-markdown) |

## Installation

Download a copy of this repository to your system.

> Git clone

```sh
git clone https://github.com/Justin-Byrne/markdown-to-json.git
```

## Usage

> Help menu

```
python3 md2json.py {<source>} [<destination>] [flags]

PATHS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

source:         Directory of JSDoc markdown file(s)

    usage:          "../jsdoc-to-markdown"

destination:    Directory of JSON output

    usage:          "../markdown-to-json"

FLAGS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

-h, --help  Display this help menu

    usage:          --help

```


## Support

Please [open an issue](https://github.com/Justin-Byrne/markdown-to-json/issues/new) for support.

## Structure

```
.
├── docs
│   ├── CHANGELOG.md
│   └── FUNDING.yml
├── source
│   └── app
│       ├── core
│       │   └── markdown2json.py
│       ├── utilities
│       │   ├── custom
│       │   │   ├── debug
│       │   │   │   └── view_arguments.py
│       │   │   └── validation
│       │   │       └── is_extension.py
│       │   ├── system
│       │   │   ├── file
│       │   │   │   ├── get_files.py
│       │   │   │   └── set_file.py
│       │   │   ├── validation
│       │   │   │   ├── is_directory.py
│       │   │   │   ├── is_file.py
│       │   │   │   └── is_flag.py
│       │   │   ├── get_commands.py
│       │   │   └── parse_commands.py
│       │   └── util.py
│       └── md2json.py
├── LICENSE.md
└── README.md
```
 
## Copyright

![Byrne-Systems](https://github.com/Justin-Byrne/markdown-to-json/blob/main/images/cube_sm.png)

== Byrne-Systems © 2024 - All rights reserved. ==
