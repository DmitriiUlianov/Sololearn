'''
the .update() method updates the current set by adding items from another iterable, such as a set, list, tuple, or dictionary. 
It also removes any duplicates, ensuring that all the elements in the original set occur only once.
update() is available for sets and dictionaries.
Lists and tuples do not have an update() method.
'''

lang_soup = set()
lang_soup.update(2*'python' + 3*'html' + 2*'sql' + 4*'css')
print(len(lang_soup))

11 

'''
The expression 2 * 'python' + 3 * 'html' + 2 * 'sql' + 4 * 'css' concatenates into a single string: 'pythonpythonhtmlhtmlhtmlsqlsqlcsscsscsscss'
When passed to set.update(), this string is treated as a sequence of individual characters. The unique characters are: {'p', 'y', 't', 'h', 'o', 'n', 's', 'q', 'l', 'c'}
There are 11 unique characters here.
'''

lang_soup = set()
lang_soup.update(['python'] * 2 + ['html'] * 3 + ['sql'] * 2 + ['css'] *4)
print(len(lang_soup))

4

'''
['python'] * 2 + ['html'] * 3 + ['sql'] * 2 + ['css'] * 4 produces: ['python', 'python', 'html', 'html', 'html', 'sql', 'sql', 'css', 'css', 'css', 'css']
When added to lang_soup, it retains only the unique elements: {'python', 'html', 'sql', 'css'}
So, len(lang_soup) is 4.
'''
