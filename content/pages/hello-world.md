Title: Hello, world!
Date: 2016-09-18
Tags: updates
Category: Computing

It's been on my list of "haunting tasks" (this is a real list I keep) to "make a Jekyll blog on Github pages". However, my experience with Jekyll was: jargon jargon jargon, gem install. Since I try not to type mysterious things into my terminal, I googled around, and eventually found a page titled ["What is a gem?"](http://guides.rubygems.org/what-is-a-gem/) that doesn't actually answer the question. Eventually this path led to many complaints about Ruby dependency nightmares with Jekyll, a blog comment about "other static site generators", and my using [Pelican](http://docs.getpelican.com/).

Here are some things I learned while throwing this together today:

1. I am an example-oriented learner, so I briefly browsed the docs and then started with the [quickstart](http://docs.getpelican.com/en/3.6.3/quickstart.html) option. It builds you a barebones page that is then as flexible as if built by hand. Viewing config & styling documents is straightforward and you can get on your way fast.

2. If you are using Github pages, the helpful info is in [tips](http://docs.getpelican.com/en/3.6.3/tips.html)

3. I have a static Github page at my .io URL, and I spend a lot of time trying to figure out how I could put a blog at mfoos.github.io/blog/ without having a confusing directory structure and/or files everywhere. I ultimately figured it out using [this Hugo tutorial](https://gohugo.io/tutorials/github-pages-blog/).
Basically:

    * Create a totally separate repo called "blog" (or whatever)

    * Create a branch called "gh-pages" (this exactly)

    * WHILE ON THE MASTER BRANCH use [ghp-import](https://github.com/davisp/ghp-import) to automatically rename the contents of your `output` so that ONCE DEPLOYED they all live in the /blog folder `git push origin gh-pages`


4. I also noticed that the themes appear slightly different in the local browser preview vs hosted on Github, so make sure you like the hosted version too.

Now I have a blog. Better write about something.

