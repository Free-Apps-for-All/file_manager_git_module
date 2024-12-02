# Gitmodule Utility to Standardize File Operations with Ease

---

## Usage

Create a `.gitmodules` file and include this gitmodule. Example:

```yaml
[submodule "file_manager"]
    path = ./gitmodules
    url = git@github.com:Free-Apps-for-All/file_manager_git_module.git
```

---

## Install

### Initial Install:

```bash
git submodule update --init --recursive
```

### Further Update (if updates are available):

```bash
git submodule update --recursive
```

---

This version should be correct. Just ensure that you are naming the file `.gitmodules` (plural) in your project.