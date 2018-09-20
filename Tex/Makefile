#自分の環境に合わせて設定
#bibファイル作成次第コメントアウトを戻してください
NAME = chukan2018 
TEX  = chukan2018.tex
BIB  = ref.bib 
#設定ここまで

all: ./$(NAME).pdf

./$(NAME).pdf: $(NAME).dvi
	dvipdfmx -o $@ $(NAME)

$(NAME).dvi: $(TEX) $(BIB)
	#通常
	#platex $(NAME); jbibtex $(NAME); platex $(NAME); platex $(NAME)
	platex $(NAME); bibtex $(NAME); platex $(NAME); platex $(NAME)
	#bibファイルをまだ作成していない場合
	#platex $(NAME); platex $(NAME); platex $(NAME)
clean:
	touch $(NAME).tex ; \rm ./$(NAME).pdf

