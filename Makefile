deploy:
	ssh cdl@rosedu.org "cd site-git-clone/cdl.rosedu.org; git pull origin unibuc; cp -rf * /home/cdl/public_html/2013-unibuc/."
