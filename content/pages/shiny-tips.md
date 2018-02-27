Title: How I Do Shiny
Date: 2017-08-09
Tags: R, Shiny, How-To
Category: Computing

I've had a handful of conversations recently with people learning Shiny who all agree that despite the many available tutorials and examples, sometimes it's hard to figure out how to do what YOU want to do. I think this is exemplified by how long it took me to figure out how to read a CSV into a Shiny app as a global object. So here's a collection of my hard-won pro-tips, as well as some non-obvious approaches for "this shouldn't be complicated" tasks.

### 1. If the "invalidation" (odd-shaped boxes with arrows) explanations don't make sense to you, don't sweat it.

Some understanding of how the reactivity works will probably help you in the long right, but don't feel like you need to 110% understand it to get started. Try out the built-in [to RStudio] geyser app, and experiment with changing the inputs and outputs. You can build useful stuff with only that logic. Reactivity boils down to a "downstream flow" - when an input changes, everything that uses it (or uses something that uses it, etc etc) recalculates/rerenders. One thing about this that can be tricky is a situation where you recalculate based on an input, and use another input in some unexciting way like generating a label - they are both equally able to trigger things downstream.

### 2. If there's no output, but no error (and you're not already error-handling it), check your in/out alignment

I wish someone had told me this when I was getting started. If you do this in server.R:
```r
output$mytable <- renderDataTable({table_code})
```

but pair it with this in ui.R:
```r
tableOutput("mytable")
```

You will pull your hair out looking for the silent bug. I have also often done this by putting `renderPlot` instead of `plotOutput` because DUH, I want it to render in the UI.

### 3. Mutable globals exist, they're just different. And you should use them.

You can load a csv into a data.frame (and maybe manipulate it) outside the server function and refer to that globally within the server function. You quickly discover, however, that if you want to modify it based on user input, you can no longer just refer to it like a regular R variable. That's because everything inside the server function must be a "reactive" variable (unless it's inside the curly braces of another function). So to limit code duplication, you should consider making a reactive object if you're re-using the modified object. Here's an example from my life:
```r
my_df <- read_tsv("cats.txt")
shinyServer(function(input, output) {
  
  reactive_df <- reactive({
    my_df <- my_df %>% filter(cat == "Herbie")
  })
  
  output$mytable <- renderDataTable({
    reactive_df() # you gotta reference it like a function
  })
  
  output$mydownload <- downloadHandler(
    filename = "Herbie.txt",
    content = function(file){
      write.table(reactive_df(), file)
    }
  )
  
})
```

### 4. Use dplyr to subset globals instead of making new reactive objects

So that was handy, right? But maybe you're like me, and you want to show URLs as links in the webapp, but text in the download. [Dplyr](https://cran.r-project.org/web/packages/dplyr/index.html) has been a LIFESAVER for me in this regard. Let me revisit the example above:
```r
reactive_df <- reactive({
  my_df <- my_df %>% filter(cat == "Herbie")
})
  
output$mytable <- renderDataTable({
  reactive_df() %>% mutate(PetfinderURL = createLink(PetfinderURL)) 
}, escape = FALSE) # this is so the link will display as a link, not the HTML
  
output$mydownload <- downloadHandler(
  filename = "Herbie.txt",
  content = function(file){
    write.table(reactive_df(), file)
  }
)
```

### 5. Using very long lists for dropdowns

> 1) I found it difficult to find examples for loading dropdown choices from a file. I am a bioinformatician. It sucked. Short version: ui.R can't access variables from server.R. If you'd like to `read_csv()` a file, you have to do it a) in a global.R file if you're doing a "2 file app", or b) outside both server and ui functions if you're doing a "1 file app".

> 2) For most of the apps I write, the `selectizeInput()` is populated by gene names. So that's like 30k entries, and although that's a "fast enough" load when you're just starting a data analysis, it's not fast enough for your webapp users. The best solution I've found for this is `updateSelectizeInput()`. Two of its parameters are tricky: _session_, and _server_. For the former, you just need to add "session" as a parameter of the server function: `shinyServer(function(input, output, session) {...}` and you're done. For the latter, you have to choose whether to use the server for the `update`. Using `server = TRUE` is faster, but it triggers a reactive event, so the page in effect loads twice if the page is initialized with a selection (`selectizeInput(..., selected = "value")` in ui.R). Nobody seems to be bothered by this but me, so if you know how to get around this, get at me on the twitters. If you use `server = FALSE` it's a little slower, but still better than `selectizeInput()` and also it behaves like you want it to. 

### 6. Use sqlite for faster lookup

Again, genes: there are a lot of them. Doing a lookup on a data.frame is surprisingly unacceptably slow. This should not be what slows down your app! SQLite aka sqlite3 comes standard with most Linux distros I've used, as well as Mac OSX, and it's basically like awesome csv. Read up on it, and/or use [RSQLite](https://cran.r-project.org/web/packages/RSQLite/index.html) to create and access a database (it can be one table, tbh) and your lookups will be so much faster (at least on the server, ymmmv on a laptop).

### 7. Use lists to return multiple values

This falls under "feels hacky" but if you find yourself writing an ... elaborate `reactive()` function, you might want to return multiple values. For me this happened when I wanted to process three dataframes the exact same way and did it in a loop rather than create three independent reactive functions. You can use a list to return multiple values, and just pass the variable around, accessing each variable with `secretly_a_list()[[1]]` etc. The truth is, Shiny can basically do anything, if you're willing to get crazy.

### 8. The syntax for using DT::renderDataTable is `output$mydt <- DT::renderDataTable({datatable(dat, args)})`

That's basically it. If you google around for "datatable shiny" there are lots of fabulous options you can use, and friggin NONE of them explain the syntax. Boom. Done.

#### Alright, I've spent enough time writing this. PUBLISH!
