# -*- encoding: utf8 -*-
# pypy -m pip install Markdown
# pypy html-gen.py

import os
import glob
from os import path
from shutil import copyfile
import markdown


FROM_PATH = path.abspath('../')
TO_PATH   = path.abspath('../../kasicass.github.io')
SKIP_DIRS = ('poem', 'html-gen',)

def getFiles(pattern):
	fromPath = path.join(FROM_PATH, pattern)
	return glob.glob(fromPath)

def genMarkdownToHTML(makedownFiles):
	# copy file to dest directory
	for filePath in markdownFiles:
		sourceDir, fileName = filePath.split(os.sep)[-2:]
		if sourceDir in SKIP_DIRS:
			continue

		print 'processing', filePath

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

def genIndexFile(markdownFiles):
	print 'generating index.html'

	mds = [filePath.split(os.sep)[-2:] for filePath in markdownFiles]
	mds = [path.join(*m) for m in mds]
	hrefs = [m.replace('.md', '.html') for m in mds]

	mds = ['* ['+m+']['+str(i+1)+']' for i, m in enumerate(mds)]
	hrefs = ['['+str(i+1)+']:'+h for i, h in enumerate(hrefs)]

	html = '# kasicass\' blog\n' + '\n'.join(mds) + '\n' + '\n'.join(hrefs)
	html = markdown.markdown(html.decode('utf-8'))
	html = '''
<html>
<head>
<meta charset="utf-8">
</head>
<body>''' + html + '''
</body>
</html>
'''

	indexFile = path.join(TO_PATH, 'index.html')
	with open(indexFile, 'w') as f:
		f.write(html.encode('utf-8'))

def copyFiles(fileList):
	for fromPath in fileList:
		print 'copying', fromPath

		toPath = fromPath.replace(FROM_PATH, TO_PATH)
		copyfile(fromPath, toPath)

if __name__ == '__main__':
	# md => html
	markdownFiles = getFiles('*/*.md')
	genMarkdownToHTML(markdownFiles)
	genIndexFile(markdownFiles)

	# copy *.png
	pngFiles = getFiles('*/*.png')
	copyFiles(pngFiles)

