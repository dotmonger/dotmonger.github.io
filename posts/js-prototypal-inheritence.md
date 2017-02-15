Experiment with Javascript prototypal inheritence
=================================================

So, a while back I stumbled upon a great article by [Addit about Prototypal Inheritence in Javascript](http://aaditmshah.github.io/why-prototypal-inheritance-matters/). So as everyone who've done programming in Javascript already aware of, doing OOP in javascript is HARD. Well, I dont have many experinces in NodeJS but defining contructor and trying to extend a class in Chrome's Javascript Console is such a pain in the ass. To done such things, you must dealt with prototype properly, carefully referencing parents, and dont mention how awfully messy the overall syntax is.

Yeah, it sucks.

And the worst thing is, I dont know why Javascript has such hideous syntax when its regarded as an Object Oriented language.

Until I've read Aadit's articel, which felt like my mind suddenly being flushed clean from all the darkness. The answer for my confusions is actually pretty plain and painfully simple: its because javascript doesnt use the same paradigm of OOP as many other OOP language. Or at least its what its originally supposed to be.

According to that article, it turns out that JavaScript actually employ a unique type of OOP Inheritence called _Prototypal Inheritence_, and just this explain numerous thing. In Javascript, every object is actually an instance of other **object**, not class. That is why many people utiize dictionary to define class, not because its mandatory, but its just the data type with the most similarities to what class is in other languages (technically, you could also use array).

So the article actually cover a lot of things, and the author himself has gained more view regarding his favour for prototypal over regular inheritence (you could read the comment section on the articel). But me myself (for now at least), felt that protypal inheritence is the best way to actually do OOP as that is actually how the JavaScript is designed. The classical inheritence (which JavaScript adopt mostly only as a marketing strategy) in many cases only bring confusion rather than improvement over the former style.

# So, how do we do Prototypal Inheritence?

So to cut the chase, use the following code as a base library:

```
function newtype(prototype) {
    var instance = prototype.instance = function () {};
    instance.prototype = prototype;
    return prototype;
}

var object = newtype({
    create: function () {
        var instance = new this.instance;
        this.init.apply(instance, arguments);
        return instance;
    },
    extend: function (keys) {
        var parent = keys.parent = this;
        var prototype = new parent.instance;
        for (var key in keys) prototype[key] = keys[key];
        return newtype(prototype);
    }
});
```

Now everytime you need to create a new class, just extend object and call create. Example:

```
var bird = object.extend({
    init: function (type, flightless) {
        this.type = type;
        this.flightless = flightless;
    },
    describe: function () {
        if (this.flightless)
            alert(this.type + " can't fly.");
        else alert(this.type + " can fly.");
    }
});

var penguin = bird.extend({
    init: function (name) {
        this.parent.init.call(this, "Penguins", true);
        this.name = name;
    },
    describe: function () {
        alert(this.name + " is a Penguin.");
        this.parent.describe.call(this);
        alert("However they can swim.");
    }
});

var tux = penguin.create("Tux");
tux.describe();
```

For me, the above syntax is way cleaner then the styles teached in many beginner JavaScript tutorials (thats why its called 'beginer'). I think I'll be using this style more in the future.