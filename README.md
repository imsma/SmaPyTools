# SmaPyTools: Streamlined Python Utilities

Welcome to SmaPyTools, a versatile collection of Python utilities designed to enhance productivity and simplify tasks for developers. Founded by [Shoket Mahmood Ahmed](https://sma.im), this project aims to provide easy-to-use tools and code snippets that address common and unique programming needs.

Here's how you can document the environment setup process for your Python project using Markdown format:

## Environment Setup

To ensure that your development environment is consistent and isolated, follow these steps to set up a Python virtual environment using `pyenv` and `venv`.

### Prerequisites

Make sure `pyenv` is installed on your system. You can install it by following the instructions on the [pyenv GitHub page](https://github.com/pyenv/pyenv).

### Steps

1. **Set Python Version**

   Set the local Python version to `3.11.2` using `pyenv`. This ensures that all operations within this directory use this specific Python version.

   ```bash
   pyenv local 3.11.2
   ```

2. **Create Virtual Environment**

   Create a new virtual environment named `env`. This virtual environment will use the previously set Python version.

   ```bash
   python -m venv env
   ```

3. **Activate Virtual Environment**

   Activate the virtual environment to start using it. Activating the environment adjusts the path and other environment variables to use the Python and pip executable files inside the `env` directory.

   ```bash
   source env/bin/activate
   ```

## Next Steps

After setting up and activating your environment, you can proceed to install required packages using `pip` and begin development.

Remember to deactivate your virtual environment when you're done by running:

```bash
deactivate
```

````

## Key Features:

- **User-friendly**: Each utility is developed with simplicity and ease of use in mind, ensuring that both novice and experienced developers can benefit.
- **Versatile**: From image processing to data manipulation, SmaPyTools aims to cover a broad range of applications, continually expanding with the community's needs.
- **Open Source**: Fully open-source, encouraging contributions and improvements from the Python community. Whether it's fixing bugs, adding features, or improving documentation, all forms of collaboration are welcome.

## Utilities:

### Image to Base64 Conversion

- **Image to Base64 Conversion**: Quickly convert images to Base64 encoding, a must-have for web development and data serialization tasks.

## Features

- **Easy-to-Use**: Tools designed for simplicity and effectiveness.
- **Versatile**: Suitable for a variety of programming tasks.
- **Community-Driven**: Contributions are welcome to extend functionality.

```bash
python -m cli.main image-to-base64 /path/to/image/
```


## Getting Started

To get started with SmaPyTools, clone this repository:

```bash
git clone https://github.com/imsma/SmaPyTools.git
````

## Contributing

Contributions to SmaPyTools are highly encouraged and appreciated. Whether it's adding new tools, improving existing ones, or enhancing documentation, all forms of collaboration help make SmaPyTools more valuable.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community for continuous support and inspiration.
- Special thanks to everyone who contributes to open source.
