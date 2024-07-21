import sys
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox

class ExchangeRatePredictor(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.data = None
        
    def initUI(self):
        self.setWindowTitle('Exchange Rate Predictor')
        
        # Layouts
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        
        # Widgets
        self.file_button = QPushButton('Select CSV File')
        self.file_label = QLabel('No file selected')
        self.date_column_label = QLabel('Date Column:')
        self.date_column_input = QLineEdit()
        self.rate_column_label = QLabel('Exchange Rate Column:')
        self.rate_column_input = QLineEdit()
        self.date_label = QLabel('Enter date (YYYY-MM-DD):')
        self.date_input = QLineEdit()
        self.predict_button = QPushButton('Predict')
        self.result_label = QLabel('')
        
        # Add widgets to layout
        hbox1.addWidget(self.file_button)
        hbox1.addWidget(self.file_label)
        hbox2.addWidget(self.date_column_label)
        hbox2.addWidget(self.date_column_input)
        hbox3.addWidget(self.rate_column_label)
        hbox3.addWidget(self.rate_column_input)
        hbox4.addWidget(self.date_label)
        hbox4.addWidget(self.date_input)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addWidget(self.predict_button)
        vbox.addWidget(self.result_label)
        
        self.setLayout(vbox)
        
        # Connect button click to functions
        self.file_button.clicked.connect(self.select_file)
        self.predict_button.clicked.connect(self.predict_exchange_rate)
        
    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Select CSV File', '', 'CSV files (*.csv)')
        
        if file_path:
            self.file_label.setText(file_path)
        else:
            self.file_label.setText('No file selected')
    
    def load_data(self, file_path, date_column, rate_column):
        self.data = pd.read_csv(file_path)
        self.data[date_column] = pd.to_datetime(self.data[date_column], format='%Y-%m-%d')
        self.data.set_index(date_column, inplace=True)
        self.data = self.data[[rate_column]].dropna()
        start_date = self.data.index.min()
        end_date = self.data.index.max()
        new_index = pd.date_range(start=start_date, end=end_date, freq='D')
        self.data = self.data.reindex(new_index)
        self.data[rate_column].interpolate(method='linear', inplace=True)
    
    def predict_exchange_rate(self):
        if self.file_label.text() == 'No file selected':
            QMessageBox.warning(self, 'Warning', 'Please select a CSV file first.')
            return
        
        date_column = self.date_column_input.text()
        rate_column = self.rate_column_input.text()
        if not date_column or not rate_column:
            QMessageBox.warning(self, 'Warning', 'Please enter both the date column and the exchange rate column names.')
            return
        
        future_date_str = self.date_input.text()
        try:
            future_date = pd.to_datetime(future_date_str)
        except ValueError:
            QMessageBox.warning(self, 'Warning', 'Invalid date format. Please use YYYY-MM-DD.')
            return
        
        # Load data
        self.load_data(self.file_label.text(), date_column, rate_column)
        
        # Extend the dataframe
        data_extended = self.data.reindex(self.data.index.union(pd.Index([future_date])))
        
        # Refit the model with extended data
        model_extended = ARIMA(data_extended[rate_column], order=(1, 1, 1))
        model_fit_extended = model_extended.fit()
        
        # Make the forecast
        forecast = model_fit_extended.get_forecast(steps=1)
        predicted_value = forecast.predicted_mean.iloc[-1]
        
        # Display the result
        self.result_label.setText(f"On {future_date.date()}, the predicted exchange rate is {predicted_value:.2f}.")
        
def main():
    app = QApplication(sys.argv)
    ex = ExchangeRatePredictor()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
