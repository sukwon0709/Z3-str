default: all

# -------------------------------------------------------------------
# Change the path to the patched Z3 4.1.1 accordingly
# The directory indicated by this path should contain "lib" and "bin"
# e.g. "/home/z3_src_4.1.1"
# -------------------------------------------------------------------
Z3_path = /home/soh/git/Z3-str/z3

JUNK = str
SOURCE = *.cpp
INCLUDE = $(Z3_path)/lib
LIB = $(Z3_path)/bin/external

ifeq ($(shell uname -s), Darwin)
	CXX = g++-5
        FLAG = -O3 -std=c++11 -fopenmp
        LDFLAG = -lz3 -Wall
else
	CXX = g++
        FLAG = -O3 -std=c++11 -fopenmp
        LDFLAG = -lz3 -lrt -Wall -ldl
endif

%.o: %.cpp
	$(CXX) -g -O3 -std=c++11 -fPIC -I$(INCLUDE) $(CFLAGS) $< -c -o $@ -Wall

libz3str.so: strArgmt.o strAstReduce.o strTheory.o strRegex.o
	$(CXX) -shared -o $@ $^ -z defs \
		-Wl,--whole-archive $(LIB)/libz3.a -Wl,--no-whole-archive \
		-fopenmp -lrt

all: $(SOURCE)
	@echo ">> Z3 Source Dir: "$(Z3_path)
	@echo ""
	$(CXX) $(FLAG) -I$(INCLUDE) -L$(LIB) $(SOURCE) $(LDFLAG) -o str
	@echo ""
	
clean:
	rm -f $(JUNK) libz3str.so *.o
