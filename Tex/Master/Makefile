NAME = master
TEX  = master.tex chapter-1.tex chapter-2.tex chapter-3.tex chapter-4.tex chapter-5.tex chapter-6.tex chapter-7.tex
BIB  = ref.bib

all: ./$(NAME).pdf

./$(NAME).pdf: $(NAME).dvi
##	dvipdfmx -o $@ $(NAME)
	dvipdfmx $(NAME)
	rm -f $(NAME).aux $(NAME).log $(NAME).out $(NAME).toc $(NAME).dvi $(NAME).bbl $(NAME).blg

$(NAME).dvi: $(TEX) $(BIB)
	platex $(NAME); jbibtex $(NAME); platex $(NAME); platex $(NAME); pbibtex $(NAME)

clean:
	touch $(NAME).tex ; \rm ./$(NAME).pdf

