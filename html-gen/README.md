
python -m pip install Markdown

import markdown
result = markdown.markdown('''
中文
'''.decode('utf-8'))

result = '''
<html>
<head>
<meta charset="utf-8">
</head>
<body>''' + result + '''
</body>
</html>
'''

