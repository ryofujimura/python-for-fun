import turtle

def fibonacci(n):
    """
    Calculates fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def draw_plant(t, length):
    """
    Draws a plant
    """
    if length > 5:
        t.forward(length)
        t.right(20)
        draw_plant(t, length - 15)
        t.left(40)
        draw_plant(t, length - 15)
        t.right(20)
        t.backward(length)

def main():
    """
    Main function
    """
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("red")
    brad.speed(0)
    draw_plant(brad, 100)
    window.exitonclick()

if __name__ == "__main__":
    main()