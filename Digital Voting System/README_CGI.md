# Working with `.cgi` files

- **File association:** Added workspace setting to treat `*.cgi` files as Perl for syntax highlighting. File: `.vscode/settings.json`
- **Run locally:** Use the provided VS Code task `Run CGI Server (python)` which runs `python -m http.server --cgi 8000` with working directory set to the `placement pro/cgi-bin` folder.

Recommended extensions (install from the Extensions view):
- Perl language support (syntax highlighting, linting) — useful if your `.cgi` are Perl scripts.
- ShellCheck — if your `.cgi` scripts are shell scripts.
- Apache Conf or HTTP Server configuration highlighters — helpful for `.htaccess` and server config.
- HTML/CSS/JS extensions for editing files in `htdocs`.

Quick commands:
```
# Run the CGI server task from VS Code: Run Task -> Run CGI Server (python)
# Or from a terminal (workspace root):
python -m http.server --cgi 8000
```

Open a browser at `http://localhost:8000/` and access your CGI scripts from the `cgi-bin` path (e.g. `http://localhost:8000/results.cgi`).
