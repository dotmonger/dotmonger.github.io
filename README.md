## Welcome My Page

Hi, I'm Dotmonger, a crazy freelance web developer from Bandung, Indonesia. I mostly worked with back-end development such as PHP, CMS, MySQL, etc. But other than my work, I'm highly interested with beautiful minimalist game (specially, [A Dark Room](http://adarkroom.doublespeakgames.com) ), along with discussion about Artifical Intelligence. I'm also a huge fan of reading mangas and novels.

Thanks for visiting!

## Contacts
- [My reddit account](https://www.reddit.com/user/dotmonger/)

Blog
==================================================

Incremental Game
-----------------------------------------------------------------------------------------
_Posted: 28 December 2016_

As I wrote on my intro, I really like minimalistic yet beautiful game. And my current favorite is [A Dark Room](http://adarkroom.doublespeakgames.com). I can't stressed enaugh how much its inspire me. Its simple yet mysterious, highly accessible due its web based nature, "What the" kind of a story, beautiful folding revelation.

In fact, few days ago I just discovered that there were some other games that fall into the same category as A Dark Room (which I pretty much suspected were inspired by it). It happened that people mostly called this kind of games as "Incremental Game", due its nature of revealing its gameplay part after part. If you like these kind of game, I suggest to try some the ones listed here : www.reddit.com/r/incremental_games/wiki/list_of_incremental_games . But for your reference, I'll listed some that happen to cam to my liking:

- [Candy Box](http://candies.aniwey.net/) : The original inspiration to 'A Dark Room'. Downright crazy yet funny.
- [Speed Warp](http://speed-warp.net) : Some of the few that really fall into the same category as 'A Dark Room' & 'Candy Box'. Entirely text-based (note the usage of ASCII art), truly unfolding interfaces as the game progress, completely mysterious gameplay. A must try
- [True Exponential](http://angarg12.github.io/TrueExponential/) : To be honest, I haven't really understand much about what this game about, and I haven't explored it far enough. But the idea of using Mathematical Research theme along with it LaTeX styled design, its really interesting.
- [Drowning In Problems](http://game.notch.net/drowning/) : Interesting example about using Incremental Game mechanics on themes regarding everyday life. I think this is some the few incremental game that really try to convey story in repetitous, monotonous, grind-all-the-way style of Incremental Game, rather than giving some mystery with no actual meaning on it.

Yeah, its really few, but I think this is enough for now. I'll try to review some more when I have tried some more games on the list I've given above. Anyway, enjoy the games.

Too hard to not being tampted
-----------------------------------------------------------------------------------------
_Posted: 16 December 2016_

Neural Network! Genetic Algorithm! State Driven Game Agent!

wanjir, pusing tapi kayak terkena bujuk rayu iblis gitu gue.

beberapa hari terakhir ini gue lagi kepincut banget sama http://www.ai-junkie.com/ . Ini situs bagus banget, it teaches about many topics on A.I. with as many practice as possible. Less math, more coding. Recommended banget buat kalian-kalian yang penasaran sama A.I., tapi gak punya basic di matematika atau informatika (gue sendiri anak matematika tapi bingung dengan bacaan-bacaan tentang A.I.).

Gue sejauh ini baru berhasil implementasi koding terkait Genetic Algorithm. Jadi kode example yang dikasih di web itu pakai C++ (iya bener, C++! gimana gue gak teler..). Biar sekalian gue latihan, gue coba translate itu bahasa ke javascript, dan pas jalan... those triumphant moments every coders always seek...

Anyway, gue belum jalan lebih jauh. Bahas genetik algoritmm sejauh ini cukup sederhana menurut gue. Pokoknya step2nya:
	- tentuin kondisi ideal yg mau dicapai
	- tentuin fungsi fitness yang sesuai
	- inisialisasi genom acak sesuai selera
	- loop sampai ketemu. di tiap loop (kita anggap sebagai 1 "generasi"):
		- beberapa kali:
			- ambil 2 pasangan dengan nilai fitness yang lumayan tinggi
			- crossover
			- mutasi
		- kemudian ganti semua populasi lama dengan populasi baru
	- done
Yaa, ini ringkasan super singkat aja sih. Bacaan lebih lanjut langsung aja ke: http://www.ai-junkie.com/ga/intro/gat1.html

Gue sekarang mau lanjut ke bahasan Neural Network, tapi bahasan ini lumayan masif ngodingnya. Ahaha. Emang bukan topik bahasan gampang sih. Selain itu juga ada topik bahasan State-Driven Agent yang berguna banget buat yang mau bikin A.I. buat game. Totally interesting...

But I think I couldn't handle anymore of this for now. Mungkin gue perlu nyoba ngoprek game yang agak lebih simpel. Just wait and see...
