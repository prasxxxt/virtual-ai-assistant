
# AI Fifty - Virtual Assistant

AI Fifty is a basic AI based virtual assistant for Microsoft Windows operating system computers. It take voice commands from the user, process the command using basic machine learning algorithm to classify it into intents and perform the task requested by the user.



## Table of Contents
* [Demo](##Demo)
* [Installing requirements](##Installing-requirements)
* [Compatibility](##Compatibility)
* [Skills](##Skills)
* [Future Scope](##Future-scope)
* [CS50 Academic Honesty](##CS50-Academic-Honesty)
    * [Policy](###Policy)
    * [Reasonable](###Reasonable)
    * [Not Reasonable](###Not-reasonable)



## Demo

[![Demo video](https://img.youtube.com/vi/hhb-8s7byR4/0.jpg)](https://www.youtube.com/watch?v=hhb-8s7byR4)


## Installing requirements

This project require some additional python libraries on your system. All required libraries are listed in requirements.txt

```bash
pip install -r requirements.txt
```
If you are facing errors while Installing "pyaudio" then try
```bash
pip install pipwin
pipwin install pyaudio
```
    
## Compatibility
Some functions of AI Fifty is only compatible with Microsoft Windows operating system. For example: launching and closing applications like notepad. But some extra lines of code can be added to make it work on Macintosh or Linux operating system too. Due to lack of resources I haven't implemented it for other Operating systems right now.
## Skills
Features of AI Fifty - 
* Greeting user according to time.
* Introducing itself.
* Repeating speech of ordered by user.
* Launching and closing applications and websites.
* Performing Google Search.
* Performing Wikipedia Search.
* Performing Youtube Search.
* Home automation by switching electrical appliances connected to Network.
* Checking Systems IP Address

### Adding new skill
AI Fifty have some limited no of Features right now but additional features can be added into "/data/intents.json" by appending intent type, utterances for natural language processing, responses to respond after finishing task and creating intent to function mapping in "/skills/functions.py".

### Adding new application or site
For adding application or website in database just append app name or site name and location in "/data/apps.json".
## Future Scope

### Future scope of AI Fifty is promising.

Since AI is one of the most popular technologies on the planet, thanks to its versatility and advanced solutions. It has been growing at a fast pace.

### But what is the future scope of AI Fifty?

Because AI Fifty has in-built funtionality to make it expandable, We can implement much more advanced skills, advanced data management systems, natural language processing and deep learning algorithms, cross platform syncronizations and etc.
## CS50 Academic Honesty
This course’s philosophy on academic honesty is best stated as “be reasonable.” The course recognizes that interactions with classmates and others can facilitate mastery of the course’s material. However, there remains a line between enlisting the help of another and submitting the work of another. The course’s policy characterizes both sides of that line.

### Policy
The essence of all work that you submit to this course must be your own. Unless otherwise specified, collaboration on assessments (e.g., assignments, labs, problem sets, projects, quizzes, or tests) is not permitted except to the extent that you may ask classmates and others for help so long as that help does not reduce to another doing your work for you. Generally speaking, when asking for help, you may show your work to others, but you may not view theirs, so long as you and they respect this policy’s other constraints.

Regret clause. If you commit some act that is not reasonable but bring it to the attention of the course’s heads by emailing certificates@cs50.harvard.edu within 72 hours, the course may impose local sanctions that may include an unsatisfactory or failing grade for work submitted, but the course will not refer the matter for further disciplinary action except in cases of repeated acts.

### Reasonable
* Communicating with classmates about assessments in English (or some other spoken language), and properly citing those discussions.
* Discussing the course’s material with others in order to understand it better.
* Helping a classmate identify a bug in their code, as by viewing, compiling, or running their code after you have submitted *that portion of the pset yourself.
* Incorporating a few lines of code that you find online or elsewhere into your own code, provided that those lines are not themselves solutions to assigned work and that you cite the lines’ origins.
* Sending or showing code that you’ve written to someone, possibly a classmate, so that they might help you identify and fix a bug.
* Submitting the same or similar work to this course that you have submitted previously to this course.
* Turning to the web or elsewhere for instruction beyond the course’s own, for references, and for solutions to technical difficulties, but not for outright solutions to assigned work.
* Whiteboarding solutions with others using diagrams or pseudocode but not actual code.
* Working with (and even paying) a tutor to help you with the course, provided the tutor does not do your work for you.

### Not reasonable
* Accessing a solution to some assessement prior to (re-)submitting your own.
* Accessing or attempting to access, without permission, an account not your own.
* Asking a classmate to see their solution to some assessment before (re-)submitting your own.
* Discovering but failing to disclose to the course’s heads bugs in the course’s software that affect scores.
* Decompiling, deobfuscating, or disassembling the staff’s solutions.
* Failing to cite (as with comments) the origins of code or techniques that you discover outside of the course’s own lessons and integrate into your own work, even while respecting this policy’s other constraints.
* Giving or showing to a classmate a solution to an assessement when it is they, and not you, who is struggling to solve it.
* Manipulating or attempting to manipulate scores artificially, as by exploiting bugs or formulas in the course’s software.
* Paying or offering to pay an individual for work that you may submit as (part of) your own.
* Providing or making available solutions to assessments to individuals who might take this course in the future.
* Searching for or soliciting outright solutions to assessments online or elsewhere.
* Splitting an assessment’s workload with another individual and combining your work.
* Submitting (after possibly modifying) the work of another individual beyond the few lines allowed herein.
* Submitting the same or similar work to this course that you have submitted or will submit to another.
* Viewing another’s solution to an assessment and basing your own solution on it.