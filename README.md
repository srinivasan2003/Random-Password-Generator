# Random Password Generator

A simple Python script to generate random passwords with specified length and character set.

## Features

- Generates passwords with a minimum length of 8 characters.
- Allows customization of character set for password generation.
- Ensures that generated passwords include at least one lowercase letter, one uppercase letter, one digit, and one special character.

## Usage

1. Run the `password_generator.py` script.
2. Enter the desired password length when prompted. Password length should be at least 8 characters.
3. Optionally, enter a custom character set or leave it empty for the default set (includes letters, digits, and punctuation).
4. The script will generate and display a password meeting the specified criteria.

## Script Structure

- `generate_password(length, chars)`: Function to generate a password with the specified length and character set.
- `get_user_input()`: Function to prompt the user for password length and character set.
- `main()`: Main function orchestrating the password generation process.

## Dependencies

- Python 3.x

## Running the Script

```bash
python password_generator.py
