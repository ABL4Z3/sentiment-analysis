# Sentiment Analysis Tool 📊

A simple and interactive web application built with Streamlit for analyzing the sentiment of text input. The tool classifies each sentence as Positive, Negative, or Neutral, providing a summary with metrics, a visual bar chart, and a detailed sentence-by-sentence breakdown.

## Features

- **Text Input**: Paste or type text to analyze.
- **Sentiment Classification**: Uses TextBlob to classify sentences based on polarity (Positive, Negative, Neutral).
- **Summary Metrics**: Displays total sentences and percentages for each sentiment category.
- **Visual Chart**: Bar chart showing sentiment distribution using Matplotlib.
- **Detailed Table**: Pandas DataFrame with sentence-level analysis including polarity scores.
- **NLTK Integration**: Automatically downloads and uses NLTK's punkt tokenizer for sentence splitting.
- **Responsive UI**: Built with Streamlit for an easy-to-use web interface.

## Installation

1. **Clone or Download the Repository**:
   ```
   git clone <repository-url>
   cd sentiment-analysis
   ```

2. **Set Up a Virtual Environment** (Recommended):
   ```
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   ```
   streamlit run app.py
   ```

2. **Access the App**:
   - Open your browser and go to `http://localhost:8501` (or the URL provided by Streamlit).

3. **Analyze Text**:
   - Enter your text in the text area.
   - Click "Analyze Sentiment" to see results.
   - View summary metrics, the bar chart, and the detailed table.

## Dependencies

- **Streamlit**: For the web application framework.
- **TextBlob**: For natural language processing and sentiment analysis.
- **Matplotlib**: For generating the bar chart.
- **Pandas**: For creating and displaying the results table.
- **NLTK**: For sentence tokenization (punkt tokenizer).

All dependencies are listed in `requirements.txt`.

## Project Structure

- `app.py`: Main application script.
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Ignores virtual environment folder (`myenv`).

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License

This project is open-source. Please check the license file for details.
