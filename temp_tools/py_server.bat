REM         Server base http folder now is public_html
REM         but can access parent folders as well

@echo off
cd public_html
@echo Starting Py Server on 8000
py_server.py
