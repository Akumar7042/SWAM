clear
BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
echo""
echo -e "${RED}                                          "
echo "        ___  _      _  _    _  _                      "
echo "       / __\ \      / / \  | \/ |                     "
echo "       \__ \  \    / /   \ ||\/||                     "
echo "       |___/   \/\/ /     \||  ||                     "


echo -e "${BLUE}   ~~ Tool for Hacking by PORT(AK-47) ${NC}"
echo ""

echo -e "${YELLOW} | Github.com/Akumar7042/SWAM.git | ${NC} "
echo ""
echo "--------------------------------------------------------------------"
echo ""

echo -e "${CYAN} [*] Enter For Install swan In Your Terminal or ctl+x(exit) -> ${NC}"
read INPUT
echo ""

I_DIR="/usr/share/doc/swam"
B_DIR="/usr/bin/"

echo "[*] Checking directories for Installing Process ! ...";
if [ -d "$I_DIR" ]; then
    echo "[!] A Directory swam Was Found.. Do You Want To Replace It ? [y/n]:" ;
    read ans

    if [ "$ans" = "y" ]; then
        rm -R "$_DIR"
    else
        exit
    fi
fi
echo "[*] Installing Swam ...";
echo "";
git clone https://github.com/Akumar7042/swam.git "$I_DIR";
echo "#!/bin/bash
python $I_DIR/swam.py" '${1+"$@"}' > swam;
chmod +x swam;
sudo cp swam /usr/bin/;
rm swam;

if [ -d "$I_DIR" ] ;
then
    echo "";
    echo "[✔] Swam is Successfuly Installed !!! [✔]";
    echo "";
    echo "[✔]========================================================================[✔]";
    echo "[✔] ✔✔ NOW you can execute tool by typing ->root/#swam !! ✔✔✔ [✔]";
    echo "[✔]========================================================================[✔]";
    echo "";
else
    echo "[✘] Installation Failed [✘]";
    exit
fi

