all:
	python3 generate.py > test.S
	gcc -o disasm src/riscv.c
	riscv64-unknown-elf-gcc -Wl,-Ttext=0x0 -nostdlib -o test.tmp test.s
	riscv64-unknown-elf-objcopy -O binary test.tmp test.bin
	./disasm > output.S
	python3 compare.py

clean:
	rm -rf test.*
	rm -rf output.*
	rm -rf disasm

.PHONY: all clean