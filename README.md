welcome to upwork job sender

You can check rss you follow via telegram with this application.

First, enter the telegram bot token on "config" file and  specify how often follow jobs to get write via 

There are two applications here. The first application will continuously monitor the rss resources you have written in the hour or minute interval you specify and save them in the database. The other application will send the applications registered in the database to you via telegram.

go to "config.py" and write bot token, your chat id and how often checking job on upwork rss

To run the application, first run the "upwork.py" file. This is the first application. You can use the code "python upwork.py &" to run it in the background. then run the "main.py" file.

After running the application, give the command "/start" to your bot via telegram.

![start](https://user-images.githubusercontent.com/17255931/111066822-1083be00-84d2-11eb-83bb-a83f978f704c.gif)

Since the application does not have an rss source to follow, you first need to add an rss link.

![addrss](https://user-images.githubusercontent.com/17255931/111067659-56db1c00-84d6-11eb-8826-dd346d1db426.gif)

After adding the rss records, you can give the "/ start" command again. Use the code "/ help" for all commands

![help](https://user-images.githubusercontent.com/17255931/111067785-d5d05480-84d6-11eb-9c51-f97811d859b3.gif)


After the time in the timer setting that you wrote in the "config.py" file, the application reads the rss records and saves all the added jobs to the database. If you want to read these jobs, you can use "/ getjob" code to read all jobs in the database.

![getjob](https://user-images.githubusercontent.com/17255931/111067892-69098a00-84d7-11eb-9c26-71aa15080baa.gif)

The number at the beginning of the jobs from the database represents the id value. If you want to see the details of incoming jobs, you have to use this id value.

![get](https://user-images.githubusercontent.com/17255931/111067989-dae1d380-84d7-11eb-9854-eb4380891e6d.gif)

You can use the code "/ get {id value} title" to get the "title" part of the jobs in the database. You can use "" / get {id value} content "to get the content part. You can also use the code" / get {id value} link" to get the link of the incoming job.

All transactions made by the application are recorded in the database. You can use the code "/ getlog {value}" to see what the application is doing. The timestamp here is based on the time on the server where you run the application.

![getlog](https://user-images.githubusercontent.com/17255931/111068166-ade1f080-84d8-11eb-88c5-b172ab74bbb8.gif)

You can create ready-made text messages for the jobs you want to apply for and save them. The code you need to use for this is "/ addnote {title} {value}"

The first message you will write will be the title. Subsequent articles will represent the content.

![addnote](https://user-images.githubusercontent.com/17255931/111068281-352f6400-84d9-11eb-84c8-33d2031bca56.gif)


To view the notes you have written before, you must use the following code. "/ shownote"

With this code, you can view all notes saved in the database.

![shownote](https://user-images.githubusercontent.com/17255931/111068868-8a6c7500-84db-11eb-9831-9ce793d6ad0b.gif)

To view jobs more easily, you can directly type the id value of the jobs in the telegram bot to get the title and its content.

![direct get job](https://user-images.githubusercontent.com/17255931/111069088-76754300-84dc-11eb-954e-7d831b122311.gif)

According to the rss sources you follow, things will multiply in the database over time. If you want, you can delete all jobs saved in the database with the command "/ deljob".

![dell all job](https://user-images.githubusercontent.com/17255931/111069118-a4f31e00-84dc-11eb-8539-acef83c132d3.gif)


