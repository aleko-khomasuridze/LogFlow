# Logflow - Python

[<img src="https://img.shields.io/badge/Version-1.0.0-blue">](#)
[<img src="https://img.shields.io/badge/Status-Stable-brightgreen">](#)
[<img src="https://img.shields.io/badge/Python-3.11-brightgreen">](#)

A simple yet elegant logging library for your `python` apps.

## Table of Contents

1. [Overview](#overview)
2. [Specs](#specs)

   * [Logging](#logging)
   * [Configuration](#configuration)
3. [Setup](#setup)

   * [Installation](#installation)
   * [Check (optional)](#check-optional)
4. [Simple Example](#simple-example)

   * [Basic Setup](#basic-setup)
   * [Code](#code)
   * [Output](#output)
5. [Logger Configuration](#logger-configuration)

   * [DateTime Format Configuration](#datetime-format-configuration)
   * [Example Code](#example-code)
   * [Example Output](#example-output)
   * [Summary](#summary)
6. [Custom Handler Implementation and Integration](#custom-handler-implementation-and-integration)

   * [Example Code](#example-code-1)
   * [Example Output](#example-output-1)
   * [Explanation](#explanation)
   * [Summary](#summary-1)
7. [Logflow Configuration](#logflow-configuration)
8. [Author & Contributions](#author--contributions)

## Overview

**LogFlow** is a lightweight yet powerful logging library for Python applications, designed to provide flexibility, readability, and modularity out of the box.
It simplifies how developers handle log generation, formatting, and output destinations — whether to the console, file system, or a custom handler such as a database or remote service.

With LogFlow, you can:

* Create structured, color-coded, and human-readable logs.
* Configure date and time formats with built-in or custom masks.
* Add or disable handlers dynamically at runtime.
* Extend the logging pipeline with your own formatters and handlers.
* Maintain consistency and clarity across small scripts or large-scale systems.

The library’s modular design allows developers to easily integrate it into existing codebases while maintaining full control over configuration and output behavior.

## Specs

### Logging

* **`console`** – colorful and elegant log format for the terminal.
* **`file`** – stashing and persistence of logs on your system with organization by date.
* **`database`** – custom logging that allows you to save your logs in a database for remote access and optimized search.

### Configuration

* **`datetime mask`** – you have a variety of standard datetime/timestamp masks to choose from.
* **`custom handlers`** – you can implement and add your own custom handlers to the logger’s handler list using our `Handler` interface/abstract class.
* **`logging file path config`** – configurable logging file path in `LogConfig`.


## Simple Example

A quick demo of `logflow`.

### Basic setup

Bare minimum code for setting up and running Logflow

#### Code

```python
from logflow import *

logger: Logger = Logger()

def main() -> None:
    logger.log(Log(LogType.DEBUG), 'some test message')

if __name__ == '__main__':
    main()
```

#### Output

```bash
[Debug]-[2025-10-24T10:22:43]: some test message
```