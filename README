Helps you download a range of numbered files from a URL.

For example, running the following command

	dlurl.py 'http://host/filename-[01-10].jpg'
	
produces the following output that can be piped to a shell to perform the actual download.

	curl http://host/filename-01.jpg > filename-01.jpg
	curl http://host/filename-02.jpg > filename-02.jpg
	curl http://host/filename-03.jpg > filename-03.jpg
	curl http://host/filename-04.jpg > filename-04.jpg
	curl http://host/filename-05.jpg > filename-05.jpg
	curl http://host/filename-06.jpg > filename-06.jpg
	curl http://host/filename-07.jpg > filename-07.jpg
	curl http://host/filename-08.jpg > filename-08.jpg
	curl http://host/filename-09.jpg > filename-09.jpg
	curl http://host/filename-10.jpg > filename-10.jpg

This is identical to calling curl directly with the same pattern. You'll find this tool useful if you want to post-process the generated commands. For example, you could split the output into multiple scripts to easily download the files in parallel.  