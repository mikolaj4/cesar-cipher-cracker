# cesar-cipher-crakcer

Program łamie szyfr cezara używając analizy częstotliwości wystepowania znaków w języku.

====

The program shows success rates in cracking cesar ciphers

Example of long plaintext in Polish:  Cześć, oto przykładowy tekst po Polsku ze znakami interpunkcyjnymi;,/$!? i kropkami..

Encrypted text with key 5:  fbizgśźśuwbąńódhśaąźińyźuśuśoyńżbibrdńdpmmrźiwużrńfąnrąpmmńwśuńdpm

Result of ciphertext-only attack:  cześćotoprzykładowytekstpopolskuzeznakamiinterpunkcyjnymiikropkami 

====

Example of long plaintext in English:  Once upon a time I decrypt some texts.

Encrypted text with key 9:  xwlndyxwjcrvnrmnlahycbxvncngcb

Result of ciphertext-only attack:  onceuponatimeidecryptsometexts 

====

Now I will check how short of a word can be decrypted using this frequency analyzer.

100  3-letters long English words. Decryption succes rate:  13% 

100  4-letters long English words. Decryption succes rate:  27% 

100  5-letters long English words. Decryption succes rate:  23% 

150  6-letters long English words. Decryption succes rate:  49% 

200  7-letters long English words. Decryption succes rate:  45% 

200  8-letters long English words. Decryption succes rate:  52% 

200  9-letters long English words. Decryption succes rate:  63% 