Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> pattern = re.compile(r'[0-9]+')
>>> mystr = "football 3world0 cup to0 be champ7ion: france"
>>> data = re.fetchall(pattern, mystr)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data = re.fetchall(pattern, mystr)
AttributeError: module 're' has no attribute 'fetchall'
>>> data
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> data = re.fetchall(mystr, pattern)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data = re.fetchall(mystr, pattern)
AttributeError: module 're' has no attribute 'fetchall'
>>> data = re.fetchAll(mystr, pattern)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data = re.fetchAll(mystr, pattern)
AttributeError: module 're' has no attribute 'fetchAll'
>>> data = re.findall(mystr, pattern)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data = re.findall(mystr, pattern)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python36\lib\re.py", line 222, in findall
    return _compile(pattern, flags).findall(string)
TypeError: expected string or bytes-like object
>>> data = re.findall(pattern, mystr)
>>> data
['3', '0', '0', '7']
>>> mystr
'football 3world0 cup to0 be champ7ion: france'
>>> pattern = re.compile(r'[a-z]+')
>>> data = re.findall(pattern, mystr)
>>> data
['football', 'world', 'cup', 'to', 'be', 'champ', 'ion', 'france']
>>> sentence = "I LOve You"
>>> import re
>>> pattern = re.compile(r'[0-9 A-Z a-z]')
>>> sentence = "I07Love03YOu"
>>> data = re.findall(pattern, sentence)
>>> data
['I', '0', '7', 'L', 'o', 'v', 'e', '0', '3', 'Y', 'O', 'u']
>>> pattern = re.compile(r'[0-9 A-Z a-z]*')
>>> pattern = re.compile(r'[0-9 A-Z a-z]*')
>>> algo = re.compile(r'[0-9 A-Z]*')
>>> sent = "I loVe Ck0703)"
>>> data = re.findall(algo, sent)
>>> data
['I ', '', '', 'V', '', ' C', '', '0703', '', '']
>>> algo = re.compile(r'[0-9 A-Z]?')
>>> data = re.findall(algo, sent)
>>> data
['I', ' ', '', '', 'V', '', ' ', 'C', '', '0', '7', '0', '3', '', '']
>>> algo = re.compile(r'[0-9 A-Z]+')
>>> data = re.findall(algo, sent)
>>> data
['I ', 'V', ' C', '0703']
>>> 
algo = re.compile(r'[0-9 A-Z]?')
>>> algo = re.compile(r'[0-9]{10, 10}')
>>> mystr = "gfyugejhfb85458648723bhjbfv "
>>> data = re.findall(algo, mystr)
>>> datd
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    datd
NameError: name 'datd' is not defined
>>> data
[]
>>> mystr = "gfyugejhfb8545864872bhjbfv "
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> mystr = "gfyugejhfb7542003518bhjbfv "
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> algo = re.compile(r'[0-9]{10, 10}')
>>> mystr = "gourav7542003518kumar"
>>> data = findall(alo, mystr)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    data = findall(alo, mystr)
NameError: name 'findall' is not defined
>>> data = re.findall(alo, mystr)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    data = re.findall(alo, mystr)
NameError: name 'alo' is not defined
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> type(mystr)
<class 'str'>
>>> algo = re.compile(r'[0-9]{10, 10}')mystr = "gourav7542003518kumar"
SyntaxError: invalid syntax
>>> algo = re.compile(r'[0-9]{10, 10}')
>>> mystr = "gourav 7542003518kumar"
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> algo = re.compile(r'[0-9]{10, 10}')
>>> mystr = "gourav 7542003518 kumar"
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> algo = re.compile(r'[0-9]{9, 9}')
>>> mystr = "gourav 7542003518 kumar"
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> algo = re.compile(r'[0-9]{9, 9}')
>>> mystr = "gourav 7542003518 kumar 8002897033"
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> algo = re.compile(r'75[0-9]{8, 8}')
>>> mystr = "gourav 7542003518 kumar 8002897033"
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> algo = re.compile(r'75[0-9]{8, 8}')
>>> mystr = "gourav 7542003518 kumar 8002897033"
>>> data = re.findall(algo, mystr)
>>> data
[]
>>> import re
>>> a = re.compile(r'75[0-9]{8, 8}')
>>> b = "grv 7542003518 kmr"
>>> c = re.findall(a, b)
>>> c
[]
>>> pattern = re.compile(r'75[0-9]{8, 8}')
>>> mystr = "grv 7542003518 kmr"
>>> data = re.findall(pattern, mystr)
>>> data
[]
>>> pattern = re.compile(r'75[0-9]{8,8}')
>>> mystr = "grv 7542003518 kmr"
>>> data = re.findall(pattern, mystr)
>>> data
['7542003518']
>>> pattern = re.compile(r'^JH')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
['JH']
>>> pattern = re.compile(r'^J[0-9]')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
[]
>>> pattern = re.compile(r'[0-9]^J')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
[]
>>> pattern = re.compile(r'$[0-9]')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
[]
>>> pattern = re.compile(r'[0-9],$')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
[]
>>> 	pattern = re.compile(r'^|J')
	
SyntaxError: unexpected indent
>>> pattern = re.compile(r'^|J')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
['']
>>> pattern = re.compile(r'^|[A-Z]')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
['', 'H', 'W', 'B']
>>> pattern = re.compile(r'[A-Z]|$')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
['J', 'H', 'W', 'B', '']
>>> pattern = re.compile(r'[A-Z 0-1]|$')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
['J', 'H', '0', '1', ' ', 'W', 'B', '0', '']
>>> pattern = re.compile(r'([0-9]|$)')
>>> mystr = "JH01 WB02"
>>> data = re.findall(pattern, mystr)
>>> data
['0', '1', '0', '2', '']
>>> #reading internet data
>>> import urllib
>>> url = urllib.request.urlopen("http://whiznet.co.in/")
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    url = urllib.request.urlopen("http://whiznet.co.in/")
AttributeError: module 'urllib' has no attribute 'request'
>>> url = urllib.urlopen("http://whiznet.co.in/")
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    url = urllib.urlopen("http://whiznet.co.in/")
AttributeError: module 'urllib' has no attribute 'urlopen'
>>> import urllib
>>> url = urllib.request.urlopen("http://whiznet.co.in/")
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    url = urllib.request.urlopen("http://whiznet.co.in/")
AttributeError: module 'urllib' has no attribute 'request'
>>> import urllib.request
>>> url = urllib.request.urlopen("http://whiznet.co.in/")
>>> data = url.read()
>>> data
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag(\'js\', new Date());\n\n  gtag(\'config\', \'UA-16497263-21\');\n</script>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <meta name="author" content="">\n\n\n    <!-- Bootstrap Core CSS -->\n    <link href="css/bootstrap.min.css" rel="stylesheet">\n\t<link href="css/modern-business.css" rel="stylesheet">\n    <link href="font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n\n    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!-- WARNING: Respond.js doesn\'t work if you view the page via file:// -->\n    <!--[if lt IE 9]>\n        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\n        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>\n    <![endif]-->\n<link rel="stylesheet" href="font-mfizz/font-mfizz.css">\n<link rel="stylesheet" href="font-mfizz/font-awesome.css">\n\t<!--my css style-->\n\t<link rel="stylesheet" href="css/whiznet.css" type="text/css" />\n\t<link href="css/gv.css" rel="stylesheet">\n\t<link href="css/whiznet2.css" rel="stylesheet">\n\t\n\n\n\t<meta name="description" content="Whiznet Technologies,LLP Ranchi phone:+91 88048-78791 Software Development, Website Development and Training and Internship Programmes in High End Technologies">\n\t\t<meta name="keywords" content="Whiznet Technologies,LLP Ranchi phone:+91 88048-78791 Software Development, Website Development and Training and Internship Programmes in High End Technologies">\n\n    <title>Whiznet Technologies: Software Development and Training in Ranchi</title>\n</head>\n\n<body>\n\n    <!-- Navigation -->\n     <style>\n .playstore{\n  height:20%;\n }\n</style>\n<nav class="navbar navbar-inverse navbar-fixed-top navbar-shrink" role="navigation">\n    \n        \n         <div class=" row toprow" >\n\t\t     <div class=\'container toprow\'>\t     \n\t\t\t     <p>&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-facebook fa-1x"></i>&nbsp;&nbsp;\n\t\t\t\t  <i class="fa fa-twitter fa-1x"></i>&nbsp;&nbsp;\n\t\t\t\t  <i class="fa fa-linkedin fa-1x"></i>&nbsp;&nbsp;\n\t\t\t\t  <span class = \'text-center white pull-right\'><strong>&nbsp;&nbsp;+91 81026-29294</strong>&nbsp;&nbsp;&nbsp;</span></p>\n\t\t\t   </div>\n\t\t\n\t\t\t  \n\t\t\t</div>\n\n\n\n\n\n        <div class="row toprow2">\n\t\t  <div class="container">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="index.php"><img class="img-responsive logoimg" src="image/logo.png" alt=""></a>\n            </div>\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            \n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                <ul class="nav navbar-nav navbar-right">\n                    <li  id = \'dd\' class="dropdown ">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Training <b class="caret"></b></a>\n                        <ul class="dropdown-menu">\n                            <li>\n                                <a href="php-and-mysql-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp; PHP & MySQL</a>\n                            </li>\n                            <li>\n                                <a href="android-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp; Android</a>\n                            </li>\n\t\t\t\t\t\t\t<li>\n                                <a href="core-java-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Core Java</a>\n                            </li>\n\t\t\t\t\t\t\t\n                            <li>\n                                <a href="advanced-java-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Advanced Java</a>\n                            </li>\n                            <li>\n                                <a href="python-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Python</a>\n                            </li>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<li>\n                                <a href="ethical-hacking-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Ethical Hacking</a>\n                            </li>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<li>\n                                <a href="summer-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Summer Training</a>\n                            </li>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<li>\n                                <a href="industrial-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Industrial Training</a>\n                            </li>\n                            <li>\n                                <a href="r-programming-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;R Programming</a>\n                            </li>\n                            \n                            <li>\n                                <a href="final-year-software-project-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Final Year Software Projects</a>\n                            </li>\n                            \n                            \n                        </ul>\n                    </li>\n                    <li>\n                        <a href="consultancy.php">Consultancy</a>\n                    </li>\n                    <li>\n                        <a href="products.php">&nbsp;Products </a>\n                    </li>\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t<li>\n                        <a href="websites.php">&nbsp;Websites </a>\n                    </li>\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t <li>\n                        <a href="contact.php"><i class="fa fa-envelope-o"></i>&nbsp;  Contact us</a>\n                    </li>\n\t\t\t\t\t\n                </ul>\n            </div>\n            <!-- /.navbar-collapse -->\n\t\t\t</div>\n        </div>\n        \n        <div ><span class="white"> <marquee><h3>Hurry: Win Brand New Raspberry Pi 3 B, Join Summer Training Program : 15% discount on select courses. Last Date  31st May 2018. 10% discount on select courses Last Date  31st August(Limited batch Size).  Flat 20% discount on group admission (2 or more)</h3></marquee></div>\n    </nav>\n\t\n<br><br>\t \n\t\n\t<!--Navigation ends -->\n\t\n\t\n <style>\n.offer{\n      padding:2px;\n      position:absolute;\n      \n      top:50px;\n\t  right:2px;\n\t  background:rgba(0,0,255,.5);\n\t  width:100px;\n\t  height:100px;\n\n    -webkit-animation: mymove 10s infinite; /* Safari 4.0 - 8.0 */\n    animation: mymove 10s infinite;\n}\n#od{\n      padding:10px;\n      color:#fff;\n      \n\n    \n      \n      top:5px;\n\t  right:2px;\n\t  background:rgba(255,0,0,.5);\n\t  width:10px;\n\t  height:10px;\n\n    \n}\n\n\n\n\n\n\n\n\n\n/* Safari 4.0 - 8.0 */\n@-webkit-keyframes mymove# {\n    0%   {top: 50px;}\n    25%  {top: 200px;}\n    75%  {top: 50px}\n    100% {top: 100px;}\n}\n\n/* Standard syntax */\n@keyframes mymove {\n    0%   {top: 50px;}\n    25%  {top: 200px;}\n    75%  {top: 50px}\n    100% {top: 100px;}\n}\n\n</style>\n\n<div class="container">\n\t\n    <div class="col-sm-4 col-sm-offset-3">\n      <div class="row">\n      <div class="panel panel-danger">\n          \n      </div>\n      \n      </div>\n    </div>\n\n\t\n\t\n           \n    <div class="col-sm-9">\n\t\t<div class="row">\n\t\t   \n\t\t   \n\t\t<!--row1-col-1  -->\n\t\t\t\t\t\n\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t<a href="android-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color4 coursebox">\n\t\t\t\t\t\t<li class="list-group-item img4"> </li>\n\t\t\t\t\t\t<table class="table">\n\t\t\t\t\t\t<div class="panel-heading"><h4> Android App <br>Development</h4> </div>\n\t\t\t\t\t\t<tr> </tr>\n\t\t\t\t\t\t<tr>   <td> Duration:1 Month [50hrs]</td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 12000 </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t\t</table> \n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n                    \n                    \n\t\t\t\t</div>\n\t\t\t\t\n\t\t<!--row1 col-2  -->\n\t\t\t\t<div class="col-md-4">\n    \t\t\t\t\t  <a href="python-training-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img3"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4> Python <br>Programming </h4> </div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 8,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\n\t\t\t\t\t\t </div>\n\t\t\t\t\t\t </a>\n                         \n                         \n\t\t\t\t\t\t</div>\t\t\t\n\t\t   \n        <!-- row1 col3 -->\n\t\t\n             <div class="col-md-4">\n    \t\t\t\t\t  <a href="iot-training-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img22"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Internet of Things(IOT)</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [30 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 8,000</td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome<br><br> </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\n             \n             \n        \n\t</div>\n        <!--end of row 1 -->     \n        \n\t\t<!--row 2-->\n\t<div class="row">\n\t\t\n<!-- row 2-col 1 -->\n\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t<a href="big-data-hadoop-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color5 coursebox">\n                        <li class="list-group-item img21"> </li>\n\t\t\t\t\t    <table class="table"> \n\t\t\t\t\t\t<div class="panel-heading"><h4>Big Data <br>& Hadoop Training</h4> </div>\n\t\t\t\t\t    <tr> </tr>\n\t\t\t\t\t    <tr><td> Duration:2 Month [80 Hrs]</td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 16,000 </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t   \n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n                    \n\t\t\t\t</div>\n<!--row 2 col2-->\n\n    \n\n\t<div class="col-md-4">\n\t\t\t\t\t<a href="advanced-java-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color5 coursebox">\n                        <li class="list-group-item img5"> </li>\n\t\t\t\t\t    <table class="table"> \n\t\t\t\t\t\t<div class="panel-heading"><h4>Advance Java <br>Programming</h4> </div>\n\t\t\t\t\t    <tr> </tr>\n\t\t\t\t\t    <tr><td> Duration:1 Month [50 Hrs]</td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 10,000</td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t   \n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n                \t\t\t\t\t</a>\n                                  \n                \n                \n\t\t\t\t</div>\n\n\t<!--row2 col 3-->\n\t\n\t\t<div class="col-md-4">\n\t\t\n\t\t\t\t\t<a href="core-java-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color6 coursebox">\n                        <li class="list-group-item img6"> </li>\n\t\t\t\t\t\t<table class="table">\n\t\t\t\t\t\t<div class="panel-heading"><h4>Core Java <br>Programming</h4> </div>\n\t\t\t\t\t  \n\t\t\t\t\t\t<tr><td> Duration: 1 month [40 Hrs] </td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 5,000 </td> </tr>\n\t\t\t\t\t\t<tr> <td><button type="submit" class="btn btn-success width-b">Sun Certified Faculty</button></td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n                            \n                \n\t\t</div>\t\n\t\n\t\n    </div>\n\t<!-- row 2 ends -->\n\t\n\t\n\t<!-- row3-->\n\n\t<div class="row">\t\t\t\n\t\t   \n\t<!--row 3 col 1  -->\n\t\t\t\t\t\n\t\t<div class="col-md-4">\n\t\t\t<a href="php-and-mysql-training-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t<ul class="list-group color coursebox">\n                     \n\t\t\t\t\t\t<li class="list-group-item img1"> </li>\n\t\t\t\t\t \n\t\t\t\t\t\t<table class="table">\n\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel-heading"><h4> PHP and MySQL <br>Programming </h4> </div>\t\t\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\t<tr><td> Duration:1 Month [50 Hrs]  </td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 10,000  </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul> \n\t\t\t\t\t\t</div></a>\n                               \n                \n                        \n\t\t</div>\n\t\t\t\n\t<!--row3 col2  -->\n\t\t\t\t\t \n\t\t\t \n\t\t<div class="col-md-4 ">\n\t\t\t\t\t<a href="ethical-hacking-in-ranchi.php"><div class="panel-body  ">\n\t\t\t\t\t\t<ul class="list-group color2 coursebox">\n\t\t\t\t\t    <li class="list-group-item img7"> </li>\n\t\t\t\t\t\t<table class="table"> \n\t\t\t\t\t\t<div class="panel-heading"> <h4>Foundation Program for Ethical <br> Hacking</h4> </div>\t\n\t\t\t\t\t\t<tr><td> Duration:1 Month </td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 6,000 </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t    </table>\n\t\t\t\t\t    </ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n\t\t</div>\n\t<!--row3 col3  -->\n\t\n\t\t<div class="col-md-4">\n\t\t\t\t\t\t  <a href="web-designing-course-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img11"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4> Web Designing </h4> </div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:2 Months [60 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 6,500</td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n                 \n                        \n                \n\t\t</div>\t\t\t\n\t\n\t</div>\n\t<!-- end of row>\n\t\n\t<div class="row">\n\t\n\t<!-- row4 col1-->\n\t\t<div class="col-md-4">\n\t\t\t<a href=" C-Data-Structure-and-C++-course-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t<ul class="list-group color3 coursebox">\n                    <li class="list-group-item img12"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>C, Data Structure and  C++</h4> </div>\n\t\t\t\t              <tr><td> Duration:2 Months [80 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i>  3500/ module </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n                         \n                \n\t\t</div>\t\n\t<!--row4 col 2>\n\n        <div class="col-md-4">\n\t\t\t<a href="rdbms-with-Oracle-11g-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t    <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img13"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>RDBMS with Oracle 11g,DBA Basics</h4> \n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Months [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 6,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t</div>\t\n           \n\t<!-- row4 col3-->\n\t\t<div class="col-md-4">\n\t\t\t<a href="linux-shell-scripting.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color2 coursebox">\n                           <li class="list-group-item img14"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Linux and Shell Scripting</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 5,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\t\t\n\t\t\n\t\t\n\t\t<div class="col-md-4">\n\t\t\t\t\t\t  <a href="final-year-software-project-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color6 coursebox">\n                           <li class="list-group-item img17"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Final year Software Projects</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 -3 Months </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 4,000-10000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\n\n                    \n               \n\t<!-- end of row>\n\t\n\t<div class="row">\n\t\n\t<!-- row4 col1-->\n\t\t<div class="col-md-4">\n    \t\t\t\t\t  <a href="r-programming-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img16"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>R Programming</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [30 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 8,000 (Early Bird Fee <i class="fa fa-inr"></i> 7000 )</td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome<br><br> </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\n\t<!--row4 col 2>\n\n        <div class="col-md-4">\n\t\t\t<a href="rdbms-with-Oracle-11g-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t    <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img13"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>RDBMS with Oracle 11g,DBA Basics</h4> \n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Months [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 6,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t</div>\t\n           \n\t<!-- row4 col3-->\n\t\t<div class="col-md-4">\n\t\t\t<a href="linux-shell-scripting.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color2 coursebox">\n                           <li class="list-group-item img14"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Linux and Shell Scripting</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 5,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\t\t\n\t\t\n\t\t\n\t\t<div class="col-md-4">\n\t\t\t\t\t\t  <a href="final-year-software-project-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color6 coursebox">\n                           <li class="list-group-item img17"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Final year Software Projects</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 -3 Months </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 4,000-10000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\n\n\n\n               \n\n\n\t\n\t\t</div>\n\t\t\n\t\t<!-- ../row-->\n\t\t\n\n\n                 \n\n              \n\t\t\n\t</div>\n\t\t\n\n\n               \n\n\n\n\n\n\n\n\n\t\n\t\t\n\n\t </div>\n\t\t\n\t\t\n\t\t\t\t\n\t\t\t<div class="col-md-3 affix">\n               \n\t\t\t\t<div class="panel panel-default query_form_bg">\n\t\t\t\t\t\n\t\t\t\t\t<div class=" panel-heading fa fa-phone 2px width-panel">\n\t\t\t\t\t<strong>  &nbsp;+91-81026-29294</strong>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="panel-heading"><a target="_blank" href="https://play.google.com/store/apps/details?id=in.co.whiznet.whiznet">\n                    <img src="playstore.png" class="responsive playstore" ></a></div>\n\t\t\t\t\t\n\t\t\t\t\t<div class="panel-heading" style="color:#10893f"><b>Enquiry Form </b></div>\n\t\t\t\t\t<div id ="success" class=" panel-body query_form_bg">\n\t\t\t\t\t<form class="form-horizontal" name="sentMessage" id="contactForm" role="form">\n\t\t\t\t\t\t<div class="form-group"> \n\t\t\t\t\t\t\t<div class="col-sm-12  ">\n\t\t\t\t\t\t\t\t<input type="text" class="form-control" id="name" placeholder="Your Name"/>\n                                                                <input type="hidden" id="course" value=\'\' > \n\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t</div>\n   \n   \n   \n   \n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<input type="number" class="form-control" id="phone" placeholder="Phone No"/>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<input type="email" class="form-control" id="email" placeholder="Email Address"/>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<textarea  cols="10" rows="2"type="number" class="form-control" id="message" placeholder="Your Query?"></textarea>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n  \n   \n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<button type="submit" class="btn btn-primary width-b">Submit Query</button>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</form>\n\t\t\t\t\t</div>\n                </div>\n\t\t\t\t\n\t\t\t</div>\t\t\t\n            \n\t\t\t\n\t\t\t</div>\n\n\n\n\n\n\n\n\n <div class="row1" style="background:#C2D8B1;">\t\t\t\t\t\n\t  <div class="container ">\n\n        <div class="col-md-9 table-responsive ">\t  \n\t     <h3>New Batches</h3>\n\t     <table class="table table-striped hidden ">\n   \n\t\t\t\t\t\t<thead >\n\t\t\t\t\t\t<tr class="course_table_row">\n\t\t\t\t\t\t<th>Course</th>\n\t\t\t\t\t\t<th>Starts</th>\n\t\t\t\t\t\t<th>Ends</th>\n\t\t\t\t\t\t<th>Days</th>\n\t\t\t\t\t\t<th>Time</th>\n\t\t\t\t\t\t<th>Price</th>\n\t\t\t\t\t\t\n\t\t\t\t\t\t<th></th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</thead>\n   \n\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-java fa-3x"> </i>Advance Java</td>\n\t\t\t\t\t\t<td>4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>700AM-0930AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-php fa-3x"> </i><i class="icon-mysql fa-3x"> </i>PHP & MySQL</td>\n\t\t\t\t\t\t<td >4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>930AM-1130AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-android fa-3x"></i>Android</td>\n\t\t\t\t\t\t<td>4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>We,Thu,Fr,Sa</td>\n\t\t\t\t\t\t<td>1200AM-0200PM</td>\n\t\t\t\t\t\t<td>INR 11500</td>\n\t\t\t\t\t\t<td>INR 9775</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3 "><i class="icon-python fa-3x"> </i>Python</td>\n\t\t\t\t\t\t<td>4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>Mo,Tue,Wed,Sat</td>\n\t\t\t\t\t\t<td>0230PM-0430PM</td>\n\t\t\t\t\t\t<td>INR 4500</td>\n\t\t\t\t\t\t<td>INR 3825</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n   \n\t\t\t\t\t\t<table  class="table table-striped hidden">\n\t\t\t\t\t\t<br/>\n\t\t\t\t\t\t\t\n\t<thead>\n\t\t\t\t\t\t<tr><strong class="hidden">15% EARLYBIRD OFF (EXPIRES ON 20th May) </strong></tr>\n\t\t\t\t\t\t<tr><strong > For New Batches Contact <span > <big>+91-81026-29294</big></span></strong></tr><br/> <br/>\n\t\t\t\t\t\t<tr><strong > Fill Up the Enquiry Form </strong></tr>\n\t\t\t\t\t\t</thead>\t\t\t\t\t\t\n\t\t\t\t\t\n\t<br/><br/><br/>\n\t     <table class="table table-striped hidden">\n   \n\t\t\t\t\t\t<thead>\n\t\t\t\t\t\t<tr class="course_table_row">\n\t\t\t\t\t\t<th>Course</th>\n\t\t\t\t\t\t<th>Starts</th>\n\t\t\t\t\t\t<th>Ends</th>\n\t\t\t\t\t\t<th>Days</th>\n\t\t\t\t\t\t<th>Time</th>\n\t\t\t\t\t\t<th>Price</th>\n\t\t\t\t\t\t<th>15% EarlyBird Off[Ends 20Apr 2015]</th>\n\t\t\t\t\t\t<th></th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</thead>\n   \n\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-java fa-3x"> </i>Advance Java</td>\n\t\t\t\t\t\t<td>1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>700AM-0930AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-php fa-3x"> </i><i class="icon-mysql fa-3x"> </i>PHP & MySQL</td>\n\t\t\t\t\t\t<td >1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>930AM-1130AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-android fa-3x"></i>Android</td>\n\t\t\t\t\t\t<td>1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>We,Thu,Fr,Sa</td>\n\t\t\t\t\t\t<td>1200AM-0200PM</td>\n\t\t\t\t\t\t<td>INR 11500</td>\n\t\t\t\t\t\t<td>INR 9775</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3 "><i class="icon-python fa-3x"> </i>Python</td>\n\t\t\t\t\t\t<td>1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>Mo,Tue,Wed,Sat</td>\n\t\t\t\t\t\t<td>0230PM-0430PM</td>\n\t\t\t\t\t\t<td>INR 4500</td>\n\t\t\t\t\t\t<td>INR 3825</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t</table>\n\t     \n\t  </div>\n\t  </div>\n\t </div>\n\t \n\t \n\t  <div class="row4" style="background:#B4D2A0">\t\t\t\t\t\n\t  <div class="container">\t\t\t\t\n\t\t<div class="col-md-9">\t\t\t\n\t\t\t\t\t\t<p class="text-h-f">Course Features:</p>\t\n\t\t\t\t\t\n\t\t\t\t<div class="panel-group" id="accordion">\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\n\t\t\t\t\t\t\t\t\t  Instructor Led Live Class Room Training\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseOne" class="panel-collapse collapse in">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\t  All course modules are designed to provide in-depth knowledge of the subject.\n\t\t\t\t\t\t\t\t  Training program is for the given number of hours.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\n\t\t\t\t\t\t\t\t\t\tAssignments\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseTwo" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tFor each course there will be a number of assignments. Completed assignments has\n\t\t\t\t\t\t\t\tto be uploaded on the website within the stipulated time-frame.Assignments will be evaluated\n\t\t\t\t\t\t\t\tand the marks will be calculated for the final grade.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div> \n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\n\t\t\t\t\t\t\t\t\t\t  Tests\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseThree" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tAll program consists of number of tests which will be evaluated and marks will be\n\t\t\t\t\t\t\t\tadded for the calculation of final grade.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseFour">\n\t\t\t\t\t\t\t\t\t\t  Lifetime Access\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseFour" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tAll successful candidates will get life-time access to our learning management system.\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseSix">\n\t\t\t\t\t\t\t\t\t\t   Get Certified\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseSix" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tUpon completion of all the modules,assignments,tests and final project you will be awarded with\n\t\t\t\t\t\t\t\tcertificate with the grade you achieved.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t<!--coln-3 close right-->\n\t\t\t</div>\n        </div>\n\t\t\n\t\t\n\t\t\n\t<!-- Marketing Icons Section top row /-->\t\n\t</div>\n\n\n        \n\n\t    \n\n    <!-- Header Carousel -->\n    \n    <!-- Page Content -->\n\n\t\n\t<!-- page content ends here -->\n  \n    <!-- footer -->\n    <div class="footer">\n\t \n\t\t<div class="container">\n\t  \n\t\t\n\t\t\t\t<div class="col-lg-3">\n\t\t\t\t\t<div class="panel panel-body nobg">\n\t\t\t\t\t<Strong class="foot-h-font">Quick Links</strong><br/>\n\t\t\t\t\t<a href="courses.php"><i class="fa fa-angle-right"></i>&nbsp Courses<br/></a>\n\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp Blog <br/>\n\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp Clients<br/>\n\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp My Whiznet<br/>\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\t<div class="col-lg-3">\n\t\t\t\t\t<div class="panel panel-body nobg">\n\t\t\t\t\t<img src="image/logo2.png" class="img-rounded img-responsive">\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<div class="col-lg-3">\n\t\t\t\t\t<div class="panel panel-body nobg">\n\t\t\t\t\t<strong class="foot-h-font">Whiznet Technologies</strong><br/>\n\t\t\t\t<u>Development and Training</u><br/>\n    \t\t\t\tRS Tower<br/>\n\t\t\t\t\t 3rd Floor<br/>\n\t\t\t\t\t Circular Road<br/>\n\t\t\t\t\t Ranchi<br/>\n\t\t\t\t\t Jharkhand<br/>\n\t\t\t\t\t (India)<br/>\n                     \n                     \n        \t\t\t\n                     \n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\n\t\t\n\t </div>\n\t \n\t <div class="container">\n\t   <div><p>&copy;  2017 Whiznet Technologies, LLP</div>\n\t </div>\n</div>\n\n\n\n    <!--footer ends here -->\t\n  \n\t  \n\t  \n\t  \n\t  \n<!--container top close-->\t  \n    \n\t\n\t\n    <!-- /.container -->\n\n    <!-- jQuery -->\n    <script src="js/jquery.js"></script>\n\n    <!-- Bootstrap Core JavaScript -->\n    <script src="js/bootstrap.min.js"></script>\n\t <script src="js/jqBootstrapValidation.js"></script>\n    <script src="js/contact_me.js"></script>\n\n    <!-- Script to Activate the Carousel -->\n    <script>\n    $(\'.carousel\').carousel({\n        interval: 5000 //changes the speed\n    })\n    </script>\n\n\t\n\t\n\n\t\n\t\n\t\n\t<script type="text/javascript">\n   $(function () { $(\'#collapseFour\').collapse({\n      toggle: false\n   })});\n   $(function () { $(\'#collapseTwo\').collapse(\'show\')});\n   $(function () { $(\'#collapseThree\').collapse(\'toggle\')});\n   $(function () { $(\'#collapseOne\').collapse(\'hide\')});\n</script>  \n\n<script src = "js/whiznet.js"></script>\n\n<script>\n  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n  })(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');\n\n  ga(\'create\', \'UA-16497263-21\', \'auto\');\n  ga(\'send\', \'pageview\');\n\n</script>\n</body>\n\n</html>'
>>> import urllib.request
>>> url = urllib.request.urlopen("http://whiznet.co.in/")
>>> url = urllib.request.urlopen("http://whiznet.co.in/\n")
>>> data = url.read()
>>> data
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag(\'js\', new Date());\n\n  gtag(\'config\', \'UA-16497263-21\');\n</script>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <meta name="author" content="">\n\n\n    <!-- Bootstrap Core CSS -->\n    <link href="css/bootstrap.min.css" rel="stylesheet">\n\t<link href="css/modern-business.css" rel="stylesheet">\n    <link href="font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n\n    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!-- WARNING: Respond.js doesn\'t work if you view the page via file:// -->\n    <!--[if lt IE 9]>\n        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\n        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>\n    <![endif]-->\n<link rel="stylesheet" href="font-mfizz/font-mfizz.css">\n<link rel="stylesheet" href="font-mfizz/font-awesome.css">\n\t<!--my css style-->\n\t<link rel="stylesheet" href="css/whiznet.css" type="text/css" />\n\t<link href="css/gv.css" rel="stylesheet">\n\t<link href="css/whiznet2.css" rel="stylesheet">\n\t\n\n\n\t<meta name="description" content="Whiznet Technologies,LLP Ranchi phone:+91 88048-78791 Software Development, Website Development and Training and Internship Programmes in High End Technologies">\n\t\t<meta name="keywords" content="Whiznet Technologies,LLP Ranchi phone:+91 88048-78791 Software Development, Website Development and Training and Internship Programmes in High End Technologies">\n\n    <title>Whiznet Technologies: Software Development and Training in Ranchi</title>\n</head>\n\n<body>\n\n    <!-- Navigation -->\n     <style>\n .playstore{\n  height:20%;\n }\n</style>\n<nav class="navbar navbar-inverse navbar-fixed-top navbar-shrink" role="navigation">\n    \n        \n         <div class=" row toprow" >\n\t\t     <div class=\'container toprow\'>\t     \n\t\t\t     <p>&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-facebook fa-1x"></i>&nbsp;&nbsp;\n\t\t\t\t  <i class="fa fa-twitter fa-1x"></i>&nbsp;&nbsp;\n\t\t\t\t  <i class="fa fa-linkedin fa-1x"></i>&nbsp;&nbsp;\n\t\t\t\t  <span class = \'text-center white pull-right\'><strong>&nbsp;&nbsp;+91 81026-29294</strong>&nbsp;&nbsp;&nbsp;</span></p>\n\t\t\t   </div>\n\t\t\n\t\t\t  \n\t\t\t</div>\n\n\n\n\n\n        <div class="row toprow2">\n\t\t  <div class="container">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="index.php"><img class="img-responsive logoimg" src="image/logo.png" alt=""></a>\n            </div>\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            \n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                <ul class="nav navbar-nav navbar-right">\n                    <li  id = \'dd\' class="dropdown ">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Training <b class="caret"></b></a>\n                        <ul class="dropdown-menu">\n                            <li>\n                                <a href="php-and-mysql-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp; PHP & MySQL</a>\n                            </li>\n                            <li>\n                                <a href="android-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp; Android</a>\n                            </li>\n\t\t\t\t\t\t\t<li>\n                                <a href="core-java-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Core Java</a>\n                            </li>\n\t\t\t\t\t\t\t\n                            <li>\n                                <a href="advanced-java-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Advanced Java</a>\n                            </li>\n                            <li>\n                                <a href="python-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Python</a>\n                            </li>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<li>\n                                <a href="ethical-hacking-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Ethical Hacking</a>\n                            </li>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<li>\n                                <a href="summer-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Summer Training</a>\n                            </li>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<li>\n                                <a href="industrial-training-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Industrial Training</a>\n                            </li>\n                            <li>\n                                <a href="r-programming-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;R Programming</a>\n                            </li>\n                            \n                            <li>\n                                <a href="final-year-software-project-in-ranchi.php"><i class=\'fa fa-angle-right fa-color\'></i>&nbsp;Final Year Software Projects</a>\n                            </li>\n                            \n                            \n                        </ul>\n                    </li>\n                    <li>\n                        <a href="consultancy.php">Consultancy</a>\n                    </li>\n                    <li>\n                        <a href="products.php">&nbsp;Products </a>\n                    </li>\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t<li>\n                        <a href="websites.php">&nbsp;Websites </a>\n                    </li>\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t <li>\n                        <a href="contact.php"><i class="fa fa-envelope-o"></i>&nbsp;  Contact us</a>\n                    </li>\n\t\t\t\t\t\n                </ul>\n            </div>\n            <!-- /.navbar-collapse -->\n\t\t\t</div>\n        </div>\n        \n        <div ><span class="white"> <marquee><h3>Hurry: Win Brand New Raspberry Pi 3 B, Join Summer Training Program : 15% discount on select courses. Last Date  31st May 2018. 10% discount on select courses Last Date  31st August(Limited batch Size).  Flat 20% discount on group admission (2 or more)</h3></marquee></div>\n    </nav>\n\t\n<br><br>\t \n\t\n\t<!--Navigation ends -->\n\t\n\t\n <style>\n.offer{\n      padding:2px;\n      position:absolute;\n      \n      top:50px;\n\t  right:2px;\n\t  background:rgba(0,0,255,.5);\n\t  width:100px;\n\t  height:100px;\n\n    -webkit-animation: mymove 10s infinite; /* Safari 4.0 - 8.0 */\n    animation: mymove 10s infinite;\n}\n#od{\n      padding:10px;\n      color:#fff;\n      \n\n    \n      \n      top:5px;\n\t  right:2px;\n\t  background:rgba(255,0,0,.5);\n\t  width:10px;\n\t  height:10px;\n\n    \n}\n\n\n\n\n\n\n\n\n\n/* Safari 4.0 - 8.0 */\n@-webkit-keyframes mymove# {\n    0%   {top: 50px;}\n    25%  {top: 200px;}\n    75%  {top: 50px}\n    100% {top: 100px;}\n}\n\n/* Standard syntax */\n@keyframes mymove {\n    0%   {top: 50px;}\n    25%  {top: 200px;}\n    75%  {top: 50px}\n    100% {top: 100px;}\n}\n\n</style>\n\n<div class="container">\n\t\n    <div class="col-sm-4 col-sm-offset-3">\n      <div class="row">\n      <div class="panel panel-danger">\n          \n      </div>\n      \n      </div>\n    </div>\n\n\t\n\t\n           \n    <div class="col-sm-9">\n\t\t<div class="row">\n\t\t   \n\t\t   \n\t\t<!--row1-col-1  -->\n\t\t\t\t\t\n\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t<a href="android-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color4 coursebox">\n\t\t\t\t\t\t<li class="list-group-item img4"> </li>\n\t\t\t\t\t\t<table class="table">\n\t\t\t\t\t\t<div class="panel-heading"><h4> Android App <br>Development</h4> </div>\n\t\t\t\t\t\t<tr> </tr>\n\t\t\t\t\t\t<tr>   <td> Duration:1 Month [50hrs]</td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 12000 </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t\t</table> \n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n                    \n                    \n\t\t\t\t</div>\n\t\t\t\t\n\t\t<!--row1 col-2  -->\n\t\t\t\t<div class="col-md-4">\n    \t\t\t\t\t  <a href="python-training-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img3"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4> Python <br>Programming </h4> </div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 8,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\n\t\t\t\t\t\t </div>\n\t\t\t\t\t\t </a>\n                         \n                         \n\t\t\t\t\t\t</div>\t\t\t\n\t\t   \n        <!-- row1 col3 -->\n\t\t\n             <div class="col-md-4">\n    \t\t\t\t\t  <a href="iot-training-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img22"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Internet of Things(IOT)</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [30 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 8,000</td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome<br><br> </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\n             \n             \n        \n\t</div>\n        <!--end of row 1 -->     \n        \n\t\t<!--row 2-->\n\t<div class="row">\n\t\t\n<!-- row 2-col 1 -->\n\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t<a href="big-data-hadoop-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color5 coursebox">\n                        <li class="list-group-item img21"> </li>\n\t\t\t\t\t    <table class="table"> \n\t\t\t\t\t\t<div class="panel-heading"><h4>Big Data <br>& Hadoop Training</h4> </div>\n\t\t\t\t\t    <tr> </tr>\n\t\t\t\t\t    <tr><td> Duration:2 Month [80 Hrs]</td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 16,000 </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t   \n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n                    \n\t\t\t\t</div>\n<!--row 2 col2-->\n\n    \n\n\t<div class="col-md-4">\n\t\t\t\t\t<a href="advanced-java-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color5 coursebox">\n                        <li class="list-group-item img5"> </li>\n\t\t\t\t\t    <table class="table"> \n\t\t\t\t\t\t<div class="panel-heading"><h4>Advance Java <br>Programming</h4> </div>\n\t\t\t\t\t    <tr> </tr>\n\t\t\t\t\t    <tr><td> Duration:1 Month [50 Hrs]</td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 10,000</td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t   \n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n                \t\t\t\t\t</a>\n                                  \n                \n                \n\t\t\t\t</div>\n\n\t<!--row2 col 3-->\n\t\n\t\t<div class="col-md-4">\n\t\t\n\t\t\t\t\t<a href="core-java-training-in-ranchi.php">\n\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<ul class="list-group color6 coursebox">\n                        <li class="list-group-item img6"> </li>\n\t\t\t\t\t\t<table class="table">\n\t\t\t\t\t\t<div class="panel-heading"><h4>Core Java <br>Programming</h4> </div>\n\t\t\t\t\t  \n\t\t\t\t\t\t<tr><td> Duration: 1 month [40 Hrs] </td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 5,000 </td> </tr>\n\t\t\t\t\t\t<tr> <td><button type="submit" class="btn btn-success width-b">Sun Certified Faculty</button></td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n                            \n                \n\t\t</div>\t\n\t\n\t\n    </div>\n\t<!-- row 2 ends -->\n\t\n\t\n\t<!-- row3-->\n\n\t<div class="row">\t\t\t\n\t\t   \n\t<!--row 3 col 1  -->\n\t\t\t\t\t\n\t\t<div class="col-md-4">\n\t\t\t<a href="php-and-mysql-training-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t<ul class="list-group color coursebox">\n                     \n\t\t\t\t\t\t<li class="list-group-item img1"> </li>\n\t\t\t\t\t \n\t\t\t\t\t\t<table class="table">\n\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel-heading"><h4> PHP and MySQL <br>Programming </h4> </div>\t\t\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\t<tr><td> Duration:1 Month [50 Hrs]  </td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 10,000  </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t</ul> \n\t\t\t\t\t\t</div></a>\n                               \n                \n                        \n\t\t</div>\n\t\t\t\n\t<!--row3 col2  -->\n\t\t\t\t\t \n\t\t\t \n\t\t<div class="col-md-4 ">\n\t\t\t\t\t<a href="ethical-hacking-in-ranchi.php"><div class="panel-body  ">\n\t\t\t\t\t\t<ul class="list-group color2 coursebox">\n\t\t\t\t\t    <li class="list-group-item img7"> </li>\n\t\t\t\t\t\t<table class="table"> \n\t\t\t\t\t\t<div class="panel-heading"> <h4>Foundation Program for Ethical <br> Hacking</h4> </div>\t\n\t\t\t\t\t\t<tr><td> Duration:1 Month </td></tr>\n\t\t\t\t\t\t<tr> <td><i class="fa fa-inr"></i> 6,000 </td> </tr>\n\t\t\t\t\t\t<tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t    </table>\n\t\t\t\t\t    </ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</a>\n\t\t</div>\n\t<!--row3 col3  -->\n\t\n\t\t<div class="col-md-4">\n\t\t\t\t\t\t  <a href="web-designing-course-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img11"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4> Web Designing </h4> </div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:2 Months [60 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 6,500</td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n                 \n                        \n                \n\t\t</div>\t\t\t\n\t\n\t</div>\n\t<!-- end of row>\n\t\n\t<div class="row">\n\t\n\t<!-- row4 col1-->\n\t\t<div class="col-md-4">\n\t\t\t<a href=" C-Data-Structure-and-C++-course-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t<ul class="list-group color3 coursebox">\n                    <li class="list-group-item img12"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>C, Data Structure and  C++</h4> </div>\n\t\t\t\t              <tr><td> Duration:2 Months [80 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i>  3500/ module </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n                         \n                \n\t\t</div>\t\n\t<!--row4 col 2>\n\n        <div class="col-md-4">\n\t\t\t<a href="rdbms-with-Oracle-11g-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t    <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img13"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>RDBMS with Oracle 11g,DBA Basics</h4> \n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Months [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 6,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t</div>\t\n           \n\t<!-- row4 col3-->\n\t\t<div class="col-md-4">\n\t\t\t<a href="linux-shell-scripting.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color2 coursebox">\n                           <li class="list-group-item img14"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Linux and Shell Scripting</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 5,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\t\t\n\t\t\n\t\t\n\t\t<div class="col-md-4">\n\t\t\t\t\t\t  <a href="final-year-software-project-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color6 coursebox">\n                           <li class="list-group-item img17"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Final year Software Projects</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 -3 Months </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 4,000-10000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\n\n                    \n               \n\t<!-- end of row>\n\t\n\t<div class="row">\n\t\n\t<!-- row4 col1-->\n\t\t<div class="col-md-4">\n    \t\t\t\t\t  <a href="r-programming-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img16"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>R Programming</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [30 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 8,000 (Early Bird Fee <i class="fa fa-inr"></i> 7000 )</td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome<br><br> </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\n\t<!--row4 col 2>\n\n        <div class="col-md-4">\n\t\t\t<a href="rdbms-with-Oracle-11g-in-ranchi.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t    <ul class="list-group color3 coursebox">\n                           <li class="list-group-item img13"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>RDBMS with Oracle 11g,DBA Basics</h4> \n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Months [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 6,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t</div>\t\n           \n\t<!-- row4 col3-->\n\t\t<div class="col-md-4">\n\t\t\t<a href="linux-shell-scripting.php">\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color2 coursebox">\n                           <li class="list-group-item img14"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Linux and Shell Scripting</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 Month [40 Hrs] </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 5,000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\t\n\t\t\n\t\t\n\t\t\n\t\t<div class="col-md-4">\n\t\t\t\t\t\t  <a href="final-year-software-project-in-ranchi.php">\n\t\t\t\t\t      <div class="panel-body">\n\t\t\t\t\t       <ul class="list-group color6 coursebox">\n                           <li class="list-group-item img17"> </li>\n\t\t\t\t\t        <table class="table">\n\t\t\t\t\t        <div class="panel-heading"><h4>Final year Software Projects</h4> \n\t\t\t\t\t\t\t<p> </p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t           \n\t\t\t\t\t         <tr><td> Duration:1 -3 Months </td></tr>\n\t\t\t\t\t          <tr> <td><i class="fa fa-inr"></i> 4,000-10000 </td> </tr>\n\t\t\t\t\t        <tr> <td class="text-font">Read more:syllabus,delivery method & training outcome </td></tr>\n\t\t\t\t\t       </table>\n\t\t\t\t\t      </ul>\n\t\t\t\t\t </div>\n\t\t\t\t </a>\n\t\t\t</div>\n\n\n\n               \n\n\n\t\n\t\t</div>\n\t\t\n\t\t<!-- ../row-->\n\t\t\n\n\n                 \n\n              \n\t\t\n\t</div>\n\t\t\n\n\n               \n\n\n\n\n\n\n\n\n\t\n\t\t\n\n\t </div>\n\t\t\n\t\t\n\t\t\t\t\n\t\t\t<div class="col-md-3 affix">\n               \n\t\t\t\t<div class="panel panel-default query_form_bg">\n\t\t\t\t\t\n\t\t\t\t\t<div class=" panel-heading fa fa-phone 2px width-panel">\n\t\t\t\t\t<strong>  &nbsp;+91-81026-29294</strong>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="panel-heading"><a target="_blank" href="https://play.google.com/store/apps/details?id=in.co.whiznet.whiznet">\n                    <img src="playstore.png" class="responsive playstore" ></a></div>\n\t\t\t\t\t\n\t\t\t\t\t<div class="panel-heading" style="color:#10893f"><b>Enquiry Form </b></div>\n\t\t\t\t\t<div id ="success" class=" panel-body query_form_bg">\n\t\t\t\t\t<form class="form-horizontal" name="sentMessage" id="contactForm" role="form">\n\t\t\t\t\t\t<div class="form-group"> \n\t\t\t\t\t\t\t<div class="col-sm-12  ">\n\t\t\t\t\t\t\t\t<input type="text" class="form-control" id="name" placeholder="Your Name"/>\n                                                                <input type="hidden" id="course" value=\'\' > \n\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t</div>\n   \n   \n   \n   \n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<input type="number" class="form-control" id="phone" placeholder="Phone No"/>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<input type="email" class="form-control" id="email" placeholder="Email Address"/>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<textarea  cols="10" rows="2"type="number" class="form-control" id="message" placeholder="Your Query?"></textarea>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n  \n   \n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t\t<button type="submit" class="btn btn-primary width-b">Submit Query</button>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</form>\n\t\t\t\t\t</div>\n                </div>\n\t\t\t\t\n\t\t\t</div>\t\t\t\n            \n\t\t\t\n\t\t\t</div>\n\n\n\n\n\n\n\n\n <div class="row1" style="background:#C2D8B1;">\t\t\t\t\t\n\t  <div class="container ">\n\n        <div class="col-md-9 table-responsive ">\t  \n\t     <h3>New Batches</h3>\n\t     <table class="table table-striped hidden ">\n   \n\t\t\t\t\t\t<thead >\n\t\t\t\t\t\t<tr class="course_table_row">\n\t\t\t\t\t\t<th>Course</th>\n\t\t\t\t\t\t<th>Starts</th>\n\t\t\t\t\t\t<th>Ends</th>\n\t\t\t\t\t\t<th>Days</th>\n\t\t\t\t\t\t<th>Time</th>\n\t\t\t\t\t\t<th>Price</th>\n\t\t\t\t\t\t\n\t\t\t\t\t\t<th></th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</thead>\n   \n\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-java fa-3x"> </i>Advance Java</td>\n\t\t\t\t\t\t<td>4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>700AM-0930AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-php fa-3x"> </i><i class="icon-mysql fa-3x"> </i>PHP & MySQL</td>\n\t\t\t\t\t\t<td >4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>930AM-1130AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-android fa-3x"></i>Android</td>\n\t\t\t\t\t\t<td>4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>We,Thu,Fr,Sa</td>\n\t\t\t\t\t\t<td>1200AM-0200PM</td>\n\t\t\t\t\t\t<td>INR 11500</td>\n\t\t\t\t\t\t<td>INR 9775</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3 "><i class="icon-python fa-3x"> </i>Python</td>\n\t\t\t\t\t\t<td>4 May</td>\n\t\t\t\t\t\t<td>30 May</td>\n\t\t\t\t\t\t<td>Mo,Tue,Wed,Sat</td>\n\t\t\t\t\t\t<td>0230PM-0430PM</td>\n\t\t\t\t\t\t<td>INR 4500</td>\n\t\t\t\t\t\t<td>INR 3825</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n   \n\t\t\t\t\t\t<table  class="table table-striped hidden">\n\t\t\t\t\t\t<br/>\n\t\t\t\t\t\t\t\n\t<thead>\n\t\t\t\t\t\t<tr><strong class="hidden">15% EARLYBIRD OFF (EXPIRES ON 20th May) </strong></tr>\n\t\t\t\t\t\t<tr><strong > For New Batches Contact <span > <big>+91-81026-29294</big></span></strong></tr><br/> <br/>\n\t\t\t\t\t\t<tr><strong > Fill Up the Enquiry Form </strong></tr>\n\t\t\t\t\t\t</thead>\t\t\t\t\t\t\n\t\t\t\t\t\n\t<br/><br/><br/>\n\t     <table class="table table-striped hidden">\n   \n\t\t\t\t\t\t<thead>\n\t\t\t\t\t\t<tr class="course_table_row">\n\t\t\t\t\t\t<th>Course</th>\n\t\t\t\t\t\t<th>Starts</th>\n\t\t\t\t\t\t<th>Ends</th>\n\t\t\t\t\t\t<th>Days</th>\n\t\t\t\t\t\t<th>Time</th>\n\t\t\t\t\t\t<th>Price</th>\n\t\t\t\t\t\t<th>15% EarlyBird Off[Ends 20Apr 2015]</th>\n\t\t\t\t\t\t<th></th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</thead>\n   \n\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-java fa-3x"> </i>Advance Java</td>\n\t\t\t\t\t\t<td>1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>700AM-0930AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-php fa-3x"> </i><i class="icon-mysql fa-3x"> </i>PHP & MySQL</td>\n\t\t\t\t\t\t<td >1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n\t\t\t\t\t\t<td>930AM-1130AM</td>\n\t\t\t\t\t\t<td>INR 8500</td>\n\t\t\t\t\t\t<td>INR 7225</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-android fa-3x"></i>Android</td>\n\t\t\t\t\t\t<td>1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>We,Thu,Fr,Sa</td>\n\t\t\t\t\t\t<td>1200AM-0200PM</td>\n\t\t\t\t\t\t<td>INR 11500</td>\n\t\t\t\t\t\t<td>INR 9775</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t<tr class="bgdarkrow">\n\t\t\t\t\t\t<td class="col-sm-3 "><i class="icon-python fa-3x"> </i>Python</td>\n\t\t\t\t\t\t<td>1 June</td>\n\t\t\t\t\t\t<td>30 June</td>\n\t\t\t\t\t\t<td>Mo,Tue,Wed,Sat</td>\n\t\t\t\t\t\t<td>0230PM-0430PM</td>\n\t\t\t\t\t\t<td>INR 4500</td>\n\t\t\t\t\t\t<td>INR 3825</td>\n\t\t\t\t\t\t<td><input type=\'button\' class=\'btn-primary\' value=\'Enroll\'></td>\n\t\t\t\t\t\t</tr> \n\t\t\t\t\t\t\n\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t</table>\n\t     \n\t  </div>\n\t  </div>\n\t </div>\n\t \n\t \n\t  <div class="row4" style="background:#B4D2A0">\t\t\t\t\t\n\t  <div class="container">\t\t\t\t\n\t\t<div class="col-md-9">\t\t\t\n\t\t\t\t\t\t<p class="text-h-f">Course Features:</p>\t\n\t\t\t\t\t\n\t\t\t\t<div class="panel-group" id="accordion">\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\n\t\t\t\t\t\t\t\t\t  Instructor Led Live Class Room Training\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseOne" class="panel-collapse collapse in">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\t  All course modules are designed to provide in-depth knowledge of the subject.\n\t\t\t\t\t\t\t\t  Training program is for the given number of hours.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\n\t\t\t\t\t\t\t\t\t\tAssignments\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseTwo" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tFor each course there will be a number of assignments. Completed assignments has\n\t\t\t\t\t\t\t\tto be uploaded on the website within the stipulated time-frame.Assignments will be evaluated\n\t\t\t\t\t\t\t\tand the marks will be calculated for the final grade.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div> \n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\n\t\t\t\t\t\t\t\t\t\t  Tests\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseThree" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tAll program consists of number of tests which will be evaluated and marks will be\n\t\t\t\t\t\t\t\tadded for the calculation of final grade.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseFour">\n\t\t\t\t\t\t\t\t\t\t  Lifetime Access\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseFour" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tAll successful candidates will get life-time access to our learning management system.\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseSix">\n\t\t\t\t\t\t\t\t\t\t   Get Certified\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div id="collapseSix" class="panel-collapse collapse">\n\t\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\tUpon completion of all the modules,assignments,tests and final project you will be awarded with\n\t\t\t\t\t\t\t\tcertificate with the grade you achieved.\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t<!--coln-3 close right-->\n\t\t\t</div>\n        </div>\n\t\t\n\t\t\n\t\t\n\t<!-- Marketing Icons Section top row /-->\t\n\t</div>\n\n\n        \n\n\t    \n\n    <!-- Header Carousel -->\n    \n    <!-- Page Content -->\n\n\t\n\t<!-- page content ends here -->\n  \n    <!-- footer -->\n    <div class="footer">\n\t \n\t\t<div class="container">\n\t  \n\t\t\n\t\t\t\t<div class="col-lg-3">\n\t\t\t\t\t<div class="panel panel-body nobg">\n\t\t\t\t\t<Strong class="foot-h-font">Quick Links</strong><br/>\n\t\t\t\t\t<a href="courses.php"><i class="fa fa-angle-right"></i>&nbsp Courses<br/></a>\n\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp Blog <br/>\n\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp Clients<br/>\n\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp My Whiznet<br/>\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\t<div class="col-lg-3">\n\t\t\t\t\t<div class="panel panel-body nobg">\n\t\t\t\t\t<img src="image/logo2.png" class="img-rounded img-responsive">\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<div class="col-lg-3">\n\t\t\t\t\t<div class="panel panel-body nobg">\n\t\t\t\t\t<strong class="foot-h-font">Whiznet Technologies</strong><br/>\n\t\t\t\t<u>Development and Training</u><br/>\n    \t\t\t\tRS Tower<br/>\n\t\t\t\t\t 3rd Floor<br/>\n\t\t\t\t\t Circular Road<br/>\n\t\t\t\t\t Ranchi<br/>\n\t\t\t\t\t Jharkhand<br/>\n\t\t\t\t\t (India)<br/>\n                     \n                     \n        \t\t\t\n                     \n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\n\t\t\n\t </div>\n\t \n\t <div class="container">\n\t   <div><p>&copy;  2017 Whiznet Technologies, LLP</div>\n\t </div>\n</div>\n\n\n\n    <!--footer ends here -->\t\n  \n\t  \n\t  \n\t  \n\t  \n<!--container top close-->\t  \n    \n\t\n\t\n    <!-- /.container -->\n\n    <!-- jQuery -->\n    <script src="js/jquery.js"></script>\n\n    <!-- Bootstrap Core JavaScript -->\n    <script src="js/bootstrap.min.js"></script>\n\t <script src="js/jqBootstrapValidation.js"></script>\n    <script src="js/contact_me.js"></script>\n\n    <!-- Script to Activate the Carousel -->\n    <script>\n    $(\'.carousel\').carousel({\n        interval: 5000 //changes the speed\n    })\n    </script>\n\n\t\n\t\n\n\t\n\t\n\t\n\t<script type="text/javascript">\n   $(function () { $(\'#collapseFour\').collapse({\n      toggle: false\n   })});\n   $(function () { $(\'#collapseTwo\').collapse(\'show\')});\n   $(function () { $(\'#collapseThree\').collapse(\'toggle\')});\n   $(function () { $(\'#collapseOne\').collapse(\'hide\')});\n</script>  \n\n<script src = "js/whiznet.js"></script>\n\n<script>\n  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n  })(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');\n\n  ga(\'create\', \'UA-16497263-21\', \'auto\');\n  ga(\'send\', \'pageview\');\n\n</script>\n</body>\n\n</html>'
>>> url = urllib.request.urlopen("http://whiznet.co.in/\n")
>>> for x in url:
	print("\n")

	

















































Traceback (most recent call last):
  File "<pyshell#148>", line 2, in <module>
    print("\n")
KeyboardInterrupt
>>> for x in url:
	print("\n+x")

	

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+x

+xTraceback (most recent call last):
  File "<pyshell#150>", line 2, in <module>
    print("\n+x")
KeyboardInterrupt
>>> for x in url:
	print("\n"+x)

	
Traceback (most recent call last):
  File "<pyshell#153>", line 2, in <module>
    print("\n"+x)
TypeError: must be str, not bytes
>>> for x in url:
	print("\n"+str(x))

	

b'\t\t\t\t\t\t</tr> \n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t</tbody>\n'

b'\t\t\t\t\t\t</table>\n'

b'   \n'

b'\t\t\t\t\t\t<table  class="table table-striped hidden">\n'

b'\t\t\t\t\t\t<br/>\n'

b'\t\t\t\t\t\t\t\n'

b'\t<thead>\n'

b'\t\t\t\t\t\t<tr><strong class="hidden">15% EARLYBIRD OFF (EXPIRES ON 20th May) </strong></tr>\n'

b'\t\t\t\t\t\t<tr><strong > For New Batches Contact <span > <big>+91-81026-29294</big></span></strong></tr><br/> <br/>\n'

b'\t\t\t\t\t\t<tr><strong > Fill Up the Enquiry Form </strong></tr>\n'

b'\t\t\t\t\t\t</thead>\t\t\t\t\t\t\n'

b'\t\t\t\t\t\n'

b'\t<br/><br/><br/>\n'

b'\t     <table class="table table-striped hidden">\n'

b'   \n'

b'\t\t\t\t\t\t<thead>\n'

b'\t\t\t\t\t\t<tr class="course_table_row">\n'

b'\t\t\t\t\t\t<th>Course</th>\n'

b'\t\t\t\t\t\t<th>Starts</th>\n'

b'\t\t\t\t\t\t<th>Ends</th>\n'

b'\t\t\t\t\t\t<th>Days</th>\n'

b'\t\t\t\t\t\t<th>Time</th>\n'

b'\t\t\t\t\t\t<th>Price</th>\n'

b'\t\t\t\t\t\t<th>15% EarlyBird Off[Ends 20Apr 2015]</th>\n'

b'\t\t\t\t\t\t<th></th>\n'

b'\t\t\t\t\t\t</tr>\n'

b'\t\t\t\t\t\t</thead>\n'

b'   \n'

b'\t\t\t\t\t\t<tbody>\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t<tr>\n'

b'\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-java fa-3x"> </i>Advance Java</td>\n'

b'\t\t\t\t\t\t<td>1 June</td>\n'

b'\t\t\t\t\t\t<td>30 June</td>\n'

b'\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n'

b'\t\t\t\t\t\t<td>700AM-0930AM</td>\n'

b'\t\t\t\t\t\t<td>INR 8500</td>\n'

b'\t\t\t\t\t\t<td>INR 7225</td>\n'

b"\t\t\t\t\t\t<td><input type='button' class='btn-primary' value='Enroll'></td>\n"

b'\t\t\t\t\t\t</tr> \n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t<tr class="bgdarkrow">\n'

b'\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-php fa-3x"> </i><i class="icon-mysql fa-3x"> </i>PHP & MySQL</td>\n'

b'\t\t\t\t\t\t<td >1 June</td>\n'

b'\t\t\t\t\t\t<td>30 June</td>\n'

b'\t\t\t\t\t\t<td>Mo,Tu,Th,Fri</td>\n'

b'\t\t\t\t\t\t<td>930AM-1130AM</td>\n'

b'\t\t\t\t\t\t<td>INR 8500</td>\n'

b'\t\t\t\t\t\t<td>INR 7225</td>\n'

b"\t\t\t\t\t\t<td><input type='button' class='btn-primary' value='Enroll'></td>\n"

b'\t\t\t\t\t\t</tr> \n'

b'\t\t\t\t\t\t<tr>\n'

b'\t\t\t\t\t\t<td class="col-sm-3"><i class="icon-android fa-3x"></i>Android</td>\n'

b'\t\t\t\t\t\t<td>1 June</td>\n'

b'\t\t\t\t\t\t<td>30 June</td>\n'

b'\t\t\t\t\t\t<td>We,Thu,Fr,Sa</td>\n'

b'\t\t\t\t\t\t<td>1200AM-0200PM</td>\n'

b'\t\t\t\t\t\t<td>INR 11500</td>\n'

b'\t\t\t\t\t\t<td>INR 9775</td>\n'

b"\t\t\t\t\t\t<td><input type='button' class='btn-primary' value='Enroll'></td>\n"

b'\t\t\t\t\t\t</tr> \n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t<tr class="bgdarkrow">\n'

b'\t\t\t\t\t\t<td class="col-sm-3 "><i class="icon-python fa-3x"> </i>Python</td>\n'

b'\t\t\t\t\t\t<td>1 June</td>\n'

b'\t\t\t\t\t\t<td>30 June</td>\n'

b'\t\t\t\t\t\t<td>Mo,Tue,Wed,Sat</td>\n'

b'\t\t\t\t\t\t<td>0230PM-0430PM</td>\n'

b'\t\t\t\t\t\t<td>INR 4500</td>\n'

b'\t\t\t\t\t\t<td>INR 3825</td>\n'

b"\t\t\t\t\t\t<td><input type='button' class='btn-primary' value='Enroll'></td>\n"

b'\t\t\t\t\t\t</tr> \n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t</tbody>\n'

b'\t\t\t\t\t\t</table>\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t</table>\n'

b'\t     \n'

b'\t  </div>\n'

b'\t  </div>\n'

b'\t </div>\n'

b'\t \n'

b'\t \n'

b'\t  <div class="row4" style="background:#B4D2A0">\t\t\t\t\t\n'

b'\t  <div class="container">\t\t\t\t\n'

b'\t\t<div class="col-md-9">\t\t\t\n'

b'\t\t\t\t\t\t<p class="text-h-f">Course Features:</p>\t\n'

b'\t\t\t\t\t\n'

b'\t\t\t\t<div class="panel-group" id="accordion">\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t<div class="panel panel-default">\n'

b'\t\t\t\t\t\t\t<div class="panel-heading">\n'

b'\t\t\t\t\t\t\t\t<p>\n'

b'\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\n'

b'\t\t\t\t\t\t\t\t\t  Instructor Led Live Class Room Training\n'

b'\t\t\t\t\t\t\t\t\t</a>\n'

b'\t\t\t\t\t\t\t\t</p>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t<div id="collapseOne" class="panel-collapse collapse in">\n'

b'\t\t\t\t\t\t\t\t<div class="panel-body">\n'

b'\t\t\t\t\t\t\t\t  All course modules are designed to provide in-depth knowledge of the subject.\n'

b'\t\t\t\t\t\t\t\t  Training program is for the given number of hours.\n'

b'\t\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t<div class="panel panel-default">\n'

b'\t\t\t\t\t\t\t<div class="panel-heading">\n'

b'\t\t\t\t\t\t\t\t<p>\n'

b'\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\n'

b'\t\t\t\t\t\t\t\t\t\tAssignments\n'

b'\t\t\t\t\t\t\t\t\t</a>\n'

b'\t\t\t\t\t\t\t\t</p>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t<div id="collapseTwo" class="panel-collapse collapse">\n'

b'\t\t\t\t\t\t\t\t<div class="panel-body">\n'

b'\t\t\t\t\t\t\t\tFor each course there will be a number of assignments. Completed assignments has\n'

b'\t\t\t\t\t\t\t\tto be uploaded on the website within the stipulated time-frame.Assignments will be evaluated\n'

b'\t\t\t\t\t\t\t\tand the marks will be calculated for the final grade.\n'

b'\t\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t</div> \n'

b'\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t<div class="panel panel-default">\n'

b'\t\t\t\t\t\t\t<div class="panel-heading">\n'

b'\t\t\t\t\t\t\t\t<p>\n'

b'\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\n'

b'\t\t\t\t\t\t\t\t\t\t  Tests\n'

b'\t\t\t\t\t\t\t\t\t</a>\n'

b'\t\t\t\t\t\t\t\t</p>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t<div id="collapseThree" class="panel-collapse collapse">\n'

b'\t\t\t\t\t\t\t\t<div class="panel-body">\n'

b'\t\t\t\t\t\t\t\tAll program consists of number of tests which will be evaluated and marks will be\n'

b'\t\t\t\t\t\t\t\tadded for the calculation of final grade.\n'

b'\t\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t<div class="panel panel-default">\n'

b'\t\t\t\t\t\t\t<div class="panel-heading">\n'

b'\t\t\t\t\t\t\t\t<p>\n'

b'\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseFour">\n'

b'\t\t\t\t\t\t\t\t\t\t  Lifetime Access\n'

b'\t\t\t\t\t\t\t\t\t</a>\n'

b'\t\t\t\t\t\t\t\t</p>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t<div id="collapseFour" class="panel-collapse collapse">\n'

b'\t\t\t\t\t\t\t\t<div class="panel-body">\n'

b'\t\t\t\t\t\t\t\tAll successful candidates will get life-time access to our learning management system.\n'

b'\t\t\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t\n'

b'\t\t\t\t\t\t<div class="panel panel-default">\n'

b'\t\t\t\t\t\t\t<div class="panel-heading">\n'

b'\t\t\t\t\t\t\t\t<p>\n'

b'\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseSix">\n'

b'\t\t\t\t\t\t\t\t\t\t   Get Certified\n'

b'\t\t\t\t\t\t\t\t\t</a>\n'

b'\t\t\t\t\t\t\t\t</p>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t<div id="collapseSix" class="panel-collapse collapse">\n'

b'\t\t\t\t\t\t\t\t<div class="panel-body">\n'

b'\t\t\t\t\t\t\t\tUpon completion of all the modules,assignments,tests and final project you will be awarded with\n'

b'\t\t\t\t\t\t\t\tcertificate with the grade you achieved.\n'

b'\t\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\t</div>\n'

b'\t\t\t\t</div>\n'

b'\t\t\t\t\t\n'

b'\t\t\t\t\t\n'

b'\t\t\t\t\t\n'

b'\t\t\t\n'

b'\t\t\t\n'

b'\t\t\t<!--coln-3 close right-->\n'

b'\t\t\t</div>\n'

b'        </div>\n'

b'\t\t\n'

b'\t\t\n'

b'\t\t\n'

b'\t<!-- Marketing Icons Section top row /-->\t\n'

b'\t</div>\n'

b'\n'

b'\n'

b'        \n'

b'\n'

b'\t    \n'

b'\n'

b'    <!-- Header Carousel -->\n'

b'    \n'

b'    <!-- Page Content -->\n'

b'\n'

b'\t\n'

b'\t<!-- page content ends here -->\n'

b'  \n'

b'    <!-- footer -->\n'

b'    <div class="footer">\n'

b'\t \n'

b'\t\t<div class="container">\n'

b'\t  \n'

b'\t\t\n'

b'\t\t\t\t<div class="col-lg-3">\n'

b'\t\t\t\t\t<div class="panel panel-body nobg">\n'

b'\t\t\t\t\t<Strong class="foot-h-font">Quick Links</strong><br/>\n'

b'\t\t\t\t\t<a href="courses.php"><i class="fa fa-angle-right"></i>&nbsp Courses<br/></a>\n'

b'\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp Blog <br/>\n'

b'\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp Clients<br/>\n'

b'\t\t\t\t\t<i class="fa fa-angle-right"></i>&nbsp My Whiznet<br/>\n'

b'\t\t\t\t\t\n'

b'\t\t\t\t\t</div>\n'

b'\t\t\t\t\t\n'

b'\t\t\t\t</div>\n'

b'\t\t\t\n'

b'\t\t\t\n'

b'\t\t\t\n'

b'\t\t\t\n'

b'\t\t\t\t<div class="col-lg-3">\n'

b'\t\t\t\t\t<div class="panel panel-body nobg">\n'

b'\t\t\t\t\t<img src="image/logo2.png" class="img-rounded img-responsive">\n'

b'\t\t\t\t\t</div>\n'

b'\t\t\t\t</div>\n'

b'\t\t\t\t\n'

b'\t\t\t\t\n'

b'\t\t\t\t<div class="col-lg-3">\n'

b'\t\t\t\t\t<div class="panel panel-body nobg">\n'

b'\t\t\t\t\t<strong class="foot-h-font">Whiznet Technologies</strong><br/>\n'

b'\t\t\t\t<u>Development and Training</u><br/>\n'

b'    \t\t\t\tRS Tower<br/>\n'

b'\t\t\t\t\t 3rd Floor<br/>\n'

b'\t\t\t\t\t Circular Road<br/>\n'

b'\t\t\t\t\t Ranchi<br/>\n'

b'\t\t\t\t\t Jharkhand<br/>\n'

b'\t\t\t\t\t (India)<br/>\n'

b'                     \n'

b'                     \n'

b'        \t\t\t\n'

b'                     \n'

b'\t\t\t\t\t\n'

b'\t\t\t\t\t</div>\n'

b'\t\t\t\t</div>\n'

b'\t\t\n'

b'\t\t\n'

b'\t </div>\n'

b'\t \n'

b'\t <div class="container">\n'

b'\t   <div><p>&copy;  2017 Whiznet Technologies, LLP</div>\n'

b'\t </div>\n'

b'</div>\n'

b'\n'

b'\n'

b'\n'

b'    <!--footer ends here -->\t\n'

b'  \n'

b'\t  \n'

b'\t  \n'

b'\t  \n'

b'\t  \n'

b'<!--container top close-->\t  \n'

b'    \n'

b'\t\n'

b'\t\n'

b'    <!-- /.container -->\n'

b'\n'

b'    <!-- jQuery -->\n'

b'    <script src="js/jquery.js"></script>\n'

b'\n'

b'    <!-- Bootstrap Core JavaScript -->\n'

b'    <script src="js/bootstrap.min.js"></script>\n'

b'\t <script src="js/jqBootstrapValidation.js"></script>\n'

b'    <script src="js/contact_me.js"></script>\n'

b'\n'

b'    <!-- Script to Activate the Carousel -->\n'

b'    <script>\n'

b"    $('.carousel').carousel({\n"

b'        interval: 5000 //changes the speed\n'

b'    })\n'

b'    </script>\n'

b'\n'

b'\t\n'

b'\t\n'

b'\n'

b'\t\n'

b'\t\n'

b'\t\n'

b'\t<script type="text/javascript">\n'

b"   $(function () { $('#collapseFour').collapse({\n"

b'      toggle: false\n'

b'   })});\n'

b"   $(function () { $('#collapseTwo').collapse('show')});\n"

b"   $(function () { $('#collapseThree').collapse('toggle')});\n"

b"   $(function () { $('#collapseOne').collapse('hide')});\n"

b'</script>  \n'

b'\n'

b'<script src = "js/whiznet.js"></script>\n'

b'\n'

b'<script>\n'

b"  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n"

b'  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n'

b'  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n'

b"  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');\n"

b'\n'

b"  ga('create', 'UA-16497263-21', 'auto');\n"

b"  ga('send', 'pageview');\n"

b'\n'

b'</script>\n'

b'</body>\n'

b'\n'

b'</html>'
>>> from bs import BeautifulSoup
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    from bs import BeautifulSoup
ModuleNotFoundError: No module named 'bs'
>>> from bs4 import BeautifulSoup
>>> import urllib.request
>>> url = urllib.request.urlopen("https://www.che.iitb.ac.in/online/people/faculty/core-faculty")
>>> data = url.read()
>>> dada = str(data)
>>> data = str(data)
>>> soup = BeautifulSoup(data)

Warning (from warnings module):
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python36\lib\site-packages\bs4\__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "html.parser")

>>> datasoup = BeautifulSoup(data, 'html.parser')
>>> data = soup.findall('+d')
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    data = soup.findall('+d')
TypeError: 'NoneType' object is not callable
>>> data = soup.findAll('td')
>>> for d in data:
	print(d.string)

	
Jhumpa  Adhikari
Professor
Core Faculty
Chemical Engineering 
241
+91 (22) 2576 7245 (O)
Email Contact Form
Rajdip  Bandyopadhyaya
Professor
Core Faculty
Chemical Engineering 
145
None
Email Contact Form
Jayesh  Bellare
Professor
Core Faculty
Chemical Engineering 
131
+91 (22) 2576 7207  (O)
Email Contact Form
Sharad  Bhartiya
Professor
Core Faculty
Chemical Engineering 
311
None
Email Contact Form
Swati  Bhattacharya
Assistant Prof.
Core Faculty
Chemical Engineering 
122
7220
Email Contact Form
Mani  Bhushan
Professor
Core Faculty
Chemical Engineering 
311
None
Email Contact Form
Abhijit  Chatterjee
Associate Prof.
Core Faculty
CAD Center
2
+91 (22) 2576 7242 (O)
Email Contact Form
Ratul  Dasgupta
Assistant Prof.
Core Faculty
Chemical Engineering 
122
91-22-2576-7235
Email Contact Form
Madhukar  Omkarnath Garg
Professor
Core Faculty
NEW PG LAB  ANNEX
0
None
Email Contact Form
Partha Sarathi Goswami
Assistant Prof.
Core Faculty
Department of Chemical engineering
151
None
Email Contact Form
Ravindra D Gudi
Professor
Core Faculty
CAD Center
243
+91 (22) 2576 7231 (O)
Email Contact Form
Venkat  Gundabala
Assistant Prof.
Core Faculty
Chemical Engineering 
241
None
Email Contact Form
Sameer  Jadhav
Associate Prof.
Core Faculty
Chemical Engineering 
112
None
Email Contact Form
Sujit S Jogwar
Assistant Prof.
Core Faculty
CAD center
100
+91 (22) 2576 7244
Email Contact Form
Devang V Khakhar
Professor
Core Faculty
Chemical Engineering 
151
+91 (22) 2576 7212 (O)
Email Contact Form
Sanjay M Mahajani
Professor
Core Faculty
Chemical Engineering
125
None
Email Contact Form
Abhijit  Majumder
Assistant Prof.
Core Faculty
Chemical Engineering 
136
+91-(22)-2576 7237
Email Contact Form
Ateeque  Malani
Assistant Prof.
Core Faculty
Chemical Engineering 
138
None
Email Contact Form
Anurag  Mehra
Professor
Core Faculty
Chemical Engineering 
222
None
Email Contact Form
Sarika  Mehra
Associate Prof.
Core Faculty
Chemical Engineering 
112
None
Email Contact Form
Arun S Moharir
Professor
Core Faculty
CAD Center
0
+91 (22) 2576 7795(O)
Email Contact Form
Kannan M Moudgalya
Professor
Core Faculty
Chemical Engineering 
311
None
Email Contact Form
Hemant  Nanavati
Professor
Core Faculty
Chemical Engineering 
242
None
Email Contact Form
Santosh  Noronha
Assistant Prof.
Core Faculty
Chemical Engineering 
123
None
Email Contact Form
Sachin C Patwardhan
Professor
Core Faculty
CAD Centre
305
None
Email Contact Form
Sandip  Roy
Associate Prof.
Core Faculty
CAD Center
131
None
Email Contact Form
Supreet  Saini
Associate Prof.
Core Faculty
PG Lab Annex.
0
+91 22 2576 7216 (O)
Email Contact Form
Arindam  Sarkar
Assistant Prof.
Core Faculty
Chemical Engineering 
125
None
Email Contact Form
Jyoti  Seth
Assistant Prof.
Core Faculty
Chemical Engineering Department
236
None
Email Contact Form
Yogendra  Shastri
Assistant Prof.
Core Faculty
Chemical Engineering 
311
+91 (22) 2576 7203 (O)
Email Contact Form
P  Sunthar
Associate Prof.
Core Faculty
Chemical Engineering 
222
None
Email Contact Form
Akkihebbal K Suresh
Professor
Core Faculty
Chemical Engineering 
220
None
Email Contact Form
Rochish Madhukar  Thaokar
Professor
Core Faculty
Chemical Engineering 
123
None
Email Contact Form
Mahesh S Tirumkudulu
Professor
Core Faculty
Chemical Engineering 
151
None
Email Contact Form
Mukta  Tripathy
Assistant Prof.
Core Faculty
Department of Chemical engineering
222
+91 (22) 2576 7204 (O)
Email Contact Form
Chandra  Venkataraman
Professor
Core Faculty
Chemical Engineering 
321
None
Email Contact Form
K. V Venkatesh
Professor
Core Faculty
Chemical Engineering 
136
None
Email Contact Form
Madhu  Vinjamur
Professor
Core Faculty
Chemical Engineering 
302
None
Email Contact Form
Ganesh A Viswanathan
Associate Prof.
Core Faculty
Chemical Engineering 
125
None
Email Contact Form
Pramod P Wangikar
Professor
Core Faculty
Chemical Engineering 
136
+91 (22) 2576 7232 (o)
Email Contact Form
>>> 
