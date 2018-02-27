Title: Getting Started with R...maybe
Date: 2018-02-24
Tags: R, learning
Category: Computing

I am probably the wrong person to write this, but I sent more than one email on the topic, so I have to write a blog post. THEM'S THE RULES.

A few days ago I got an email saying "I'm new to R, and I just don't know where to start learning it, can you help?" (This may seem odd given that I run an R user group, but the sender is not local to the group, she found me because I'm in her state). You might say that there are lots of resources on the web (true), but when you are suffering from "don't know where to start", you... don't know where to start! If you are unfamiliar with this experience, you should see me trying to order takeout when I'm reeeeeeally tired.

Anyway, the reason I feel unfit to write this is that I learned R in an obscenely expensive graduate statistics class. In that class, I learned basic data structures and how to copy code verbatim. To be honest, it took me a long time to stop getting that error you get when you forget the comma when subsetting rows AND columns. Then I landed at an internship that was all R all the time. Which brings me to my advice.

1. **Identify a problem and solve it**  

   This is both the best programming-learning advice I've ever gotten, and some of the most frustrating. It's hard to pick something out of thin air, especially if you're so new that you can't tell what's an appropriate problem. Or if you're anxious to LEARN THE IMPORTANT THINGS OMG (I'm here with Python, btw). So I guess I recommend you think about what prompted you to seek out R (cool plots? want to run the same analysis many times with different data?), and draw from that. I also recommend that you not dismiss candidate ideas because they seem too easy. I learned my first programming language writing a script that read a formatted file and did third-grade arithmetic. It was gruesome and you can see it [here](https://github.com/mfoos/NPLab_Projects/blob/master/winner_finder-3x4x1.plx). When you choose a problem to solve, you are keeping your eyes on the prize, so you can focus on learning things that solve your problem/subproblems, and your path is sort of linear toward a goal. It's sort of like how people who are saving money for a concrete goal are often better able to do so than those who are saving for savings' sake. Eventually, you'll probably start to think about adding features or changing how something works, and you can branch out then.

2. **Read other peoples' code**

   I think every time I read someone else's R code, I learn about a new function that I hadn't known I didn't know. It will also teach you about the value of liberal whitespace usage. The ideal way to read other peoples' code is to see something cool a coworker has done, and say "cool, how did you do that?" because then it's likely to be a smallish example, about something interesting to you, and hopefully an opportunity for some coaching. If that's not in the cards, you're still sitting pretty, because the recent uptick in popularity of R has been paralleled by interest in reproducible research, so many many many many R resources will contain a link to the code used to generate them.

3. **Attend a Data Carpentry workshop or read their materials**

   [Data Carpentry](http://www.datacarpentry.org/) is a non-profit with the mission of teaching computational data skills to researchers, with a strong focus on becoming productive as fast as possible. Workshops happen all over the world, and you can either find one to attend on their website, or encourage your organization to host one. (Usually places host them to educate THEIR people, but sometimes they are open enrollment.) If you can't swing one of those options, all the teaching materials are online, and you can work on them independently. The general R lesson is [here](http://www.datacarpentry.org/R-ecology-lesson/). Data Carpentry has a sister organization called [Software Carpentry](https://software-carpentry.org/) that skews more toward software than data, and beyond that, I simply prefer the DC lessons.

4. **R User Groups**

   This won't help everyone, but if you live near a city or large university, there may be an R User Group or [R-Ladies](rladies.org) chapter near you. If you are a gender minority (female, non-binary, etc.) you can even check out [R-Ladies Remote](https://www.r-bloggers.com/introducing-r-ladies-remote-chapter/), which is in the powering-up stage as I write this. User groups usually offer tutorials and seminars, and are an opportunity to meet potential mentors, mentees or collaborators. Plus, it is among the best ways to keep up-to-date with R happenings.

**Thus ends the personal endorsement section**

Below are some additional resources that get positive reviews from the folks around me

1. **DataCamp**
   [DataCamp](https://www.datacamp.com/) offers a ton of courses in R and Python, including many taught by "R celebrities" like Julia Silge and Charlotte Wickham (and several R-Ladies founders). Full disclosure, DataCamp sponsored an R-Ladies Boston. I've never used DataCamp, but my R-Ladies members rave about it. As I understand it, some courses are free, and some are subscriber-only, with the first chapter free to view. Pay plans are $25-29 per month.

2. **R4DS**

   [R4DS](http://r4ds.had.co.nz/) or "R for Data Science" is a free ebook (or non-free paperback) by Hadley Wickham and Garrett Grolemund, who both work at RStudio and are actually also DataCamp instructors. They thus contribute a lot to shaping the language and have their fingers on the pulse of R. I have landed in this ebook while troubleshooting, but never tried to go through it systematically (some R-Ladies chapters are doing this, I believe)

3. **MOOCs in general**

   Udemy, Coursera, Udacity and edX all have R courses. I started the JHU Data Science Specialization on Coursera and I wouldn't recommend it for absolute beginners to R. But other than that, I have no experience with R MOOCs.

4. **RStudio's Resource list**

   I only found [this](https://www.rstudio.com/online-learning/#r-programming) researching this blog post. I haven't clicked past the list, but folks at RStudio KNOW R and have a significant interest in getting more people using it. They also make the RStudio IDE and the RMarkdown and Shiny packages, so they are go-tos for those R-adjacent topics.

#### Alright, kiddos, go learn some R! Go help someone learn R!
