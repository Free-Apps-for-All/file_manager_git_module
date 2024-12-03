# Gitmodule Utility to standard manage file operations with ease.

--- 

## Usage


###  1. First thing first


```bash
git init
```

### 2. Turn on Git's sparse-checkout

Need this to exclude `README.md` and  `.gitignore` files:

```bash
git config core.sparseCheckout true
```

```bash
echo "!/.gitignore" >> .git/info/sparse-checkout
echo "!/README.md" >> .git/info/sparse-checkout
```

### 3. Include the submodule

```bash
git submodule add git@github.com:Free-Apps-for-All/file_manager_git_module.git gitmodules/file_manager
```

or adjust as you wish
```bash
git submodule add git@github.com:Free-Apps-for-All/file_manager_git_module.git <path/to/save>
```

---
