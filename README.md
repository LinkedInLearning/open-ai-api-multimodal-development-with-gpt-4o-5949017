# OpenAI API: Multimodal development with GPT-4o
This is the repository for the LinkedIn Learning course `OpenAI API: Multimodal development with GPT-4o`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

In this hands-on course you’ll use the OpenAI API to leverage the multimodal capabilities of GPT-4o and function calling to extract text from images, conform the data to JSON, and call functions to save the extracted data to a spreadsheet.

_See the readme file in the main branch for updated instructions and information._
## Instructions
This repository holds example data and two Jupyter Notebooks:
- `data/` holds a collection of images of random receipts and one wild-card.
- `expenses.csv` is the target CSV. At init, the CSV only holds column headings.
- `gp4o-setup.py` demonstrates how to how to access gpt-4o for multimodal prompting.
- `modular-process.py` and the module files in `utils/` demonstrate a comprehensive process of ingesting and interpreting multiple receipts and sending the data to a CSV file.

The first time you run a block in a Jupyter Notebook, the environment will ask you to pick an environment. Follow the instructions and pick the first available Python environment. 

NOTE: The first code block may take a while to load because the environment has to load first.

## Installing
It is recommended you run these exercise files in GitHub Codespaces. This gives you a pre-configured Python environment for the Jupyter Notebooks to run.
To use the exercise files, follow these steps:
1. In the root folder, rename the file `env-template` to `.env`.
2. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
3. Generate a new key and copy the key to your clipboard.
4. In `.env` add the key without quotes or parentheses.


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/openai-api-multimodal-development-with-gpt-4o
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D4E0DAQH67m3BQizrcw/learning-public-crop_675_1200/0/1717777723110?e=2147483647&v=beta&t=QpXxJL0FkIrZVPHZDGci173murlG_Yf8FJiERdEhJ_0

