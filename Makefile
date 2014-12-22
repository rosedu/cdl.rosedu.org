deploy:
	ssh cdl@rosedu.org "cd site-git-clone/cdl.rosedu.org; git checkout cdl-2015; git pull origin cdl-2015; cp -rf * /home/cdl/public_html/2015/."
