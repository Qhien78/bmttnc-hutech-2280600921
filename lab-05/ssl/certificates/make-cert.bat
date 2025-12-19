@echo off
setlocal
cd /d %~dp0

set "PATH=%PATH%;C:\Program Files\OpenSSL-Win64\bin"

openssl req -new -x509 -newkey rsa:2048 -nodes ^
  -keyout server-key.key ^
  -out server-cert.crt ^
  -days 365 ^
  -config server-cert.cnf

pause
