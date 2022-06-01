
joseph@jose-pc MINGW64 ~
$ ssh 6a37f91fa422@6a37f91fa422.b5e9b37f.alx-cod.online
6a37f91fa422@6a37f91fa422.b5e9b37f.alx-cod.online's password:
root@6a37f91fa422:/# cd alx-higher_level_programming
root@6a37f91fa422:/alx-higher_level_programming# cd 0x00-python-hello_world
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# cat > 4-print_float.py
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# chmod u+x 4-print_float.py
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git add .
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# commit -m 'Print float py'
bash: commit: command not found
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git commit -m 'Print float py'
[master b7971f2] Print float py
 1 file changed, 3 insertions(+)
 create mode 100755 0x00-python-hello_world/4-print_float.py
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git push
Username for 'https://github.com': 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
Password for 'https://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@github.com':
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 399 bytes | 399.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/BankoleJoseph12345/alx-higher_level_programming.git
   64f290a..b7971f2  master -> master
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# cat > 5-print_string.py
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[0:9])
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# chmod u+x 5-print_string.py
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git add .
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git commit -m 'Print string py'
[master 020f6b8] Print string py
 1 file changed, 4 insertions(+)
 create mode 100755 0x00-python-hello_world/5-print_string.py
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git push
Username for 'https://github.com': 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
Password for 'https://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@github.com':
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 402 bytes | 402.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/BankoleJoseph12345/alx-higher_level_programming.git
   b7971f2..020f6b8  master -> master
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# cat > 6-concat.py
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
s3 = '{} {}'.format(str1, str2)
print(f"Welcome to {s3}!")
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# chmod u+x 6-concat.py
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git add .
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git commit -m 'concat py'
[master 564c17f] concat py
 1 file changed, 5 insertions(+)
 create mode 100755 0x00-python-hello_world/6-concat.py
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# git push
Username for 'https://github.com': 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
Password for 'https://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@github.com':
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 425 bytes | 425.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/BankoleJoseph12345/alx-higher_level_programming.git
   020f6b8..564c17f  master -> master
root@6a37f91fa422:/alx-higher_level_programming/0x00-python-hello_world# cat > 7-edges.py
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
