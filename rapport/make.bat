@ECHO OFF

pushd %~dp0

REM Genere le rapport Sphinx. Usage : make.bat html

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -m sphinx
)
set SOURCEDIR=source
set BUILDDIR=build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.La commande sphinx-build est introuvable. Installe les dependances avec :
	echo.    pip install -r requirements.txt
	echo.depuis la racine du depot.
	exit /b 1
)

if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
