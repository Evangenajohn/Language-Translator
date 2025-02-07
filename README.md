# Language Translator

A simple language translation application built with Python using Tkinter for the GUI and Google Translate API (via the `googletrans` library). This application allows users to input text and translate it into any language of their choice.

## Features
- Input any text for translation.
- Select the target language from a dropdown menu.
- Real-time translation displayed on the GUI.
- Supports a wide range of languages from Google Translate.

## Demo
![Language Translator Logo](images/LT Logo.png)


## Installation

### Prerequisites
To run this app, you'll need Python installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/Evangenajohn/Language-Translator.git
```

### 2. Navigate to the Project Folder
```bash
cd Language-Translator
```

### 3. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```

#### Activate the Virtual Environment
- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Required Libraries
If a `requirements.txt` file exists, install dependencies with:
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file, manually install dependencies:
```bash
pip install googletrans==4.0.0-rc1
pip install tk
```

## Usage
Once the dependencies are installed, you can start the language translator application.

### Run the Application
```bash
python translator.py
```

### How to Use:
1. Enter the text you want to translate in the **Input Text** field.
2. Select the language you want to translate to from the **Target Language** dropdown menu.
3. Click **Translate** to see the translated text in the **Output** field.

## Supported Languages
This app supports all languages available in Google Translate. Some common examples include:

- English
- Spanish
- French
- German
- Chinese
- Japanese
- Russian
- ... and many more!

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Contributing
We welcome contributions to improve the Language Translator! Here's how you can contribute:

1. **Fork** this repository.
2. Create a **new branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and **commit** them:
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push** to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a **Pull Request** to merge your changes into the main branch.

## Acknowledgments
- **Google Translate API** for translation capabilities.
- **Tkinter** for the graphical user interface.
- **googletrans** Python library for accessing Google Translate.

## Contact
Created by **Evangelin John**

Feel free to **open issues** or **contact me** if you have any questions or suggestions.
