CC = g++
CXXFLAGS = -std=c++17

INCLUDE	=	-I/opt/homebrew/include \
			-I/usr/local/include \
			-I./lib \
			-I./lib/include \
			-I./lib/include/GLFW \
			-I$(VULKAN_SDK)/include

LIBS	=	-L/opt/homebrew/lib \
			-L/usr/local/lib \
			-L./lib/lib-arm64 \
			-L$(VULKAN_SDK)/lib \
			-lglfw3 \
			-lvulkan \

FRAMEWORKS = -framework Cocoa \
			-framework IOKit \
			-framework CoreFoundation \
			-framework CoreGraphics

# SRC = src/test.cpp
SRC	=	src/test.cpp

OBJ = $(SRC:.cpp=.o)
TARGET = vulkan_viewer

$(TARGET): $(OBJ)
	$(CC) $(CXXFLAGS) $(INCLUDE) -o $(TARGET) $(OBJ) $(LIBS) $(FRAMEWORKS)

%.o: %.cpp
	$(CC) $(CXXFLAGS) $(INCLUDE) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: clean
