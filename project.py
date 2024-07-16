from flask import Flask
app=Flask(__name__)
@app.route('/')
def project():
    return "<h1 style='background:orange'><center>My first routing page</center></h1><h2><center> The Elephant and the Ants</center></h2><p>There was once a pleased elephant who generally harassed smaller animals. He would go to the ant colony and shower water on the ants. The ants, with their size, could just cry. The elephant laughed and threatened the ants that he would kill them.The ants had enough and chose to show the elephant a lesson.They went straight into the elephant's trunk and started messing with him. The elephant started crying in pain. He understood his mistake and apologised to the ants and every one of the animals he had harassed.</p>" 
@app.route('/abc')
def project1():
    return "<h1 style='background:mauve'><center>My second page</center></h1><h2><center> The Hare and the Tortoise</center></h2><p>One day, a hare was showing off how fast he could run. He laughed at the turtle for being so slow. After seeing the overconfidence, the turtle moved him to a race. The hare (rabbit) laughed at the turtle's test, and he accepted his demand.As the race began, the rabbit ran extremely quickly and went far ahead of the turtle and got drained. He thought there was a lot of time to relax as the turtle was far away. Soon he slept, thinking he would win the race easily.However, the turtle(tortoise) kept walking slowly until he arrived at the finish line. The rabbit sees the turtle on the opposite side of the finish line. The turtle had won the race.</p>"
if __name__=='__main__':
    app.run(debug=True)