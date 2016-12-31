Making Progress-Button Inspired by "A Dark Room"
===============================================
_Posted: 31 December 2016_

Happy New Year! I know this blog is really short, but I think its proper worth to congratulate all of us for arriving at the end of the year.

So today I'll try to explain to you how to make a button with a progress bar animation as we could find on "A Dark Room".

In my oppinion, the button used in "A Dark Room" is a really good example of a nice User Interface design on a game. Its simple, intuitive, the player would immediately understand what it does just by interacting with it once. And for the use of unfolding, this kind of button is really useful, hence I make this post to try to explain it to you guys.

To make a progress button (thats how we'll call them here from now), one of the easiest method is to tranform the basic _button_ element in HTML into progress bar with some CSS helping. Most of the css here is adapted from this article: https://css-tricks.com/css3-progress-bars/ . The idea is the button should be a container of a _span_ element that will represent the growing bar of a progress bar.

So first, lets lay down some HTML:

```
<button id="button1" class="progressButton">click</button>
```

along with some basic CSS
```
.progressButton {
	height: 20px;  /* Can be anything */
  width: 100px;
  position: relative;
  background: #FFF;
  padding: 3px;
}
```

Okay, after we lay down the basic, we will strat making the growing bar inside the button. To make it, here we will make a javascript function to insert all button with progressButton class with a span class, (in case you're wondering, here I use the min.js script by remy https://github.com/remy/min.js for the DOM selector function. Of course you could use any other JS library you like, or just use vanilla javascript if you fancy).

```
var initProgressButton = function() {
  $('.progressButton').forEach(function(button) {
    button.innerHTML += '<span></span>';
  });
}
initProgressButton();
```

and some css styling
```
.progressButton span {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  height: 100%;
  background-color: rgb(43,194,83);
  overflow: hidden;
}
```

That should took care of the styilng. Now is the trickiest part, the actual loading animation. The idea here is that wi will register a button click event handler that whenever the button is clicked, it will trigger a JS setInterval, which will regularly change the span element as we desired. So to do it, first lets make a little modification to our initProgressButton function. First, we will need to add some parameters to our button to hold the desires loading duration:

```
var initProgressButton = function() {
  $('.progressButton').forEach(function(button) {
    button.innerHTML += '<span></span>';
    var bar = button.firstElementChild; // the span element

    button.step = 25;
    button.duration = 2000;
...
```

And now the handler for click event. First, some styling edit
```
...
	button.on('click', function() {
		button.disabled = true;
		bar.style.display = 'block';
..
```

Then the animation
```
...
		var progress = 0;
		var interval = setInterval(function() {
		progress += button.step;
		if (progress >= button.duration) {
		  clearInterval(interval);
		  button.disabled = false;
		  bar.style.display = 'none';
		} else {
		  // button.innerText = txt + ' (' + Math.round((button.duration-progress)/1000) + 's)'
		  bar.style.width = Math.round(progress*100/button.duration) + '%';
		}
		}, button.step);
...
```

Here's the complete code:
```
<html>
<head>
	<title></title>
	<script type="text/javascript" src="https://cdn.rawgit.com/remy/min.js/master/dist/%24.min.js"></script>
</head>
<body>
  <button id="button1" class="progressButton">click</button>
  <br><br><br>
  <button id="button2" class="progressButton">click</button>

</body>
<style type="text/css">

.progressButton {
  height: 20px;  /* Can be anything */
  width: 100px;
  position: relative;
  background: #FFF;
  padding: 3px;
}

.progressButton span {
  position: absolute;
  top: 0;
  left: 0;
  display: none;
  height: 100%;
  width: 100%;
  background-color: rgb(43,194,83);
  overflow: hidden;
}

</style>
<script type="text/javascript">
var initProgressButton = function() {
  $('.progressButton').forEach(function(button) {
    button.innerHTML += '<span></span>';
    var bar = button.firstElementChild; // the span element

    button.step = 25;
    button.duration = 2000;

    button.on('click', function() {
      button.disabled = true;
      bar.style.display = 'block';

      var progress = 0;
      var interval = setInterval(function() {
        progress += button.step;
        if (progress >= button.duration) {
          clearInterval(interval);
          button.disabled = false;
          bar.style.display = 'none';
        } else {
          // button.innerText = txt + ' (' + Math.round((button.duration-progress)/1000) + 's)'
          bar.style.width = Math.round(progress*100/button.duration) + '%';
        }
      }, button.step);
    })
  });
}
initProgressButton();
</script>
</html>
```