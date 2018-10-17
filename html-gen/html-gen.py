# -*- encoding: utf8 -*-
# pypy -m pip install Markdown
# pypy html-gen.py

import os
import glob
from os import path
import markdown


FROM_PATH = path.abspath('../')
TO_PATH   = path.abspath('../../kasicass.github.io')
SKIP_DIRS = ('html-gen',)

if __name__ == '__main__':
	# get all markdown files
	fromPath = path.join(FROM_PATH, "*/*.md")
	markdownFiles = glob.glob(fromPath)

	# copy file to dest directory
	for filePath in markdownFiles:
		print 'processing', filePath

		sourceDir, fileName = filePath.split(os.sep)[-2:]
		if sourceDir in SKIP_DIRS:
			continue

		# make sure the dest dir is exists
		destDir = path.join(TO_PATH, sourceDir)
		if not path.isdir(destDir):
			os.makedirs(destDir)

		with open(filePath, 'r') as f:
			data = f.read()
			html = markdown.markdown(data.decode('utf-8'))

		html = '''
<html>
<head>
<meta charset="utf-8">
</head>
<body>''' + html + '''
</body>
</html>
'''

		destPath = path.join(destDir, fileName)
		destPath = destPath[:destPath.rfind('.')] + '.html'
		with open(destPath, 'w') as f:
			f.write(html.encode('utf-8'))

