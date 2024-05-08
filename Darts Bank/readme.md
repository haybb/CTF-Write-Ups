# 404CTF 2024 - DartsBank

**"Warning: this challenge contains malicious code. Although the author has tried to make it relatively harmless, Adequate insulation measures should be taken if it has to be carried out. The organization assumes no responsibility for any damage to your system."**  
Regarding that, every *malicious files* are stored within the zipped folder **Be_Careful**.  
Unzip it using 7Zip, knowing that password is ```infected```.

1. Walking through packets using Wireshark  
=> package no.50 with powershell

2. Obfuscated powershell code with large chunks in base64  
=> we decode the pieces in base64 and obtain a huge command (see commands.txt for encrypted + decrypted code)  
  
3. We had XOR keys which encrypt the data then send by HTTP POST to http://192.168.78.89/index.html  
  
4. Search ```http.request.method == POST```  
=> 9 packets containing messages to be decoded from base64 then to XOR  
  
5. We decode then xor these 9 messages *(see dartsbank.py)*  
  
6. We obtain 9 SSL keys, concatenated in the same *sslkey.log* file  
  
7. We put in wireshark *(Edit > Preferences > TLS > Add pre-master key log file)* 
  
8. New HTTP2 decrypted packets have appeared.  
  
9. We search for files: *File > Export Objects > HTTP > Save All*  
  
10. Here the file *%5c* (the name changes depending on the execution) contains the flag :)  
