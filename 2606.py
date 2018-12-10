Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> dir(os)
['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
>>> inFile = open ("Hey.txt","r")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    inFile = open ("Hey.txt","r")
FileNotFoundError: [Errno 2] No such file or directory: 'Hey.txt'
>>> inFile = open ("G:\pyprg\Hey","r")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    inFile = open ("G:\pyprg\Hey","r")
FileNotFoundError: [Errno 2] No such file or directory: 'G:\\pyprg\\Hey'
>>> inFile = open ("G:\\pyprg\Hey","r")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    inFile = open ("G:\\pyprg\Hey","r")
FileNotFoundError: [Errno 2] No such file or directory: 'G:\\pyprg\\Hey'
>>> inFile = open ("G:\\pyprg\Hey.txt","r")
>>> inFile = open ("G:\\pyprg\Hey.txt","r")
>>> fr = inFile.read()
>>> inFile.close()
>>> print(fr)
lol

>>> f = open("Hey.txt",w)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    f = open("Hey.txt",w)
NameError: name 'w' is not defined
>>> f = open ("G:\\pyprg\Hey.txt","w")
>>> f.writelines("Good Morning \n")
>>> f.writelines("How r u? ")
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x000001A8F24851F8>
>>> f.close()
>>> g = open ("G:\\pyprg\Hey.txt","r")
>>> inFile = open ("G:\\pyprg\Hey.txt","r")
>>> g = inFile.read()
>>> inFile.close()
>>> print(g)
Good Morning 
How r u? 
>>> f = open ("G:\\pyprg\Hey.txt","r")
>>> fr = f.readline()
>>> i = int(input("Which line : "))
Which line : 4
>>> i = int(input("Which line : "))
Which line : 1
>>> for x in range(1, i)
SyntaxError: invalid syntax
>>> for x in range(1, i):
	fr = f,readline()

>>> f.close()
>>> print(fr)
Good Morning 

>>>  os.path.isdir("G:\\pyprg")
 
SyntaxError: unexpected indent
>>> os.path.isdir("G:\\pyprg")
True
>>> os.path.exists("G:\\pyprg\2206.py")
False
>>> os.path.exists("G:\\pyprg\2506.py")
False
>>> os.path.exists("G:\\pyprg\2506")
False
>>> os.path.exists("G:\\pyprg\2206.py")
False
>>> os.path.exists("2206.py")
False
>>> os.path.exists("G:\\pyprg\Hey.txt")
True
>>> os.path.exists("G:\\pyprg\2206.py")
False
>>> os.path.exists("G:\\pyprg\2206")
False
>>> import glob
>>> glob.glob("G:\\pyprg\Hey.txt")
['G:\\pyprg\\Hey.txt']
>>> 
>>> os.stat("G:\\pyprg\2206.py")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    os.stat("G:\\pyprg\2206.py")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'G:\\pyprg\x906.py'
>>> os.stat("G:\\pyprg")
os.stat_result(st_mode=16895, st_ino=7599824371189491, st_dev=1421451685, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1530003541, st_mtime=1530003541, st_ctime=1529657541)
>>> os.path.exists("G:\\pyprg\.py")
False
>>> t=os.stat("d:\\sss")

import time

time.localtime(t.st_ctime)
