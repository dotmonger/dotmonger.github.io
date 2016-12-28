Too hard to not being tempted
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
