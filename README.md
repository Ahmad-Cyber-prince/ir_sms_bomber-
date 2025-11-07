```markdown
# IR SMS Bomber

A powerful and advanced SMS bombing tool for Iranian services developed by Ahmad Cyber for educational and testing purposes.

## 🚀 Features
- Support for multiple Iranian services
- Multi-threading for fast execution
- Easy-to-use interface
- Cross-platform compatibility
- Customizable delay between requests
- Phone number validation
- Real-time status updates

## ⚠️ Disclaimer
**This tool is developed for educational purposes only. The developer is not responsible for any misuse of this tool. Use it at your own risk and only on phone numbers you own or have explicit permission to test.**

## 📋 Supported Services
- Snapp
- Gap
- Tap30
- Divar
- Torob
- SnapFood
- Sheypoor
- AliBaba
- SnapMarket
- And many more...

## 🛠️ Installation

### Termux (Android)
```bash
# Update packages
pkg update && pkg upgrade

# Install Python and required tools
pkg install python git

# Clone the repository
git clone https://github.com/Ahmad-Cyber-prince/ir-sms-bomber.git

# Navigate to directory
cd ir-sms-bomber

# Install Python dependencies
pip install requests urllib3

# Run the script
python ir_sms_bomber.py
```

Linux (Ubuntu/Debian)

```bash
# Update system
sudo apt update && sudo apt upgrade

# Install Python and git
sudo apt install python3 python3-pip git

# Clone the repository
git clone https://github.com/Ahmad-Cyber-prince/ir-sms-bomber.git

# Navigate to directory
cd ir-sms-bomber

# Install Python dependencies
pip3 install requests urllib3

# Run the script
python3 ir_sms_bomber.py
```

Linux (CentOS/RHEL/Fedora)

```bash
# For CentOS/RHEL
sudo yum update
sudo yum install python3 python3-pip git

# For Fedora
sudo dnf update
sudo dnf install python3 python3-pip git

# Clone and run
git clone https://github.com/Ahmad-Cyber-prince/ir-sms-bomber.git
cd ir-sms-bomber
pip3 install requests urllib3
python3 ir_sms_bomber.py
```

🎯 Usage

Basic Usage

```bash
python ir_sms_bomber.py
```

Step-by-Step Guide

1. Run the script using one of the methods above
2. Enter the target phone number when prompted (in +98 format)
3. Set the delay between requests (default is 0.1 seconds)
4. The script will start sending SMS to the target number
5. Press Ctrl+C to stop the script at any time

Phone Number Formats Supported

· +989123456789
· 989123456789
· 09123456789
· 9123456789

Advanced Usage

You can modify the delay time between requests for different speeds:

· Fast: 0.1 seconds
· Medium: 0.5 seconds
· Slow: 1-2 seconds

📁 Project Structure

```
ir-sms-bomber/
├── ir_sms_bomber.py    # Main script
├── README.md           # Documentation
└── requirements.txt    # Python dependencies
```

🔧 Requirements

· Python 3.6 or higher
· requests library
· urllib3 library
· Internet connection

🐛 Troubleshooting

Common Issues & Solutions

Issue: ModuleNotFoundError

```bash
pip install --upgrade pip
pip install requests urllib3
```

Issue: Python not found

```bash
# Termux
pkg install python

# Linux
sudo apt install python3
```

Issue: Permission denied

```bash
# Give execution permission
chmod +x ir_sms_bomber.py
```

Issue: Encoding problems

```bash
export LANG=en_US.UTF-8
python ir_sms_bomber.py
```

Issue: Slow execution

· Increase the delay time between requests
· Check your internet connection

🔒 Legal Notice

This tool is intended for:

· Educational purposes
· Security research
· Testing your own systems
· Learning about API security

Illegal use of this tool is strictly prohibited. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

📞 Contact & Support

· GitHub: Ahmad-Cyber-prince
· Instagram: Cyber_ir_Ahmad

If you encounter any issues:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. DM me on Instagram
4. Ensure you're using the latest version

🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

📄 License

This project is for educational purposes. Use responsibly.

---

Developer: Ahmad Cyber
GitHub: Ahmad-Cyber-prince
Instagram: Cyber_ir_Ahmad
Version: 1.0

⭐ Star the Repository

If you find this tool useful, please consider giving it a star on GitHub!

🔔 Updates

Check the GitHub repository regularly for updates and new features.

```
