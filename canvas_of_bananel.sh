
echo "!!!!!!! PLEASE NOTE !!!!!!!"
echo "This Launcher is still in BETA and has many bugs"
echo "!!!!!!! PLEASE NOTE !!!!!!!"
echo ""

if command -v python3 >/dev/null 2>&1; then
    ver="$(python3 --version 2>&1 | awk '{print $2}')"
    if [ "$ver" = "3.12.3" ]; then
        if command -v pip >/dev/null 2>&1; then
            echo "Everything installed!"
            echo "Checking pygame..."
            ins="$(pip show pygame 2>&1 | awk '{print $2}')"
            if [ "$ins" = "WARNING: Package(s) not found: pygame" ]; then
                echo "pygame not installed!"
                echo "Installing pygame..."
                pip install pygame
                echo "pygame installed!"
            else
                echo "pygame already installed!"
            fi
            echo "Launching..."
            echo ""
            python3 main.py
            echo ""
            echo "Thanks for playing!"
            echo "Closing launcher..."
            
        else
            echo "pip not installed!"
            echo ""
            echo "(Aborting)"
        fi
    else
        echo "Wrong Python version installed!"
        echo "(You have version $ver installed)"
        echo "Please install Python 3.12.3 from https://www.python.org/downloads/release/python-3120/"
        echo ""
        echo "(Aborting)"
    fi
else
    echo "Python not installed!"
    echo "Please install Python 3.12.3 from https://www.python.org/downloads/release/python-3120/"
    echo ""
    echo "(Aborting)"
fi