Title: Event Report - DataRescue Boston @MIT
Date: 2017-02-23
Tags: hackathons
Category: Computing

Once upon a time an awesome lady I met on the internet, who blogs about challenging her own comfort zone, asked me if I might ever want to guest post. From what I can tell, she started a company, redirected her efforts there, and is sort of MIA on the internet now. I hope it's her dream come true. Anyway, I had a hard time coming up with a challenge for my own comfort zone, but had finally settled on "attend a hackathon".

This past Saturday, I attended a hackathon hosted by [DataRescue Boston](https://datarescue-boston.github.io/) at MIT. DataRescue is a movement of volunteers working to archive taxpayer-funded scientific data in the event that an antagonistic administration were to limit access to it.

I arrived at MIT half an hour late, because I screwed up, and was relieved to discover that it was still trickle-in time. There was a ton of coffee, bagels/toppings, OJ, fruit salad and awesome vegetarian breakfast burritos from Feed the People. I checked in, got a nametag, sticker and level keychain (!!!!) and was offered the option of opting out of photography at the event. 

I went and washed the MBTA slime off my hands, and sat down at a round table just as the program began. The organizers introduced themselves and the volunteer guides/managers, the purpose and motivation for Data Rescue, the facility information, the schedule and an outline of the roles folks could choose for the event. Two things that I really liked were the inclusion of facility information (bathroom and info table locations, etc.) and the pre-existing "Attendee Info Packet" they'd set up online with info in greater detail.

People chose their own "track" from:

* Surveyors: Researching government departments not already being archived (not touching data)

* Seeders: Use the information supplied by the surveyors to identify and queue data that needs to be archived

* Harvesters: Download data, document download process, and upload to the archive

* Storytellers: Document the event for communication to the public and the press.

The roles/tracks was something I had researched ahead of time, but didn't quite understand, so I want to dwell on them for a moment. First of all, I'm a "technical" person aka I code, but given the importance of the mission, I went with the intention of "going where I was most needed". It turns out that was unnecessary: because of the size and parallelization of the national movement, there is already plenty in all stages of the pipeline. In addition, the software and workflow are designed so that at every stage (2-3 hours) the data is annotated and repackaged for the next person.

The other thing I noticed about the tracks was that there were WAY more people there to "harvest" than anything else. To me this suggests that, of the people who were aware of the event, the majority of the ones who interpreted it as "for them" were coding people - big surprise. I'm a bit red-faced here because I've always been under the impression that all hackathons say that everyone is welcome regardless of technical skill, but that this is essentially lip service. I was wrong about at least this event and probably in general. Surveying and seeding needed subject matter experts, people familiar with government, and anyone know knows how to gather information on the web. Harvesting needed web-scrapers, sure, but we also needed subject matter experts, and web/UI developers (what just happened?! was it javascript?!). Storytelling needed critical thinkers and policy folks and technical journalists and social media experts and photographers.

Once we had resettled by track, and then again by department (shoutout to team NOAA!) it was about 10am, and I'd say it took me about another hour to familiarize myself with the workflow (how to start, what to check) and choose a dataset that seemed right for me. I was just getting started relearning the Python BeautifulSoup package when many, many pizzas arrived. We all nommed pizza and continued working. Folks were helping each other out, both at the table and between tables via Slack - What does this mean? I'm getting this error, can someone help? Why is it doing this? Did javascript just happen? It was very relaxed and many an "I don't know" was gracefully given and accepted.

I was plagued by a phantom 404 (after I checked the urls!) which ate up a lot of my time, but I eventually solved it (the library I used to check urls preprocessed them, the library I used to download didn't) and finished my download and archiving at home later. I now have the info and logins to contribute independent of an event, and I hope to do so.

I enjoyed the event a lot - I was worried about disorganization and drudgery, but the DataRescue folks (Boston organizers and above) were very organized, and the distributed pipeline meant that individuals having issues didn't cause problems for the general forward progress of the group. There's another event coming up at [Northeastern](https://datarescue-boston.github.io/northeastern/), which I recommend checking out.

Random comments on the event: There were gender neutral and accessible bathrooms, as well as vegetarian and gluten-free food options. There was no ASL/captioning, but all of the information was available in static written form. I'd say attendance was at least 1/3 women.
