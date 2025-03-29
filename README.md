

<p align="center">
  <img src="https://i.imgur.com/SFKLF26.jpeg" alt="Port Scanner Tool" />
</p>

# Python Port Scanner: Basic Security Tool

A lightweight basic, multi-threaded port scanner written in Python for educational purposes and basic security assessments. This tool demonstrates fundamental concepts of network security and port scanning techniques.

---

## 🔍 Features

- **Multi-threaded scanning**: Fast port scanning using thread pools
- **Service detection**: Identifies common services on open ports
- **Detailed reporting**: Generates comprehensive scan reports
- **Customizable parameters**: Adjustable port ranges and timeout settings
- **Command-line interface**: Easy to use with command-line arguments

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/diegoamororor/Python-Port-Scanner-Basic-Tool.git
cd Python-Port-Scanner-Basic-Tool
````

---

## 💻 Usage

Basic usage:

```bash
python port_scanner.py target_host
```

Advanced usage:

```bash
python port_scanner.py target_host -s start_port -e end_port -t timeout
```

### Parameters:

- `target_host`: IP address or hostname to scan
- `-s, --start`: Starting port number (default: 1)
- `-e, --end`: Ending port number (default: 1024)
- `-t, --timeout`: Timeout in seconds for each port (default: 1)

### Example:

```bash
python port_scanner.py example.com -s 80 -e 443 -t 0.5
```

---

## 📋 Output Example

```
=====================================
Scan Report for: example.com
Date and time: 2025-03-29 10:30:15
=====================================

Open ports found:
------------------------------
Port 80: http
Port 443: https

=====================================
```

---

## 🛠 Technical Details

### Components:

1. **PortScanner Class**
    
    - Main scanning engine
    - Handles connection attempts
    - Service detection
    - Report generation
2. **Threading Implementation**
    
    - Uses ThreadPoolExecutor
    - Configurable number of workers
    - Efficient parallel scanning
3. **Service Detection**
    
    - Built-in service identification
    - Common port mapping
    - Unknown service handling

---

## 🔒 Security Considerations

- This tool should only be used on systems you own or have explicit permission to test
- Port scanning without authorization may be illegal in some jurisdictions
- Use responsibly and ethically
- Not intended for malicious purposes

---

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

This tool is created for educational purposes only. The author is not responsible for any misuse or damage caused by this program. Users must ensure they have explicit permission to test the target systems.

---

## 📚 Resources

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [Threading in Python](https://docs.python.org/3/library/threading.html)
- [Port Numbers Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)

---

## 👥 Author

Diego Amoroso

- GitHub: [@diegoamorosor](https://github.com/diegoamorosor)
- LinkedIn: [Diego Amoroso](https://linkedin.com/in/diegoamorosor)

---

## 🙏 Acknowledgments

- Thanks to the Python community for the excellent documentation
- Inspired by various open-source security tools
