# MCQ Generator

## A GenAI application that lets users create MCQs from any .txt or .pdf file

### Project Description

This application uses a Generative AI model to create multiple-choice questions (MCQs) from the content of .txt or .pdf files using OpenAI and LangChain. The generated MCQs can be tailored to different subjects and levels of difficulty. The app leverages LangChain and Hugging Face models for natural language processing.

### Prerequisites

- **Python 3.8** (ensure you have Python 3.8 installed on your system)
- **An OpenAI API key** (if using OpenAI models)

### Setup Instructions

Follow the steps below to set up and run the MCQ Generator application:

#### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

#### 2. Create a Virtual Environment using Conda

```bash
conda create --name mcq-generator python=3.8
conda activate mcq-generator
```

#### 3. Install Required Packages
Make sure you are in the project directory, then install the required packages using pip:
```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables
Create a .env file in the root directory of the project and add your OpenAI API key:
```bash
touch .env
```
Open the .env file in a text editor and add the following line:
```bash
API_KEY="<your-openai-api-key>"
```

#### 5. Run the Application
To run the application, use the following command:
```bash
streamlit run app.py
```

### Usage Instructions

1. **Upload a .txt or .pdf File:**
   - Upload a `.txt` or `.pdf` file containing the text you want to generate MCQs from.

2. **Set Parameters:**
   - Set the number of questions, subject, and tone according to your requirements.

3. **Generate MCQs:**
   - The app will generate and display the MCQs based on the provided text.

4. **Review and Download:**
   - You can review the generated MCQs and download them if satisfied.

### Troubleshooting

- **Application Fails to Start:**
  - Ensure that all dependencies are installed correctly by following the installation steps in the [Setup Instructions](#setup-instructions).
  
- **Python Version Issue:**
  - Verify that the Python version is set to 3.8 in your virtual environment.
  
- **API Key Issue:**
  - Ensure the `.env` file contains the correct OpenAI API key.

### Contributing

- **Fork and Pull Request:**
  - If you'd like to contribute to the project, please fork the repository and submit a pull request.

- **Open an Issue:**
  - For major changes, please open an issue first to discuss what you would like to change.

  
### License

This project is licensed under the MIT License. 

You are free to use, modify, and distribute this software under the terms of the MIT License. See the [LICENSE](./LICENSE) file for more details.
