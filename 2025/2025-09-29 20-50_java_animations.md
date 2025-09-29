# Java Animations

*Date:* 2025-09-29

*Time:* 20:50

---

Java

Made some progress on my tetris game project today. We're in the final week just finalising some things. I'm adding animations to the line clearing logic. Seems pretty straightforward using the JavaFx animation package. I added the nodes required to be animated to a List and built an animation for them each. Then using parallel transition played each of the registered animations in sync. This required refactoring how the lineclear logic worked so I could register and animate all the correct rows without messing up the indicies on the gamegrid. Initially it worked well but I noticed a bug which caused the boardstate view to desync from the engine state. THe view seemed accurate but pieces were locking and fitting in locations they shouldn't be. I had to trace this back to the way that the async animation wasnt pausing the spawning/locking of new tetromino pieces creating the desync. To fix this... or at least at this point *think* I fixed it I had to refactor the setTetromino method to behave as a continuation. This gave me a bit of practice with my async concepts as I really haven't done enough of this yet. Still need to implement the final sounds but trying to clean up the codebase before I do that.

MongoDB

Really slacking a bit here, Sunday wasn't very productive. Not feeling great about it but really need to try and get some progress made on this assignment. It's going to be big and all at once. I'm going to need to use the weekend for some other projects so need to start refactoring my frontend on this assignment and add the features.

Life

Getting on, still processing what has happened over the last month. It's all been pretty distracting and offputting but this journaling was a product of trying to find meaningful steps to be more productive and change things up. Need to try and count my blessings and be more optimistic and...ruthlessly efficient? like I used to be when I was younger. Bit worried about the upcoming cramming I need to do for all my subjects but hopefully...this is the last time I'll ever need to do this. Still havent been back to gym or been productive in my downtime with those language aspirations. Got some bad associations with it I'll need to work through but that's neither here nor there.
