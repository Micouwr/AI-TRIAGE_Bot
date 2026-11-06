# Prompts Directory

This directory contains prompt templates used by the Vigil to classify and process support tickets.

## Contents

- **classification_prompt.txt**: The live prompt template used by `bot_engine/router.py` to classify support tickets into predefined categories. The router formats it with the ticket categories from `scope.yaml` and expects a JSON object with `category` and `confidence`.

## Purpose

The prompts in this directory are designed to guide the AI model in making accurate and consistent classifications, ensuring that the Vigil operates effectively and adheres to governance standards.

## Usage

To use the prompts:
1. Place the relevant prompt template in the input stream of the AI model.
2. Ensure the AI model is configured to parse and respond to the prompt as expected.
3. The AI model will generate an output based on the prompt, which should then be processed according to the bot's logic.

## How to Contribute

If you need to add or modify prompts:
- Ensure the changes align with the bot's classification categories and governance requirements.
- Update the prompt templates as needed to improve classification accuracy or to accommodate new features.
- Document any changes in the `lifecycle/versionhistory.md` file to maintain an audit trail.

## Contact

For questions or issues related to the prompts, contact William Micou at micouwr@gmail.com.
