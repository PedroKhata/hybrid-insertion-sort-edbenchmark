CXX = g++
CXXFLAGS = -O3 -Wall
PYTHON = python3
PIP = pip3

SRC_CPP_DIR = src/cpp
SRC_PY_DIR = src/python
BIN_DIR = src/bin
DATA_DIR = data

CPP_SOURCES = $(SRC_CPP_DIR)/main.cpp $(SRC_CPP_DIR)/LinkedList.cpp
CPP_TARGET = $(BIN_DIR)/engine_sort
PY_MAIN = $(SRC_PY_DIR)/main.py

.PHONY: all help run build clean install

all: help

help:
	@echo "==================================================================="
	@echo "Comandos disponíveis:"
	@echo "  make run      : Executa o main (Python)"
	@echo "  make build    : Compila o C++ isoladamente (para testes)"
	@echo "  make clean    : Limpa todos os executáveis, caches e logs gerados"
	@echo "  make install  : Instala as bibliotecas listadas no requirements.txt"
	@echo "==================================================================="

run:
	$(PYTHON) $(PY_MAIN)

build:
	mkdir -p $(BIN_DIR)
	$(CXX) $(CPP_SOURCES) -o $(CPP_TARGET) $(CXXFLAGS)

clean:
	rm -f $(CPP_TARGET)
	rm -rf $(SRC_PY_DIR)/__pycache__
	rm -rf .pytest_cache/
	rm -f $(DATA_DIR)/*_ordenados*.txt

install:
	$(PIP) install -r requirements.txt