Making A Github Blog Without Any Static-File Generator
======================================================
_Posted: 28 December 2016_

So, as I said earlier, here I will try to give a simple tutorial on how to blog on GitHub Pages without any third party Static-Website Generator such as Jekyll, Hexo, or such. Instead, we will use existing javascript library (which already hosted outside so we can just call it without any extra effort). So, here we go:

### 0. Overview
To blog on Github, of course we first need to have a Github Page repository.

The technologies we used here:
- JQuery
- Markdown
- Bootstrap for styling
- ShowdownJS : A JS library for parsing markdown

Folder structures:
```
- index.html
- posts/
	- first-post.md
	- second-post.md
	- third-post.md
```

### 1. Preparing the index.html

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Dotmonger blog</title>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <style>
		body {
		  padding-top: 50px;
		}
		.starter-template {
		  padding: 40px 15px;
		  text-align: left;
		}
    </style>
  </head>
  <body>

    <div class="container">

      <div class="starter-template" id="main_content"></div>

    </div><!-- /.container -->
    

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <!-- Showdownjs Markdown converter -->
    <script src="https://rawgit.com/showdownjs/showdown/develop/dist/showdown.min.js"></script>
  </body>
</html>
```

### 2. The scripting

Put it before the end of body:
```
<script type="text/javascript">
</script>
```

Define the post list:
```
var posts = [
  'posts/first-post',
  'posts/second-post',
  'posts/third-post',
];
```

Initialization:
```
var main_content = $('#main_content');
var converter = new showdown.Converter();
var main_url = 'https://dotmonger.github.io/';  
```

Create a function to display posts:
```
function display_all(posts, content, converter) {
  $.each(posts, function (key, val) {
    $.get(main_url + val + '.md', function(data) {
      content.append(converter.makeHtml(data));
    });
  })
}
```

Main call:
```
$().ready(function() {
  display_all(posts, main_content, converter);
});
```

Thats all.
```
git add .
git commit -a "First post"
git push origin master
```