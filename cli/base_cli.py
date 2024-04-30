class BaseCLI:
    """Base class for CLI commands, providing shared functionalities."""

    def execute(self):
        raise NotImplementedError("Subclasses must implement this method.")