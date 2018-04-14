# COMPILATION SETUP
MD := $(wildcard *.md)
PDF := $(patsubst %.md,pdf/%.pdf,$(MD))
all : pdf 
pdf : $(PDF)
pdf/%.pdf : %.md
	$ pandoc $< -o $@

.PHONY : clean

clean:
	@rm *pdf 
