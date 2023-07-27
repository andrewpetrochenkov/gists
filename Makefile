USERNAME:=$(shell git config user.name)
URL:=https://github.com/$(USERNAME)/gists

all:
	bash -l -c 'python3 scripts/data.py' # -l include env
	python3 scripts/readme.py
	python3 scripts/languages.py
	python3 scripts/tags.py
	bash -l -c 'python3 scripts/homepage.py'
	bash -l -c 'python3 scripts/topics.py'
	git add -A
	git commit -q -m ' '
	git push github -f --all
	open $(URL)
