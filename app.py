import socket
import re
from flask import Flask, render_template, request
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Function to validate input (check if it's an IP or URL)
def validate_input(input_data):
    try:
        socket.inet_aton(input_data)
        return 'ip', input_data  # It's an IP address
    except socket.error:
        if re.match(r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', input_data):
            try:
                ip = socket.gethostbyname(input_data)
                return 'url', input_data  # It's a URL
            except socket.gaierror:
                raise ValueError(f"Invalid URL: {input_data}")
        else:
            raise ValueError(f"Invalid input: {input_data}")

# Function to scan a single port
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:  # Port is open
                service = socket.getservbyport(port, "tcp") if port <= 65535 else "Unknown"
                return port, "Open", service
    except Exception:
        pass
    return port, "Closed", "N/A"

# Threaded scanning function using ThreadPoolExecutor
def scan_ports(host, start_port, end_port):
    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, host, port): port for port in range(start_port, end_port + 1)}
        for future in futures:
            port, status, service = future.result()
            if status == "Open":  # Only keep open ports
                results.append((port, status, service))
    return results

# Route to display the form (home page)
@app.route("/")
def home():
    return render_template("index.html")

# Route to start the port scan and return results
@app.route('/scan', methods=['POST'])
def start_scan():
    target = request.form['target']
    start_port = int(request.form['start_port']) if request.form['start_port'] else 1
    end_port = int(request.form['end_port']) if request.form['end_port'] else 1024

    try:
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range.")

        input_type, validated_target = validate_input(target)
        
        # Perform the scan
        results = scan_ports(validated_target, start_port, end_port)
        
        return render_template('index.html', results=results, target=validated_target)

    except ValueError as e:
        return render_template('index.html', error_message=str(e))

# Main block to run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Allow external access
