# Installation Guide for ZOAU Python Stubs

This guide provides step-by-step instructions for setting up the ZOAU Python
stubs for development.

## Quick Start

```bash
# Navigate to the stubs directory
cd /Users/fultonm/Documents/Development/zoau_stubs

# Install in editable mode
pip install -e .

# Verify installation
pip list | grep zoautil
```

You should see: `zoautil-py-stubs` in the output.

## Detailed Installation Steps

### 1. Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- VS Code with Python extension

### 2. Install the Stubs Package

The key is to install in **editable mode** using the `-e` flag:

```bash
cd /Users/fultonm/Documents/Development/zoau_stubs
pip install -e .
```

**Why editable mode?**

- Changes to `.pyi` files are immediately available
- No need to reinstall after updating stubs
- Package links to this directory instead of copying files
- Easy to maintain and update

### 3. Verify Installation

Check that the package is installed:

```bash
pip list | grep zoautil
```

Expected output:

```text
zoautil-py-stubs    1.0.0    /Users/fultonm/Documents/Development/zoau_stubs
```

### 4. Configure VS Code

#### Option A: Automatic (Recommended)

VS Code should automatically detect the installed package. Just restart the
Python language server:

1. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Python: Restart Language Server"
3. Press Enter

#### Option B: Manual Configuration

If IntelliSense doesn't work automatically, add to your project's `.vscode/settings.json`:

```json
{
    "python.analysis.extraPaths": [
        "/Users/fultonm/Documents/Development/zoau_stubs"
    ],
    "python.analysis.typeCheckingMode": "basic"
}
```

### 5. Test IntelliSense

Create a test file to verify IntelliSense is working:

```python
# test_zoau_stubs.py
from zoautil_py import mvscmd, datasets
from zoautil_py.ztypes import DDStatement

# Type 'mvscmd.' and you should see autocomplete suggestions
# Type 'DDStatement(' and you should see parameter hints
```

If you see autocomplete and parameter hints, the stubs are working correctly!

## Virtual Environments

### Using venv

```bash
# Create virtual environment
python3 -m venv ~/venvs/zoau-dev

# Activate it
source ~/venvs/zoau-dev/bin/activate  # macOS/Linux
# or
~/venvs/zoau-dev/Scripts/activate     # Windows

# Install stubs
cd /Users/fultonm/Documents/Development/zoau_stubs
pip install -e .
```

### Using conda

```bash
# Create conda environment
conda create -n zoau-dev python=3.9

# Activate it
conda activate zoau-dev

# Install stubs
cd /Users/fultonm/Documents/Development/zoau_stubs
pip install -e .
```

## Project-Specific Setup

For each project that uses ZOAU:

### 1. Create/Update requirements.txt

For development (local machine):

```txt
# requirements-dev.txt
-e /Users/fultonm/Documents/Development/zoau_stubs
```

For z/OS (production):

```txt
# requirements.txt
# zoautil_py is pre-installed on z/OS
# Do not include zoautil-py-stubs here
```

### 2. Update .gitignore

Add to your project's `.gitignore`:

```text
# Don't commit the stubs package
zoautil_py/
*.pyi
```

### 3. Document for Team Members

Add to your project's README:

```markdown
## Development Setup

This project uses ZOAU (Z Open Automation Utilities). For local development:

1. Install ZOAU stubs for IntelliSense:
   ```bash
   pip install -e /Users/fultonm/Documents/Development/zoau_stubs
   ```

1. The stubs provide type hints only. Code must be tested on z/OS.

1. On z/OS, the real ZOAU package is used automatically.

```text

## Uninstalling

If you need to uninstall the stubs:

```bash
pip uninstall zoautil-py-stubs
```

Note: This only removes the package registration, not the files (since it's
installed in editable mode).

## Updating the Stubs

Since the package is installed in editable mode:

1. Edit any `.pyi` file in `zoautil_py/`
2. Save the file
3. Restart VS Code's Python language server (Cmd+Shift+P → "Python: Restart
   Language Server")
4. Changes are immediately available - no reinstall needed!

## Troubleshooting

### Problem: IntelliSense not working

**Solution 1**: Restart Python language server

```text
Cmd+Shift+P → "Python: Restart Language Server"
```

**Solution 2**: Check Python interpreter

```text
Cmd+Shift+P → "Python: Select Interpreter"
```

Make sure you're using the interpreter where stubs are installed.

**Solution 3**: Verify installation

```bash
pip list | grep zoautil
python -c "import zoautil_py; print(zoautil_py.__file__)"
```

### Problem: Import errors in VS Code

**Solution**: Check that you're importing correctly:

```python
# Correct
from zoautil_py import mvscmd
from zoautil_py.ztypes import DDStatement

# Incorrect
import zoautil_py.mvscmd  # May not work with stubs
```

### Problem: Stubs installed on z/OS by mistake

**Solution**: Uninstall immediately

```bash
pip uninstall zoautil-py-stubs
```

The real ZOAU package should be the only `zoautil_py` on z/OS.

### Problem: Type checker errors

**Solution**: Configure type checking mode in VS Code settings:

```json
{
    "python.analysis.typeCheckingMode": "basic"
}
```

Or use `# type: ignore` comments for known issues.

## Advanced Configuration

### Multiple Python Versions

If you work with multiple Python versions:

```bash
# Python 3.8
python3.8 -m pip install -e /Users/fultonm/Documents/Development/zoau_stubs

# Python 3.9
python3.9 -m pip install -e /Users/fultonm/Documents/Development/zoau_stubs
```

### CI/CD Integration

For CI/CD pipelines that run on non-z/OS systems:

```yaml
# .github/workflows/test.yml
- name: Install ZOAU stubs
  run: |
    pip install -e /path/to/zoau_stubs
  if: runner.os != 'zOS'
```

### Docker Development

```dockerfile
# Dockerfile
FROM python:3.9

# Install stubs for development
COPY zoau_stubs /opt/zoau_stubs
RUN pip install -e /opt/zoau_stubs

# Your application code
COPY . /app
WORKDIR /app
```

## Getting Help

If you encounter issues:

1. Check this guide's troubleshooting section
2. Verify Python and pip versions: `python --version && pip --version`
3. Check VS Code Python extension version
4. Review VS Code's Python output panel for errors

## Next Steps

After installation:

1. Read [README.md](README.md) for usage examples
2. Test IntelliSense in your projects
3. Update stubs as needed for your use cases
4. Share this setup with your team
