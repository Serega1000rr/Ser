
def unicode_test(value):
	import unicodedata
	name = unicodedata.name(value)
	value2 = unicodedata.lookup(name)
	print('value="%s", name="%s", value2="%s"' % (value, name, value2))
unicode_test('\u00e9')
snowman = 'cafe\u2603'
ds = snowman.encode('utf-8')
print(ds)
print(ds.decode('latin-1'))
import html
print(html.unescape("&alpha;&xi;"))