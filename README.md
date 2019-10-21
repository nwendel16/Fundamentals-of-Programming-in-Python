# Analysis and Reflection

  When I signed up for IT-75 I had no prior knowledge of coding in Python, or any computer language for that matter. If you told me that halfway through the semester, I'd be able to write a Password Locker program that allows users to store and encrypt their passwords, I would have laughed at the thought. The truth is though, by the end of day one I was already writing programs, albeit they were small and simple. With the Python language and the helpful instruction from Professor Amalong I have been able to learn and accomplish many things I never thought possible.
  
  Over the past two months we have been asked to work on a variety of exercises and projects within Python. These tasks have either taught us the fundamentals of a topic or had us put this knowledge together to form a cohesive program. One of the first programs were asked to create was "Hello Turtle". We were asked to create a picture with the use of the turtle module built into Python. I really enjoyed this project because it was one of the first programs I have ever written. I also enjoyed writing a block of code and then testing it to see what the little 'turtle' would print out. It was so cool to me to see lines of code turn into an actual picture. 
  
  Here is the start of what my code looks like: 

```python
import turtle

tt = turtle.Turtle()
tt.color('black' , 'gold')
tt.speed(10)
tt.pensize(3)

tt.begin_fill()
for i in range(12):
    tt.forward(12.5)
    tt.left(90)
    tt.forward(300)
```

  The program I am most proud of is the aforementioned Password Locker program. I am most proud of this piece because it was by far the most difficult project for me to complete. I ran into many problems along the way and it took a lot of trial and error for me to get it to run properly. I think this piece is great because it really is a culmination of everything, we have learned in our class thus far. While it is a functioning program there are many improvements, I would like to make to it. One of those improvements would be for it to save the entered information once the program is closed, which I now have the knowledge to do so I can't wait to go back and implement that into the program. While this project was difficult and time consuming, it has been the most rewarding to complete. 
  
  Here is a peek at one of the functions I created within the program:
  
```python
def view_all():         # Function to print all saved accounts
    print('\n'*35)
    header()
    print('Here are all of your saved accounts:')
    print('\n'*2)
    for k in credentials.keys():        # Searches the credentials dictionary and prints only the keys (accounts)
        print('- ' + str(k) + '\n' + '\n')
    print('\n'*2)
    header()
```

## Unit 1 Projects

  If you would like to view the full code for any of the projects I have created so far this semester follow this link to my [Unit 1 Repository](https://github.com/nwendel16/Fundamentals-of-Programming-in-Python)


[Home](https://nwendel16.github.io/portfolio)
