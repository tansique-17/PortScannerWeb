# [PortScannerWeb](https://portscannerweb.onrender.com/)

# Deployment  

https://portscannerweb.onrender.com/

## Flask-Based Port Scanner

This project is a Flask web application that performs port scanning on a target IP address or URL. It allows users to input a target, specify a port range, and displays open ports along with their associated services.

## Features

- **Input Validation**: Validates if the target is a valid IP address or URL.
- **Port Scanning**: Scans ports in the specified range and checks if they are open or closed.
- **Multi-threading**: Utilizes `ThreadPoolExecutor` for efficient and fast scanning.
- **Web Interface**: Provides an interactive web form for input and displays the results.

---

## Requirements

Ensure you have the following installed:

- Python 3.9 or later
- Flask

Install the required dependencies using:

```bash
pip install flask
```

---

## Project Structure

```
/your_project
|-- static/         # Folder for static files like CSS
|-- templates/      # Folder for HTML templates
|   |-- index.html  # Main HTML page
|-- app.py          # Main Python application file
|-- README.md       # Project documentation (this file)
```

---

## How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tansique-17/PortScannerWeb.git
   cd port-scanner-web
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Web App**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage

1. Enter a target (IP address or URL) in the input field.
2. Specify the start and end port range (optional; defaults to 1-1024).
3. Click the "Scan" button.
4. View the results on the same page, displaying open ports and their services.

---

## Code Overview

### `app.py`
- **Functions**:
  - `validate_input(input_data)`: Validates the target input as either an IP or URL.
  - `scan_port(host, port)`: Scans a single port and returns its status.
  - `scan_ports(host, start_port, end_port)`: Scans a range of ports using multi-threading.
- **Routes**:
  - `/`: Displays the home page with the input form.
  - `/scan`: Handles the form submission, performs the scan, and returns the results.

---

## Error Handling

- Validates inputs for IPs, URLs, and port ranges.
- Displays appropriate error messages for invalid inputs.

---

## Example Output

After scanning, the results will display a table with the following columns:

- **Port**: The port number.
- **Status**: "Open" or "Closed".
- **Service**: The associated service name (e.g., HTTP, FTP).

---

## Future Enhancements

- Add UDP scanning.
- Implement user authentication for added security.
- Improve the UI design with a more modern framework.
- Allow saving scan results as a file (e.g., CSV).

---

## License

This project is open-source and available under the MIT [License](https://github.com/tansique-17/PortScannerWeb/blob/main/LICENSE).

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## Author

Tansique Dasari

Feel free to contact me at [tansique.17@gmail.com](mailto:tansique.17@gmail.com) for any questions or feedback!

