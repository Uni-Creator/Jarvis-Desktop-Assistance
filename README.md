# Jarvis - Personal Desktop Assistant

A powerful desktop assistant built in Python with voice and GUI-based interactions. Jarvis integrates web search, system automation, multimedia control, and more.

## Features

- **Voice Commands:** Control your desktop and get information via natural voice commands.
- **Modern GUI Interface:** An intuitive, chat-style GUI built with Tkinter.
- **System Controls:**
  - Lock, shutdown, restart, or hibernate the system.
  - Empty or restore the recycle bin.
  - Camera control, screenshot capture, wallpaper management.
  - Volume and brightness control.
- **Web Integration:**
  - Google search
  - Weather updates
  - News retrieval
  - Location search on Google Maps
- **Customizable and Modular:** Easily add new features or commands.
- **Multi-mode Input:** Supports both voice and text input.

## Project Overview

The Jarvis project is structured with separate modules for key functionalities, such as voice commands, GUI control, and web-based interactions, ensuring an organized and scalable codebase.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/jarvis-desktop-assistant.git
   cd jarvis-desktop-assistant
   ```
   
2. **Set Up a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Assistant:**
   ```bash
   python jarvis.py
   ```
   or
   ```bash
   python testChatUI.py
   ```
   

## Usage

Jarvis can operate in:
- **GUI Mode:** Interact via the chat-style interface.
- **Voice Mode:** Speak commands directly into the microphone.

### Common Commands:
- "What’s the weather in [location]?"
- "Find [topic] on Google."
- "Change wallpaper."
- "Lock the screen."
- "Empty recycle bin."

## Technical Overview

- **Speech Recognition**: Using `speech_recognition` and `pyttsx3`.
- **Data Parsing**: JSON and file handling for user data and preferences.
- **API Integrations**: Weather, news, and Google Maps.
- **Thread Management**: For smooth execution of background tasks.
- **Cross-module Communication**: Helper functions connect core features, GUI, and data.

## Project Structure

```plaintext
Jarvis/
├── README.md                  # Project readme file
├── requirements.txt           # Python dependencies
├── LICENSE                    # License for the project
├── .gitignore                 # Git ignore settings
│
├── Jarvis.py                  # Core assistant class and functionality
├── testChatUI.py              # Main GUI interface
│
├── data/
│   ├── GUI/
│   │   ├── ico/               # Icons and images for GUI
│   │   ├── jarvis.ui          # Main UI layout
│   │   └── wallpaper.ui       # Wallpaper selector UI
│   │
│   ├── features/
│   │   ├── google_search.py   # Google search module
│   │   ├── weather.py         # Weather API integration
│   │   └── gui.py             # GUI helper functions
│   │
│   ├── files/
│   │   ├── ico/               # System icons
│   │   ├── myinfo/            # User information storage
│   │   └── BGW/               # Background wallpapers
│   │
│   └── loginInfo/             # User authentication data
│
├── functions/
│   ├── settings.py            # System settings controls
│   ├── notification.py        # Notifications module
│   ├── progress.py            # Progress bar utilities
│   └── wallpaper.py           # Wallpaper management
```

## Contributing

We welcome contributions! Please:
1. Fork the repository.
2. Create a feature branch.
3. Commit and push changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please feel free to reach out to the project maintainer at [abhayr245654@gmail.com].
