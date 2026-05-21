# Python Examples

## In your own project

Install from PyPI:

```
pip install space-gass-api
```

Each example includes a `requirements.txt` you can copy into your own project.

## From this repo

Install the SDK in editable mode once:

```
pip install -e sdks/python/client
```

This makes the local source available as the `space-gass-api` package. All examples will resolve imports from the local client code — no path hacks needed.

### VS Code

If you open the `sdks/python/examples` folder in VS Code, the [`.vscode/settings.json`](.vscode/settings.json) configures Pylance to resolve imports from the local client for IntelliSense.
