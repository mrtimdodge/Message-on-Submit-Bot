# Message-on-Submit-Bot for /r/dueling

Before running edit authorized.txt to contain the names of users you want to be able to call the bot, one per line, no extra spaces

Program flow:

1. You start the bot, it will start reading the flair for submissions from /r/dueling, when you first start it it will read back one submission, so make sure the previous submission is NOT a flair with "Game" (only when you start it though)

2. You (or anyone really) make a post with the flair "Game". It has to be that exact flair to work. 

3. The bot posts a comment "#COMMENT HERE WITH KEYWORD poke FOR A POKE WHEN QUIZ IS OPEN"

4. The bot starts reading comments for the keyword, if a comment has the keyword, it adds the user's name to a file

5. You or any user authorized (I have a file named authorized.txt for that list) comments "Duelingbot! Lumos"

6. The bot send out messages saying the game has started and gives a link back to the original post

7. Bot sits and waits for a message with the word "Results" as its subject

8. You (or anyone authorized) send a message with the word "Results" to the bot

9. The bot posts a comment in the original post with the results and "#COMMENT HERE WITH KEYWORD poke FOR A POKE WHEN FULL RESULTS ARE UP"

10. Bot goes back to reading comments for keyword

11. You or You or any user authorized comments "Duelingbot! Nox"

12. Bot sends out messages saying the results are up, and links back to the original post (not sure if thats what you wanted for this part?)

13. Bot goes back to reading submissions and then back to step 2.
