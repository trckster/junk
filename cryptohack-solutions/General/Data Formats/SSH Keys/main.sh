ssh-keygen -f rsa.pub -e -m pem > rsa.pem
python3 print-n-from-pem.py
