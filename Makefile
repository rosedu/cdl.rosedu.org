deploy_unibuc:
	ssh cdl@rosedu.org "cd site-git-clone/cdl.rosedu.org/editions/unibuc_2013/; git pull origin master; cp -rf * /home/cdl/public_html/2013-unibuc/."

deploy_etti:
	ssh cdl@rosedu.org "cd site-git-clone/cdl.rosedu.org/editions/etti_2014/; git pull origin master; cp -rf * /home/cdl/public_html/2014-etti/."

deploy_extended:
	ssh cdl@rosedu.org "cd site-git-clone/cdl.rosedu.org/editions/extended_2014/; git pull origin master; cp -rf * /home/cdl/public_html/2014/."

