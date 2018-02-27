Title: Ughhhh, Computer Shopping
Date: 2017-09-17
Tags: hardware, chromebook
Category: Computing

I was a lifelong Windows user until 2010 when I was impressed by Ubuntu on my [Dell Mini 9](http://www.dell.com/us/dfh/p/inspiron-mini9/pd). Remember netbooks? They were like crappy, expensive, bulky Chromebooks, but they were ahead of their time introducing mainstream users to Ubuntu. When the laptop I bought when I left for college died in 2011 after several months of being pink, I bought another PC that turned out to be a spectacular piece of crap. It [BSoD](https://en.wikipedia.org/wiki/Blue_Screen_of_Death)’d several times a day, and was eventually helped to limp along by replacing Windows with CrunchBang Linux. The Linux came in pretty handy for my bioinformatics night school classes, but the computer continued to be difficult. After putting up with my whining for a year or so, my ex sold me his old MacBook Pro for the tidy sum of me throwing my existing computer down a flight of concrete stairs behind our apartment building.

I really liked the terminal access, the “just working”, and the wankless access to Microsoft Office, and my bioinformatics professor got a very satisfying “I Told You So” out of it. I am still using that MBP, but the model is no longer supported, and I’m starting to notice performance issues. I’ve been casually window-shopping for a new machine, and it’s got me thinking about what’s out there, option-wise.

This is a good time to plug [Olga Botvinnik's recent MacBook setup post](https://olgabotvinnik.com/blog/macbook-setup/)

I know Chromebooks started out as an inexpensive option for web browsing and word processing, but have come up in the world. For those who don’t know, Chromebooks run Chrome OS rather than Windows or OSX. Apps are available from Google and through the Chrome webstore, but [there’s apparently also an android integration in the works, that’s in stable release for some hardware.](https://sites.google.com/a/chromium.org/dev/chromium-os/chrome-os-systems-supporting-android-apps) Chrome OS is built on top of Linux, but the Linux isn’t intended to be “exposed” to the user, for lack of a better word.

I’ve had a Samsung 3 (XE500C13-K02US) [Chromebook](https://www.google.com/chromebook/device/samsung-chromebook-3/) for about a year, which I bought after reading about [crouton](https://github.com/dnschneid/crouton), which is a sort of live-switching dual-boot between Chrome OS and the Linux environment of your choice (I assume there are limitations, but I set up Ubuntu 14.04 (Trusty Tahr) with Unity and never looked back). I think I used a mishmash of tutorials, because none/all look right when I check now. I also definitely read somewhere that you could only use crouton with a Chromebook with an Intel processor, but have not been able to find the reference. I don’t know whether it is true, or was ever true. In any case, that factored into my decision to buy the Samsung 3, which I’m very happy with.

So that’s what this rambling post was supposed to be about: Options for Chromebook users who use the shell as much as most people use MS Word or Excel. When I buy a computer to “get work done on the run”, that includes parsing text with GNU utilities, Python and R scripting, and communicating with Github for version control and static web publishing, among other things.

Here’s my list of demands:  
- Terminal that works like a linux terminal, including git, ssh, apt-get/yum, curl and GNU text utilities
- [Jupyter notebooks](http://jupyter.org/) and/or [ipython](https://ipython.org/)
- [RStudio](https://www.rstudio.com/products/RStudio/) (tfw you’re a Shiny developer)

As far as I can tell, there are three options, which are not all mutually exclusive.

[Crouton](https://github.com/dnschneid/crouton) -  Lets you run side-by-side sessions in Chrome OS and a Linux desktop, with instant screen swapping.  
**Pros:** You can do whatever you want with the Linux desktop once you’ve set it up.  
**Cons:** Fussy to set up, overrides security, results in an opaque warning that could get you in trouble at an airport (it starts beeping if you don’t hit ctrl + D) or get your chroots (basically your configuration) erased by a well meaning friend who needed to check their email (the screen prompts you to “re-enable” the secure mode)

[Google Play / Termux](https://blog.lessonslearned.org/building-a-more-secure-development-chromebook/) - aka the [Kenn White](https://twitter.com/kennwhite) method, using an Android app [(Termux)](https://termux.com/) that’s a terminal emulator/Linux environment (requires that your Chromebook supports Google Play)  
**Pros:** Runs without root, doesn’t compromise Chrome OS integrity/security  
**Cons:** No GUI for RStudio, unclear how hard it’s going to be to install non-standard languages like R, looks sort of fussy to set up (but I haven’t actually tried it yet, and my threshold for fussy has a lot to do with “doesn’t work as promised”), not available to all Chromebook users.

Rely on remotes - Set up a server elsewhere (like an Amazon EC2 instance) with the software you want to use, and ssh into it from either the native crosh shell, or a supported ssh client from the Chrome app store  
**Pros:** Real Linux (Install anything! No surprises!), RStudio Server and Jupyter mean GUIs are available via the browser, same environment available to multiple devices  
**Cons:** Requires internet connection and additional infrastructure investment

I’m currently doing #1 and considering switching to a combo of #2 & #3 - I really use RStudio a lot! A couple of people have already written about doing this:  
- [http://code.markedmondson.me/rstudio-server-chromebook/](http://code.markedmondson.me/rstudio-server-chromebook/)
- [https://jrfarrer.github.io/r/2016/12/29/RStudio-Lightsail.html](https://jrfarrer.github.io/r/2016/12/29/RStudio-Lightsail.html)

I must say, though, that in the process of writing this post, I’ve had a realization about what sort of specs I need on my next “main” computer. I don’t game and I don’t edit images, and the heavier-lifting data stuff I do needs to get off-loaded to a cluster anyway. So I suppose my one, big, remaining question is:  Why do other developers have high-powered MBPs? Not in a “you’re wrong” way - In a “what am I missing?” way.

I don’t have comments set up on the blog, but I am quite curious to hear feedback on this! Tweet me at [@mariannafoos](https://twitter.com/MariannaFoos), or well...figure out my gmail address :)
